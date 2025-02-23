# **Mess Entry Monitoring System**

## Overview
The Mess Entry Monitoring System** is designed to automatically track and count individuals entering a mess hall using cameras. The system utilizes AI algorithms to accurately detect people, handle occlusions, filter out non-human objects, and provide real-time analysis. It is built to offer precise monitoring, enhance security, and improve entry management.

Key features of the system include:
- Real-time people tracking and counting.
- Handling of occlusions and overlapping individuals.
- Filtering out non-human objects from the tracking system.
- Real-time updates and monitoring via a user-friendly interface.

## Features

### Core Workflow
1. **Real-Time People Tracking and Counting**:
   - The system uses cameras to capture video footage and AI-powered models (e.g., YOLO) to detect and count people entering the mess hall in real-time.

2. **Occlusion Handling**:
   - Advanced tracking algorithms (like DeepSORT) are used to handle occlusions when individuals are partially blocked or overlapping, ensuring accurate counting even in complex scenarios.

3. **Non-Human Object Filtering**:
   - The system is designed to filter out non-human objects, ensuring that only people are tracked and counted.

4. **Real-Time Updates**:
   - Provides real-time updates on the number of people in the mess hall, and updates are displayed on the dashboard for monitoring and analysis.


## Installation

### Prerequisites
- **Python 3**
- **YOLOv8** (or another object detection model)
- **DeepSORT** (for tracking)
- **Face Recognition Libraries** (optional: `dlib`, `face_recognition`)

### TechStack
#### Frontend:
- **React.js** – UI framework for building the web interface.
- **React Router** – For navigation between Home and Upload Video pages.
- **Fetch** – For sending video files to the backend.
- **Tailwind CSS** – For styling.

#### Backend:
- **Flask** – Lightweight web framework for handling API requests.
- **OpenCV** – For real-time video processing.
- **YOLOv8 (Ultralytics)** – For object detection in videos trained on custom datasets.
- **FastAPI** – For improved API handling.
- **HTTP Streaming** – For video stream handling.

#### Datasets:
- **WIDER FACE** – Handling occlusion and multiple face detection, contained 12800 images.

#### Storage & Hosting:
- **Vercel** – For frontend deployment.


### Steps
1. Clone the repository:
   ```bash
   git clone https://github.com/SarimMalik01/Crowd-Management.git
   ```
2. Navigate to the project directory:
   ```bash
   cd Web
   ```
3. Install dependencies:
   ```bash
   npm install
   ```

5. Run the application:
   ```bash
   npm start
   ```
6. Access the application at `http://localhost:3000`.

## Project Structure
```
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

```

## Features in Detail

### Real-Time Entry Tracking
- **AI-Powered People Detection**: YOLOv8 detects people in the camera feed and counts the number of entries as individuals enter the mess hall. This ensures precise tracking of people in real-time.
  
- **Handling Occlusions**: The DeepSORT algorithm ensures that individuals are tracked even when temporarily obscured by other people or objects. This enhances the system's ability to provide accurate counts even in crowded or complex scenarios.

### Optional Features
1. **Facial Recognition**: The system can integrate facial recognition technology to identify individuals entering the mess hall. This feature helps in verifying identities and preventing unauthorized access or duplicate counting of individuals.

2. **RFID Integration**: The system can also integrate with RFID tags to automatically track individuals entering the mess hall. This feature provides an additional layer of security and helps in the automatic identification of people as they enter.

## Future Enhancements
1. **Enhanced AI Models**: In the future, we aim to upgrade to more advanced object detection models to further improve the accuracy of the system in detecting and tracking people.

2. **Web Dashboard**: A web-based dashboard could be developed to visualize real-time data, entry counts, and provide detailed individual analysis for better monitoring.

3. **Additional Sensors**: Integration of additional sensors (such as infrared or motion sensors) could improve the system’s ability to handle crowd density and provide more accurate entry analysis.

## Contributing
Contributions are welcome! Please follow these steps:
1. Fork the repository.
2. Create a new branch for your feature:
   ```bash
   git checkout -b feature-name
   ```
3. Commit your changes:
   ```bash
   git commit -m "Add feature description"
   ```
4. Push to your branch:
   ```bash
   git push origin feature-name
   ```
5. Open a pull request.


---

