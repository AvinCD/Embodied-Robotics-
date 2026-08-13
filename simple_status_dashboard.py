#!/usr/bin/env python3

import json
from pathlib import Path
from flask import Flask, render_template_string


PROJECT_ROOT = Path(__file__).resolve().parents[1]

ROBOT_STATE_PATH = PROJECT_ROOT / "dashboard/state/robot_state.json"
GEMINI_STATE_PATH = PROJECT_ROOT / "dashboard/state/gemini_scene_state.json"

app = Flask(__name__)


DEFAULT_ROBOT_STATE = {
    "robot_status": "IDLE",
    "navigation_status": "Waiting",
    "current_goal": "None",
    "path_status": "Unknown",
    "updated": "",
}

DEFAULT_GEMINI_STATE = {
    "scene_status": "Waiting",
    "risk_level": "Unknown",
    "summary": "No scene analysis yet.",
    "navigation_hint": "Waiting for advisory.",
    "spoken_advisory": "No advisory yet.",
    "movement_authority": "none",
    "timestamp": "",
}


HTML = """
<!DOCTYPE html>
<html>
<head>
    <title>Explainable AMR Dashboard</title>
    <meta http-equiv="refresh" content="3">
    <style>
        body {
            margin: 0;
            font-family: Arial, sans-serif;
            background: #0b1220;
            color: white;
        }

        .header {
            padding: 24px;
            background: #123c69;
            text-align: center;
        }

        .header h1 {
            margin: 0;
            font-size: 34px;
        }

        .container {
            padding: 24px;
            display: grid;
            grid-template-columns: 1fr 1fr;
            gap: 20px;
        }

        .card {
            background: #172338;
            border: 1px solid #2f4f73;
            border-radius: 14px;
            padding: 20px;
        }

        .card h2 {
            color: #7fc7ff;
            margin-top: 0;
        }

        .row {
            font-size: 18px;
            margin: 12px 0;
        }

        .label {
            color: #9cc8ed;
            font-weight: bold;
        }

        .footer {
            text-align: center;
            padding: 18px;
            color: #9cc8ed;
        }
    </style>
</head>
<body>

<div class="header">
    <h1>Safe and Explainable AMR Dashboard</h1>
    <p>ROS 2 Nav2 Navigation · Gemini Advisory Reasoning · Voice Explanation</p>
</div>

<div class="container">

    <div class="card">
        <h2>Robot Status</h2>
        <div class="row"><span class="label">Robot:</span> {{ robot.robot_status }}</div>
        <div class="row"><span class="label">Navigation:</span> {{ robot.navigation_status }}</div>
        <div class="row"><span class="label">Goal:</span> {{ robot.current_goal }}</div>
        <div class="row"><span class="label">Path:</span> {{ robot.path_status }}</div>
        <div class="row"><span class="label">Updated:</span> {{ robot.updated }}</div>
    </div>

    <div class="card">
        <h2>Gemini Scene Advisory</h2>
        <div class="row"><span class="label">Scene:</span> {{ gemini.scene_status }}</div>
        <div class="row"><span class="label">Risk:</span> {{ gemini.risk_level }}</div>
        <div class="row"><span class="label">Summary:</span> {{ gemini.summary }}</div>
        <div class="row"><span class="label">Hint:</span> {{ gemini.navigation_hint }}</div>
        <div class="row"><span class="label">Authority:</span> {{ gemini.movement_authority }}</div>
        <div class="row"><span class="label">Timestamp:</span> {{ gemini.timestamp }}</div>
    </div>

</div>

<div class="footer">
    Gemini advisory only. ROS 2 Nav2 retains movement authority.
</div>

</body>
</html>
"""


def load_json(path, default):
    try:
        if path.exists():
            with open(path, "r", encoding="utf-8") as file:
                return json.load(file)
    except Exception:
        pass

    return default


@app.route("/")
def index():
    robot = load_json(ROBOT_STATE_PATH, DEFAULT_ROBOT_STATE)
    gemini = load_json(GEMINI_STATE_PATH, DEFAULT_GEMINI_STATE)

    return render_template_string(
        HTML,
        robot=robot,
        gemini=gemini,
    )


if __name__ == "__main__":
    print("Dashboard running at http://0.0.0.0:5000")
    app.run(host="0.0.0.0", port=5000, debug=False)
