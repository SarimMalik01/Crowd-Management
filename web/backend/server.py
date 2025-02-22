from flask import Flask, Response, request, jsonify
from flask_cors import CORS  
import cv2
import torch
from ultralytics import YOLO
from src.tracking import DeepSORTTracker
from src.count_manager import CrowdCounter

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes

# Load YOLO model
model = YOLO("database/yolov8n.pt")

# Load Tracker and Counter
tracker = DeepSORTTracker()
counter = CrowdCounter()

video_path = None  # To store uploaded video path
current_count = 0  # To store real-time count


def generate_frames():
    """ Generator function to yield processed frames """
    global video_path, current_count
    if not video_path:
        return  # No video uploaded yet

    cap = cv2.VideoCapture(video_path)

    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break

        # YOLO Detection
        results = model(frame)
        detections = [
            (int(box.xyxy[0][0]), int(box.xyxy[0][1]), int(box.xyxy[0][2]), int(box.xyxy[0][3]), float(box.conf[0]))
            for r in results for box in r.boxes
            if int(box.cls[0]) == 0 and float(box.conf[0]) > 0.3  # Detect only persons
        ]

        # Object Tracking
        tracked_objects = tracker.update(detections, frame)

        # People Counting
        current_count = counter.update(tracked_objects)

        # Draw bounding boxes and labels
        for obj in tracked_objects:
            x1, y1, x2, y2, obj_id = obj
            cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 2)
            cv2.putText(frame, f"ID {obj_id}", (x1, y1 - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)

        cv2.putText(frame, f"Total Count: {current_count}", (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)

        # Encode frame as JPEG
        _, buffer = cv2.imencode('.jpg', frame)
        frame_bytes = buffer.tobytes()

        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame_bytes + b'\r\n')

    cap.release()


@app.route('/upload-video', methods=['POST'])
def upload_video():
    """ Handle video upload """
    global video_path
    file = request.files['video']
    video_path = f"./uploads/{file.filename}"
    file.save(video_path)
    return {"message": "Video uploaded successfully", "stream_url": "/video-feed"}, 200


@app.route('/video-feed')
def video_feed():
    """ Route for live video streaming """
    return Response(generate_frames(), mimetype='multipart/x-mixed-replace; boundary=frame')


@app.route('/get-count')
def get_count():
    """ API to get the current people count """
    return jsonify({"count": current_count})


if __name__ == '__main__':
    app.run(debug=True)
