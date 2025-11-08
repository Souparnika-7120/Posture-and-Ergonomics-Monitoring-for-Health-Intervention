"""
Main Script: Posture and Ergonomics Monitoring for Health Intervention
Author: [Your Name]
Description:
This program captures live video from your webcam, detects posture using Mediapipe,
and alerts the user if a bad posture is maintained for a long time.
"""

import cv2
import mediapipe as mp
import time
from posture_detector import check_posture
from alert_system import alert_user

# Initialize webcam
cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print("Error: Could not open webcam.")
    exit()

# Variables
bad_posture_duration = 0
alert_threshold = 5  # seconds before alert
start_time = 0

print("🧍‍♀ Posture Monitoring Started... Press 'q' to exit.")

while True:
    success, frame = cap.read()
    if not success:
        print("Error: Unable to read from webcam.")
        break

    # Flip the frame for a mirror view
    frame = cv2.flip(frame, 1)

    # Check posture using helper function
    posture_status = check_posture(frame)

    # Display posture status on screen
    cv2.putText(frame, f"Posture: {posture_status}", (30, 50),
                cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0) if posture_status == "Good" else (0, 0, 255), 3)

    # Track how long the user stays in bad posture
    if posture_status == "Bad":
        if start_time == 0:
            start_time = time.time()
        bad_posture_duration = time.time() - start_time

        # If bad posture maintained for more than threshold, trigger alert
        if bad_posture_duration > alert_threshold:
            alert_user()
            start_time = 0  # reset timer after alert
    else:
        start_time = 0
        bad_posture_duration = 0

    # Show webcam feed
    cv2.imshow("Posture Monitoring", frame)

    # Exit on 'q' key
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
