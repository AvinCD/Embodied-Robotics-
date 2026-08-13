# Safe and Explainable Embodied AI Navigation for Autonomous Mobile Robots

## Overview

This project presents a ROS 2-based Autonomous Mobile Robot framework that integrates reliable autonomous navigation with an advisory embodied AI reasoning layer and explainable human-robot interaction.

The system combines:

- Autonomous navigation using ROS 2 Nav2
- 2D LiDAR-based mapping and localisation
- Event-based visual reasoning using Gemini Robotics-ER / Gemini AI
- Voice explanation using offline text-to-speech
- Local dashboard for robot status and transparency
- Safety-aware system design where AI does not directly control robot motion

The objective of this project is to develop an AMR capable of navigating in indoor environments while clearly explaining its status, visual observations, and navigation-related events to users.

Unlike traditional autonomous robots that operate as black-box systems, this project focuses on explainable and safety-conscious robot behaviour.

---

## Project Motivation

Autonomous Mobile Robots are increasingly used in indoor environments such as hospitals, laboratories, smart buildings, warehouses, and service spaces.

Conventional AMRs can localise, plan, and avoid obstacles using maps, LiDAR, costmaps, and path planners. However, they usually do not explain their actions in a human-friendly way.

For example, a robot may stop because of a blocked path, localisation uncertainty, or planning failure, but the user may not know why.

Recent advances in embodied AI and Vision-Language Models allow robots to interpret visual scenes and generate meaningful explanations. However, directly connecting AI reasoning to robot motion creates safety risks.

This project addresses the gap by separating:

- Physical movement authority, handled by ROS 2 Nav2
- High-level visual reasoning, handled by Gemini AI
- Human-facing explanation, handled through dashboard and voice output

The main motivation is to improve human trust and transparency while keeping robot motion under deterministic local control.

---

## Project Objectives

The main objectives of this project are:

- Develop a stable ROS 2 autonomous navigation system
- Integrate 2D LiDAR for mapping, localisation, and obstacle sensing
- Use Nav2 for safe autonomous movement
- Use Gemini AI as an event-based visual reasoning layer
- Provide transparent robot explanations through voice and dashboard
- Keep AI advisory output separate from physical robot control
- Demonstrate a working proof-of-concept AMR system

---

## System Architecture

The system follows a layered architecture.

```
Human Interaction Layer
Voice output, dashboard, onboard display

Gemini AI Reasoning Layer
Event-based visual scene interpretation and advisory explanation

Mission / Status Management Layer
Tracks robot state, activity, and approved system events

Safety Boundary
Prevents AI from directly controlling robot motion

ROS 2 / Nav2 Execution Layer
Map server, AMCL, costmaps, planner, controller, recovery behaviours

Robot and Sensor Layer
AMR base, 2D LiDAR, depth camera, odometry, compute, speaker, display
