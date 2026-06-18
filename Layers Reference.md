Layer 0: Hardware
AMR base, LiDAR, RealSense, mic, speaker

Layer 1: ROS 2 device layer
Ranger driver, odom, TF, camera driver, LiDAR driver

Layer 2: Autonomy layer
Nav2, AMCL, costmaps, planner, controller, recovery

Layer 3: HRI layer
Speech-to-text, text-to-speech, command parser, UI/UX

Layer 4: Reasoning / AI agent layer
Local LLM or Gemini Robotics-ER

Layer 5: Safety / command validation layer
Allowed actions, stop rules, station list, confirmation logic




Use this order:

1. Finish simple local speech interaction
2. Add ROS status replies
3. Add safe named-station commands
4. Add UI/UX
5. Add local LLM for natural language
6. Add Gemini Robotics-ER for advanced vision/spatial reasoning




FINAL PROJECT GOAL
Safe + Explainable Embodied AI Navigation for AMR
│
├── 1. BASE ROBOT LAYER
│   │
│   ├── ROS2 Humble
│   ├── Ranger AMR bringup
│   ├── SICK lidar
│   ├── TF tree
│   ├── odometry
│   └── motor/control stability
│
│   Purpose:
│   Make sure the robot can move reliably.
│
│   Your current focus:
│   Stabilize AMR control and movement.
│
├── 2. NAVIGATION LAYER
│   │
│   ├── Nav2
│   ├── AMCL localization
│   ├── map
│   ├── costmap
│   ├── planner
│   ├── controller
│   └── recovery behavior
│
│   Purpose:
│   Robot can move from one station to another.
│
│   Target:
│   Home → Station A → Station B → Lab
│
├── 3. SPEECH INTERACTION LAYER
│   │
│   ├── Speech-to-text
│   ├── Text-to-speech
│   ├── voice command input
│   └── spoken robot response
│
│   Purpose:
│   Human can talk to the robot.
│
│   Example:
│   User: "Go to the lab."
│   Robot: "Understood. I am going to the lab."
│
├── 4. GEMINI ROBOTICS-ER REASONING LAYER
│   │
│   ├── command understanding
│   ├── task reasoning
│   ├── blocked-path explanation
│   ├── recovery suggestion
│   └── human-friendly explanation
│
│   Purpose:
│   Gemini understands the situation and explains it.
│
│   Important:
│   Gemini does NOT control motors.
│
│   Correct role:
│   Gemini reasons.
│   Nav2 moves.
│
├── 5. MISSION MANAGER LAYER
│   │
│   ├── receives Gemini output
│   ├── checks destination
│   ├── maps destination to waypoint
│   ├── sends goal to Nav2
│   └── tracks mission state
│
│   Purpose:
│   Converts AI output into robot mission commands.
│
│   Example:
│   "go to lab" → lab waypoint → Nav2 goal
│
├── 6. SAFETY SUPERVISOR LAYER
│   │
│   ├── checks obstacle distance
│   ├── checks valid destination
│   ├── checks robot localization
│   ├── checks emergency stop
│   ├── limits unsafe movement
│   └── rejects unsafe commands
│
│   Purpose:
│   Prevent AI from causing unsafe robot behavior.
│
│   Rule:
│   Gemini can suggest.
│   Safety supervisor approves.
│
├── 7. EXPLAINABILITY DISPLAY LAYER
│   │
│   ├── current goal
│   ├── robot state
│   ├── Gemini reasoning
│   ├── safety status
│   └── recovery status
│
│   Purpose:
│   Humans can understand what the robot is doing.
│
│   Example display:
│   "Obstacle detected."
│   "I am waiting and replanning safely."
│
└── 8. FINAL DEMO SCENARIO
    │
    ├── User gives voice command
    ├── Gemini understands task
    ├── Safety supervisor checks command
    ├── Nav2 sends robot to destination
    ├── Obstacle appears
    ├── Gemini explains the issue
    ├── Robot replans safely
    └── Robot completes delivery
