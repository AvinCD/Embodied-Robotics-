# Safe and Explainable Embodied AI Navigation for Autonomous Mobile Robots

## Overview

This project presents a ROS2-based Autonomous Mobile Robot (AMR) framework that integrates:

* Autonomous navigation using ROS2 Nav2
* Embodied AI reasoning using Gemini AI
* Verified safety supervision
* Explainable human-robot interaction

The objective of this project is to develop a mobile robot capable of:

1. Navigating autonomously in dynamic environments
2. Explaining its decisions in real time
3. Safely handling unexpected obstacles and failures
4. Improving human trust through transparent robot reasoning

Unlike traditional autonomous robots that operate as black-box systems, this project focuses on combining AI reasoning with safe and explainable robot execution.

---

# Project Motivation

Recent developments in embodied AI and Vision-Language Models (VLMs), such as Gemini Robotics AI, allow robots to reason about environments before acting.

However, many current AI robotic systems:

* lack verified safety constraints,
* do not explain robot decisions clearly,
* and cannot guarantee safe execution on real mobile platforms.

This project addresses these limitations by integrating:

* AI reasoning,
* ROS2 autonomous navigation,
* and a verified safety layer

into a single explainable robotic framework.

---

# Project Objectives

The main objectives of this project are:

* Develop a stable ROS2 autonomous navigation system
* Integrate Gemini AI as a high-level reasoning layer
* Design a safety verification layer for robot execution
* Display robot reasoning transparently to nearby users
* Improve human trust and interaction with autonomous robots

---

# Proposed System Architecture

---
                ┌────────────────────┐
                │ Gemini AI Reasoning│
                │  Embodied Thinking │
                └─────────┬──────────┘
                          │
            High-Level Reasoning Output
                          │
                ┌─────────▼──────────┐
                │ Safety Supervisor  │
                │ Verified Execution │
                └─────────┬──────────┘
                          │
                ┌─────────▼──────────┐
                │ ROS2 Nav2 Stack    │
                │ Localization + Nav │
                └─────────┬──────────┘
                          │
                ┌─────────▼──────────┐
                │ AgileX Ranger AMR  │
                └────────────────────┘
```

---

# Key Features

## 1. ROS2 Autonomous Navigation

The robot uses:

* ROS2 Humble
* Nav2
* AMCL localization
* 2D Lidar 
* waypoint-based navigation

for autonomous movement and obstacle avoidance.

---

## 2. Embodied AI Reasoning

Gemini AI is used as a semantic reasoning layer.

The AI:

* interprets environmental situations,
* explains robot decisions,
* identifies navigation failures,
* and proposes recovery behaviors.

Example reasoning output:

```
Obstacle detected ahead.
Primary route blocked.
Searching for alternative safe route.
```

Important:
**Gemini AI does NOT directly control the robot motors.**

It only provides:

* reasoning,
* explanations,
* and high-level decision suggestions.

---

## 3. Safety Verification Layer

A safety supervisor layer is implemented between the AI and the robot navigation stack.

The purpose of this layer is to:

* enforce velocity limits,
* verify safe navigation behavior,
* reject unsafe actions,
* and maintain collision-free operation.

This prevents unsafe AI-generated behaviors from being executed directly on the physical robot.

---

## 4. Explainable Robot Display

The robot includes a display interface that shows:

* current navigation goals,
* robot state,
* AI reasoning,
* and recovery explanations.

This improves:

* transparency,
* predictability,
* and human trust.

Example:

```
Current Goal: Station B
Obstacle detected.
Alternative route selected.
Proceeding safely.
```

---

# Proposed Scenario

## Autonomous Hospital / Laboratory Delivery Assistant

The robot autonomously transports:

* medicine,
* lab samples,
* or medical tools

between predefined stations.

During navigation:

* people may block corridors,
* objects may obstruct pathways,
* or localization failures may occur.

The robot:

1. detects the issue,
2. reasons about the situation,
3. safely replans navigation,
4. explains the reasoning on the display,
5. and completes the mission safely.

---

# Research Contribution

This project contributes a framework that combines:

* embodied AI reasoning,
* verified autonomous navigation,
* and explainable human-robot interaction.

Unlike traditional AI-only systems, this project focuses on ensuring that AI-generated decisions are safely executable on a real mobile robotic platform.

---

# Hardware Used

* AMR Robot 
* Intel-based mini PC
* 2D lidar
* Display interface
* Intel depth camera d435i

---

# Software Stack

* Ubuntu 22.04
* ROS2 Humble
* Nav2
* AMCL
* RViz2
* Python
* Flask / Web UI
* Gemini API

---

# Current Development Status

## To Complete

* ROS2 AMR bringup
* Lidar integration - Done as of June 2 
* Nav2 autonomous navigation
* Waypoint navigation
* Recovery behavior testing
* Localization setup
* ROS2 communication framework
* Gemini reasoning integration
* Safety supervisor implementation
* Display interface
* Human trust evaluation experiments

---

# Expected Outcome

The final system will demonstrate:

* autonomous ROS2 navigation,
* AI-assisted reasoning,
* safe recovery behaviors,
* transparent robot explanations,
* and improved human-robot interaction.

---

# Author

Aravind Kalai

Final Year Project - SUTD
Robotics 
