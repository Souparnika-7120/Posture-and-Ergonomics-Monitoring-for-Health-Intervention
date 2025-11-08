"""
Module: posture_detector.py
Purpose: Detect user's posture using Mediapipe Pose estimation.
"""

import mediapipe as mp
import cv2

mp_pose = mp.solutions.pose
pose = mp_pose.Pose()

def check_posture(frame):
    img_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    results = pose.process(img_rgb)

    if results.pose_landmarks:
        landmarks = results.pose_landmarks.landmark
        shoulder_left = landmarks[mp_pose.PoseLandmark.LEFT_SHOULDER]
        shoulder_right = landmarks[mp_pose.PoseLandmark.RIGHT_SHOULDER]
        ear_left = landmarks[mp_pose.PoseLandmark.LEFT_EAR]
        ear_right = landmarks[mp_pose.PoseLandmark.RIGHT_EAR]

        # Simple heuristic: if ears drop too low relative to shoulders, posture is bad
        ear_shoulder_dist = abs(ear_left.y - shoulder_left.y)
        shoulder_diff = abs(shoulder_left.y - shoulder_right.y)

        if ear_shoulder_dist > 0.08 or shoulder_diff > 0.05:
            return "Bad"
    return "Good"
