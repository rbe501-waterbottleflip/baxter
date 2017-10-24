## *********************************************************
## 
## File autogenerated for the baxter_interface package 
## by the dynamic_reconfigure package.
## Please do not edit.
## 
## ********************************************************/

from dynamic_reconfigure.encoding import extract_params

inf = float('inf')

config_description = {'upper': 'DEFAULT', 'lower': 'groups', 'srcline': 246, 'name': 'Default', 'parent': 0, 'srcfile': '/opt/ros/indigo/lib/python2.7/dist-packages/dynamic_reconfigure/parameter_generator_catkin.py', 'cstate': 'true', 'parentname': 'Default', 'class': 'DEFAULT', 'field': 'default', 'state': True, 'parentclass': '', 'groups': [], 'parameters': [{'srcline': 293, 'description': 'left_gripper - Timeout (Seconds) to achieve command or determined gripping', 'max': 20.0, 'cconsttype': 'const double', 'ctype': 'double', 'srcfile': '/opt/ros/indigo/lib/python2.7/dist-packages/dynamic_reconfigure/parameter_generator_catkin.py', 'name': 'left_gripper_timeout', 'edit_method': '', 'default': 5.0, 'level': 0, 'min': -1.0, 'type': 'double'}, {'srcline': 293, 'description': 'left_gripper - Electric Gripper - Maximum final error', 'max': 100.0, 'cconsttype': 'const double', 'ctype': 'double', 'srcfile': '/opt/ros/indigo/lib/python2.7/dist-packages/dynamic_reconfigure/parameter_generator_catkin.py', 'name': 'left_gripper_goal', 'edit_method': '', 'default': 5.0, 'level': 0, 'min': 0.0, 'type': 'double'}, {'srcline': 293, 'description': 'left_gripper - Electric Gripper - Velocity', 'max': 100.0, 'cconsttype': 'const double', 'ctype': 'double', 'srcfile': '/opt/ros/indigo/lib/python2.7/dist-packages/dynamic_reconfigure/parameter_generator_catkin.py', 'name': 'left_gripper_velocity', 'edit_method': '', 'default': 50.0, 'level': 0, 'min': 0.0, 'type': 'double'}, {'srcline': 293, 'description': 'left_gripper - Electric Gripper - Force threshold. Grip achieved when surpassed.', 'max': 100.0, 'cconsttype': 'const double', 'ctype': 'double', 'srcfile': '/opt/ros/indigo/lib/python2.7/dist-packages/dynamic_reconfigure/parameter_generator_catkin.py', 'name': 'left_gripper_moving_force', 'edit_method': '', 'default': 40.0, 'level': 0, 'min': 0.0, 'type': 'double'}, {'srcline': 293, 'description': 'left_gripper - Electric Gripper - Holding force applied when gripping/after motion.', 'max': 100.0, 'cconsttype': 'const double', 'ctype': 'double', 'srcfile': '/opt/ros/indigo/lib/python2.7/dist-packages/dynamic_reconfigure/parameter_generator_catkin.py', 'name': 'left_gripper_holding_force', 'edit_method': '', 'default': 30.0, 'level': 0, 'min': 0.0, 'type': 'double'}, {'srcline': 293, 'description': 'left_gripper - Suction Gripper - Vacuum threshold. Grip achieved when surpassed.', 'max': 100.0, 'cconsttype': 'const double', 'ctype': 'double', 'srcfile': '/opt/ros/indigo/lib/python2.7/dist-packages/dynamic_reconfigure/parameter_generator_catkin.py', 'name': 'left_gripper_vacuum_threshold', 'edit_method': '', 'default': 18.0, 'level': 0, 'min': 0.0, 'type': 'double'}, {'srcline': 293, 'description': 'left_gripper - Suction Gripper - When suction ceased, seconds of blown air.', 'max': 100.0, 'cconsttype': 'const double', 'ctype': 'double', 'srcfile': '/opt/ros/indigo/lib/python2.7/dist-packages/dynamic_reconfigure/parameter_generator_catkin.py', 'name': 'left_gripper_blow_off', 'edit_method': '', 'default': 0.0, 'level': 0, 'min': 0.0, 'type': 'double'}, {'srcline': 293, 'description': 'right_gripper - Timeout (Seconds) to achieve command or determined gripping', 'max': 20.0, 'cconsttype': 'const double', 'ctype': 'double', 'srcfile': '/opt/ros/indigo/lib/python2.7/dist-packages/dynamic_reconfigure/parameter_generator_catkin.py', 'name': 'right_gripper_timeout', 'edit_method': '', 'default': 5.0, 'level': 0, 'min': -1.0, 'type': 'double'}, {'srcline': 293, 'description': 'right_gripper - Electric Gripper - Maximum final error', 'max': 100.0, 'cconsttype': 'const double', 'ctype': 'double', 'srcfile': '/opt/ros/indigo/lib/python2.7/dist-packages/dynamic_reconfigure/parameter_generator_catkin.py', 'name': 'right_gripper_goal', 'edit_method': '', 'default': 5.0, 'level': 0, 'min': 0.0, 'type': 'double'}, {'srcline': 293, 'description': 'right_gripper - Electric Gripper - Velocity', 'max': 100.0, 'cconsttype': 'const double', 'ctype': 'double', 'srcfile': '/opt/ros/indigo/lib/python2.7/dist-packages/dynamic_reconfigure/parameter_generator_catkin.py', 'name': 'right_gripper_velocity', 'edit_method': '', 'default': 50.0, 'level': 0, 'min': 0.0, 'type': 'double'}, {'srcline': 293, 'description': 'right_gripper - Electric Gripper - Force threshold. Grip achieved when surpassed.', 'max': 100.0, 'cconsttype': 'const double', 'ctype': 'double', 'srcfile': '/opt/ros/indigo/lib/python2.7/dist-packages/dynamic_reconfigure/parameter_generator_catkin.py', 'name': 'right_gripper_moving_force', 'edit_method': '', 'default': 40.0, 'level': 0, 'min': 0.0, 'type': 'double'}, {'srcline': 293, 'description': 'right_gripper - Electric Gripper - Holding force applied when gripping/after motion.', 'max': 100.0, 'cconsttype': 'const double', 'ctype': 'double', 'srcfile': '/opt/ros/indigo/lib/python2.7/dist-packages/dynamic_reconfigure/parameter_generator_catkin.py', 'name': 'right_gripper_holding_force', 'edit_method': '', 'default': 30.0, 'level': 0, 'min': 0.0, 'type': 'double'}, {'srcline': 293, 'description': 'right_gripper - Suction Gripper - Vacuum threshold. Grip achieved when surpassed.', 'max': 100.0, 'cconsttype': 'const double', 'ctype': 'double', 'srcfile': '/opt/ros/indigo/lib/python2.7/dist-packages/dynamic_reconfigure/parameter_generator_catkin.py', 'name': 'right_gripper_vacuum_threshold', 'edit_method': '', 'default': 18.0, 'level': 0, 'min': 0.0, 'type': 'double'}, {'srcline': 293, 'description': 'right_gripper - Suction Gripper - When suction ceased, seconds of blown air.', 'max': 100.0, 'cconsttype': 'const double', 'ctype': 'double', 'srcfile': '/opt/ros/indigo/lib/python2.7/dist-packages/dynamic_reconfigure/parameter_generator_catkin.py', 'name': 'right_gripper_blow_off', 'edit_method': '', 'default': 0.0, 'level': 0, 'min': 0.0, 'type': 'double'}], 'type': '', 'id': 0}

min = {}
max = {}
defaults = {}
level = {}
type = {}
all_level = 0

#def extract_params(config):
#    params = []
#    params.extend(config['parameters'])    
#    for group in config['groups']:
#        params.extend(extract_params(group))
#    return params

for param in extract_params(config_description):
    min[param['name']] = param['min']
    max[param['name']] = param['max']
    defaults[param['name']] = param['default']
    level[param['name']] = param['level']
    type[param['name']] = param['type']
    all_level = all_level | param['level']

