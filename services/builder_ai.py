
# builder_ai.py
import datetime

def log_user_action(action):
    with open("ai_behavior_log.txt", "a") as f:
        f.write(f"{datetime.datetime.now()}: {action}\n")

def get_suggestions():
    return [
        "Consider making 'Root Cause' required when issue is a breakdown.",
        "Automate part assignment for frequently paired assets.",
        "Optimize form layout for mobile users."
    ]
