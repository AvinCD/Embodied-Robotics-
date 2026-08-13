#!/usr/bin/env python3

import os
import json
import datetime
from pathlib import Path

from google import genai
from PIL import Image


MODEL_NAME = "gemini-robotics-er-1.6-preview"

PROJECT_ROOT = Path(__file__).resolve().parents[2]
IMAGE_PATH = PROJECT_ROOT / "dashboard/state/latest_scene.jpg"
STATE_PATH = PROJECT_ROOT / "dashboard/state/gemini_scene_state.json"


def save_state(data: dict):
    STATE_PATH.parent.mkdir(parents=True, exist_ok=True)

    with open(STATE_PATH, "w", encoding="utf-8") as file:
        json.dump(data, file, indent=2)


def main():
    api_key = os.environ.get("GEMINI_API_KEY")

    if not api_key:
        raise RuntimeError("GEMINI_API_KEY is not set.")

    if not IMAGE_PATH.exists():
        raise FileNotFoundError(f"Image not found: {IMAGE_PATH}")

    client = genai.Client(api_key=api_key)
    image = Image.open(IMAGE_PATH)

    prompt = """
You are an advisory visual reasoning layer for a ROS 2 autonomous mobile robot.

Analyze the scene in the image and return only valid JSON.

Required JSON format:
{
  "scene_status": "CLEAR or BLOCKED or CAUTION or UNKNOWN",
  "risk_level": "LOW or MEDIUM or HIGH or UNKNOWN",
  "visible_objects": ["object1", "object2"],
  "summary": "One short sentence describing the scene.",
  "navigation_hint": "One short robot-relevant advisory.",
  "spoken_advisory": "One short sentence suitable for robot speech.",
  "movement_authority": "none"
}

Rules:
- Do not command the robot to move.
- Do not generate velocity commands.
- Do not claim certainty if the image is unclear.
- Keep all output advisory only.
"""

    response = client.models.generate_content(
        model=MODEL_NAME,
        contents=[prompt, image],
    )

    response_text = response.text if response.text else "{}"

    try:
        parsed = json.loads(response_text)
    except Exception:
        parsed = {
            "scene_status": "UNKNOWN",
            "risk_level": "UNKNOWN",
            "visible_objects": [],
            "summary": "Could not parse Gemini response.",
            "navigation_hint": "Operator should verify the scene manually.",
            "spoken_advisory": "I could not reliably understand the scene.",
            "movement_authority": "none",
            "raw_response": response_text,
        }

    parsed["timestamp"] = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    parsed["model"] = MODEL_NAME

    save_state(parsed)

    print(json.dumps(parsed, indent=2))


if __name__ == "__main__":
    main()
