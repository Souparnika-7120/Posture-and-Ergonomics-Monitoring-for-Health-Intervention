"""
Module: alert_system.py
Purpose: Generates alerts when poor posture is detected for long durations.
"""

import platform

def alert_user():
    print("⚠ Warning: Bad posture detected! Please sit upright.")

    # Play sound based on OS
    os_name = platform.system()
    if os_name == "Windows":
        import winsound
        winsound.Beep(800, 800)
    else:
        print("\a")  # Terminal beep for Mac/Linux
