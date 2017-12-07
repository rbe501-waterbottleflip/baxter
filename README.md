RBE 501 Semester project, trying to simulate the waterbottle flip using a Baxter robot in Gazebo

To run: 
 1. roslaunch bottleflip bottleflip.launch
 2. Once the robot is fully initialized (the Gravity Compensation has been turned off message is shown in the log), rosrun baxter_interface joint_trajectory_action_server.py
 3. To run the code rosrun bottleflip grip_test.py
