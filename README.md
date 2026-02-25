# Autonomous Patrol Robot using ROS2, Gazebo and RViz

## Overview

This project implements an Autonomous Patrol Robot using ROS2. The robot navigates through predefined waypoints in a simulated environment using Gazebo and visualizes its movement in RViz.

The system demonstrates waypoint-based navigation, autonomous movement logic, and logging of visited coordinates.

This project was developed as part of robotics training to understand practical ROS2 navigation workflows.

---

## Features

- Autonomous waypoint-based patrol
- Real-time robot simulation in Gazebo
- Visualization using RViz
- Coordinate logging of visited waypoints
- Structured ROS2 node implementation
- Launch file integration

---

## Technologies Used

- ROS2
- Gazebo
- RViz
- Python (rclpy)
- Linux environment

---

## System Architecture

1. Robot Model
   - Simulated mobile robot in Gazebo environment

2. Navigation Logic
   - Predefined waypoint coordinates
   - Robot sequentially navigates to each point
   - Continuous patrol loop

3. Logging
   - Coordinates of visited waypoints stored in log file
   - Timestamped movement tracking

---

## Waypoint Logic

Example visited coordinates:

(1.5, 0.0)
(1.5, 1.5)
(0.0, 1.5)
(0.0, 0.0)

The robot moves sequentially through each coordinate and repeats the cycle continuously.

---

## How to Run

1. Build the workspace:

colcon build

2. Source the workspace:

source install/setup.bash

3. Launch the patrol system:

ros2 launch patrol_launch.py

4. Open RViz (if not auto-launched):

rviz2

---

## Output

- Robot moves autonomously in Gazebo
- RViz shows robot state and movement
- Terminal logs visited coordinates
- Patrol loop continues indefinitely

---

## Demo

The repository includes:

- Demo video of Gazebo simulation
- RViz visualization screenshots
- Sample patrol log file

---

## Learning Outcomes

- Understanding ROS2 node structure
- Working with launch files
- Integrating Gazebo simulation
- Visualizing robot movement in RViz
- Implementing waypoint navigation logic
- Logging and debugging ROS2 systems

---

## Future Improvements

- Implement SLAM-based navigation
- Add obstacle avoidance using sensors
- Integrate Nav2 stack
- Add real robot hardware implementation
- Multi-robot patrol system

---

Raghav Sathe  
ENTC Engineering Undergraduate  
Robotics | Embedded Systems | ROS2  

This project demonstrates foundational understanding of ROS2 autonomous navigation and simulation workflows.
