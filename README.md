# Vehicle Detection, Classification, and Counting

This project uses OpenCV for detecting, counting, and classifying vehicles from a video feed. The vehicles are classified as "Car" or "Truck" based on specific size criteria, and the application keeps track of the vehicles moving up and down across a predefined line.

## Table of Contents
- [Overview](#overview)
- [Features](#features)
- [Requirements](#requirements)

## Overview
The system processes each frame of a video file, applies background subtraction and contour extraction, and detects moving vehicles. Vehicles are counted based on crossing a specified line, and they are classified as either "Car" or "Truck" based on aspect ratio and area. The resulting frame shows the count and classification of vehicles in real-time.

## Features
- **Vehicle Detection:** Detects moving vehicles using background subtraction.
- **Vehicle Counting:** Counts vehicles crossing a predefined line.
- **Vehicle Classification:** Classifies vehicles as "Car" or "Truck" based on size.
- **Real-Time Display:** Displays the processed video with bounding boxes, counters, and classifications.

## Requirements
The project requires the following libraries:
- [OpenCV](https://opencv.org/) - for video processing and contour detection.
- [NumPy](https://numpy.org/) - for array manipulation.

