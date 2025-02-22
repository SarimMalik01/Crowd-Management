Team Name: Synapse

Team Members:
Sarim Malik
Ankit Chaurasiya
Om Jain
Himanshi Verma
Aakarsh Bibhaw

AI-powered Mess Entry Monitoring System

Overview
The AI-powered Mess Entry Monitoring System is designed to automatically track and count individuals entering a mess hall using cameras. The system utilizes AI algorithms to accurately detect people, handle occlusions, filter out non-human objects, and provide real-time analysis. It is built to offer precise monitoring, enhance security, and improve entry management.

Key features of the system include:

Real-time people tracking and counting.
Handling of occlusions and overlapping individuals.
Filtering out non-human objects from the tracking system.
Real-time updates and monitoring via a user-friendly interface.
Optional features such as facial recognition or RFID for identity verification and duplicate detection.
Features
Core Workflow
Real-Time People Tracking and Counting:

The system uses cameras to capture video footage and AI-powered models (e.g., YOLO) to detect and count people entering the mess hall in real-time.
Occlusion Handling:

Advanced tracking algorithms (like DeepSORT) are used to handle occlusions when individuals are partially blocked or overlapping, ensuring accurate counting even in complex scenarios.
Non-Human Object Filtering:

The system is designed to filter out non-human objects, ensuring that only people are tracked and counted.
Real-Time Updates:

Provides real-time updates on the number of people in the mess hall, and updates are displayed on the dashboard for monitoring and analysis.
Optional Features
Facial Recognition:

For identity verification and duplicate detection, the system can integrate facial recognition models to verify identities of individuals entering the mess hall.
RFID Integration:

Supports RFID tags for entry verification, offering an additional layer of security and allowing for tracking of individuals using their RFID cards.
Installation
Prerequisites
Python 3
YOLOv8 (or another object detection model)
DeepSORT (for tracking)
Face Recognition Libraries (optional: dlib, face_recognition)


TechStack : 

Frontend :
React.js – UI framework for building the web interface.
React Router – For navigation between Home and Upload Video pages.
Fetch – For sending video files to the backend.
Tailwind CSS – For styling.
Backend :
Flask – Lightweight web framework for handling API requests.
OpenCV – For real-time video processing.
YOLOv8 (Ultralytics) – For object detection in videos trained on custom datasets.
FastAPI  
HTTP Streaming
Datasets:
WIDER FACE - Handling occlusion and multiple face detection, contained 12800 images

Storage & Hosting:
Vercel – For frontend deployment.
Steps
Clone the repository:

bash
Copy
git clone https://github.com/your-username/mess-entry-monitoring-system.git
cd mess-entry-monitoring-system
Install dependencies:

bash
Copy
pip install -r requirements.txt
Download YOLOv8 model weights:

Download YOLOv8 model weights and place them in the models/ directory.
Configure the environment:

Set up the camera feed or video file that will be used for entry tracking.
If using MongoDB, configure the database connection in the .env file (optional).
Run the system:

bash
Copy
python main.py
Access the application at http://localhost:5000 (or the specified port).

Technology Stack
Frontend: React.js, Tailwind CSS (optional, for dashboard display)
Backend: Python (OpenCV, YOLOv8, DeepSORT)
Database: MongoDB (optional)
AI Integration: YOLOv8 (for people detection), DeepSORT (for tracking)
Optional: Facial Recognition (dlib, face_recognition), RFID integration
Project Structure
css
Copy
Mess-Entry-Monitoring-System
├── public
├── src
│   ├── components
│   ├── models
│   ├── utils
│   ├── services
│   └── styles
├── .env
├── main.py
├── requirements.txt
└── README.md
Features in Detail
Real-Time Entry Tracking
AI-Powered People Detection: YOLOv8 detects people in the camera feed and counts the number of entries.
Handling Occlusions: DeepSORT keeps track of individuals, even if they are temporarily obscured by other people or objects.
Optional Features
Facial Recognition: Identifies individuals entering the mess hall and verifies their identity. This can help prevent unauthorized access and duplicate counting.
RFID Integration: Tracks individuals using RFID cards, allowing them to be identified automatically as they enter.
Future Enhancements
Enhanced AI Models: Upgrade to more advanced object detection models for improved accuracy.
Web Dashboard: Integrate a web dashboard to visualize real-time data, entry counts, and individual analysis.
Additional Sensors: Integration of sensors to better handle crowd density and improve entry analysis.
Contributing
Contributions are welcome! Please follow these steps:

Fork the repository.
Create a new branch for your feature:
bash
Copy
git checkout -b feature-name
Commit your changes:
bash
Copy
git commit -m "Add feature description"
Push to your branch:
bash
Copy
git push origin feature-name
Open a pull request.
Contact
For any queries or support, please contact us at support@messentrymonitor.com.
