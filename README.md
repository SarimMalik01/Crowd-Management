# **Team Name**: Synapse

**Team Members**:
- Sarim Malik
- Ankit Chaurasiya
- Om Jain
- Himanshi Verma
- Aakarsh Bibhaw

# **AI-powered Mess Entry Monitoring System**

## Overview
The **AI-powered Mess Entry Monitoring System** is designed to automatically track and count individuals entering a mess hall using cameras. The system utilizes AI algorithms to accurately detect people, handle occlusions, filter out non-human objects, and provide real-time analysis. It is built to offer precise monitoring, enhance security, and improve entry management.

Key features of the system include:
- Real-time people tracking and counting.
- Handling of occlusions and overlapping individuals.
- Filtering out non-human objects from the tracking system.
- Real-time updates and monitoring via a user-friendly interface.
- Optional features such as facial recognition or RFID for identity verification and duplicate detection.

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

