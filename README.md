# Posture-and-Ergonomics-Monitoring-for-Health-Intervention
Poor posture and bad ergonomics during daily activities especially long hours of sitting or working on computers can lead to neck pain, back pain and other musculoskeletal disorder. The project aims to monitor and correct user posture in real time using computer vision and sensor based techiniques, providing health intervention feedback to promote better ergonomics and long term well being.


OBJECTIVE 
1. Detect improper posture using vision based or sensor based inputs.
2. Alert users when incorrect posture is maintained for too long.
3. Analyze posture patterns to provide personalized ergonomics recommendations.
4. Support early intervention to prevent posture related health issues.

KEY FEATURES.
1. Real time posture detection(such as sitting,standing,stretching,leaning,slouching).
2. Automatic alerts generated for poor posture.
3. Dashboardor report showing poature analytic and daily score.
4. Integraton with wearable sensors
5. Health tips and ergonomics recommendations.

TECHNOLOGIES USED 
1.PROGRAMMING LANGUAGE:- Python
2.Implementation Tool:- MATLAB/GOOGLE COLAB 
3.Libraries- OpenCV,Mediapipe,TensorFlow/PyTorch,NumPy,Pandas,Matplotlib
4.Interface:- Web/Mobile dashboard for feedback visualization.

WORKING PRINCIPLE 
The system works by continuously monitoring the users posture using either a camera or body mounted sensors. The camera based approach uses computer vision techiniques to detect key body landmarks such as shoulders, neck and spine alignment while sensors(like MPU6050) to measure body angles and orientation. The captured data is processed to extract relevant features that represent the users sitting or standing posture. A classification model or threshold based logic is then applied to determine whether the posture is correct or incorrect. When an improper posture is detected and sustained for a predefined duration, the system generates an alert such as a sound,vibration or on-screen notification to remind the user to adjust their position.
Simultaneiusly, the posture data is logged to analyze long term bahaviour and geenrate health insights, The real time feedback loop helps users develop better ergonomics habits and reduces the risk of posture related health problems.
