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
