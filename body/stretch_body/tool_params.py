
#originally from toolshare
RE2V0_DW2_stretch_gripper={
        'range_pad_t': [100.0, -100.0],
        'flip_encoder_polarity': 0,
        'gr': 1.0,
        'id': 14,
        'max_voltage_limit': 15,
        'min_grip_strength': -125,
        'min_voltage_limit': 11,
        'gripper_conversion':'stretch_gripper_3_conversion',
        'motion':{
            'trajectory_vel_ctrl':1,
            'trajectory_vel_ctrl_kP':1.5,
            'default':{
              'accel': 10.0,
              'vel': 6.0},
            'fast':{
              'accel': 10.0,
              'vel': 8.0},
            'max':{
              'accel': 20,
              'vel': 20},
            'slow':{
              'accel': 4.0,
              'vel': 3.0},
            'trajectory_max': {
                'vel_r': 50.0,
                'accel_r': 100.0},
            'vel_brakezone_factor': 1},
        'set_safe_velocity': 1,
        'pid': [640.0,0,0],
        'pwm_homing': [-400, 0],
        'pwm_limit': 885,
        'req_calibration': 1,
        'return_delay_time': 0,
        'stall_backoff': 2.0,
        'stall_max_effort': 20.0,
        'stall_max_time': 0.5,
        'stall_min_vel': 0.1,
        'temperature_limit': 72,
        'usb_name': '/dev/hello-dynamixel-wrist',
        'use_multiturn': 1,
        'use_pos_current_ctrl':0,
        'retry_on_comm_failure': 1,
        'baud': 115200,
        'enable_runstop': 1,
        'disable_torque_on_stop': 1}

RE1V0_DW2_stretch_gripper = RE2V0_DW2_stretch_gripper

stretch_gripper_3_conversion={'finger_length_m':0.171,
                                      'open_aperture_m':0.09,
                                      'closed_aperture_m':0.0,
                                      'open_robotis':70.0,
                                      'closed_robotis':0.0}

RE2V0_wrist_yaw ={
    'flip_encoder_polarity': 1,
    'gr': 2.4,
    'id': 13,
    'max_voltage_limit': 15,
    'min_voltage_limit': 11,
    'motion': {
        'trajectory_vel_ctrl': 1,
        'trajectory_vel_ctrl_kP': 1.5,
        'default': {
            'accel': 3.0,
            'vel': 2.0},
        'fast': {
            'accel': 5.0,
            'vel': 2.5},
        'max': {
            'accel': 10,
            'vel': 6.0},
        'slow': {
            'accel': 1.5,
            'vel': 0.75},
        'trajectory_max': {
            'vel_r': 3.0,
            'accel_r': 3.0},
        'vel_brakezone_factor': 0.2},
    'set_safe_velocity': 1,
    'pid': [640, 0, 0],
    'pwm_homing': [-300, 300],
    'pwm_limit': 885,
    'req_calibration': 1,
    'return_delay_time': 0,
    'stall_backoff': 0.017,
    'stall_max_effort': 20.0,
    'stall_max_time': 1.0,
    'stall_min_vel': 0.1,
    'temperature_limit': 72,
    'usb_name': '/dev/hello-dynamixel-wrist',
    'use_multiturn': 1,
    'use_pos_current_ctrl': 0,
    'retry_on_comm_failure': 1,
    'baud': 115200,
    'enable_runstop': 1,
    'disable_torque_on_stop': 1,
    'range_pad_t': [100.0, -100.0]}

# originally from toolshare
RE2V0_DW2_wrist_pitch ={
    'flip_encoder_polarity': 1,
    'enable_runstop': 1,
    'gr': 1.0,
    'id': 15,
    'max_voltage_limit': 15,
    'min_voltage_limit': 11,
    'motion': {
        'trajectory_vel_ctrl': 1,
        'trajectory_vel_ctrl_kP': 1.5,
        'default': {'accel': 6.0, 'vel': 2.0},
        'fast': {'accel': 8.0, 'vel': 2.0},
        'max': {'accel': 10.0, 'vel': 3.0},
        'slow': {'accel': 4.0, 'vel': 1.0},
        'trajectory_max': {'accel_r': 16.0, 'vel_r': 8.0},
        'vel_brakezone_factor': 1},
    'set_safe_velocity': 1,
    'pid': [400, 0, 200],
    'pwm_homing': [0, 0],
    'pwm_limit': 885,
    'range_t': [730, 2048],
    'req_calibration': 0,
    'return_delay_time': 0,
    'stall_backoff': 0.017,
    'stall_max_effort': 10.0,
    'stall_max_time': 1.0,
    'stall_min_vel': 0.1,
    'temperature_limit': 72,
    'usb_name': '/dev/hello-dynamixel-wrist',
    'use_multiturn': 0,
    'use_pos_current_ctrl': 1,
    'zero_t': 1024,
    'baud': 115200,
    'retry_on_comm_failure': 1,
    'disable_torque_on_stop': 0,
    'float_on_stop': 1,
    'current_float_A': -0.13,
    'current_limit_A': 2.5
}

# originally from toolshare
RE2V0_DW2_wrist_roll = {
    'flip_encoder_polarity': 0,
    'enable_runstop': 1,
    'gr': 1.0,
    'id': 16,
    'max_voltage_limit': 16,
    'min_voltage_limit': 9,
    'motion': {
        'trajectory_vel_ctrl': 1,
        'trajectory_vel_ctrl_kP': 1.5,
        'default': {'accel': 8.0, 'vel': 2.0},
        'fast': {'accel': 10.0, 'vel': 3.0},
        'max': {'accel': 12, 'vel': 4.5},
        'slow': {'accel': 4.0, 'vel': 1.0},
        'trajectory_max': {'accel_r': 16.0, 'vel_r': 8.0},
        'vel_brakezone_factor': 1},
    'set_safe_velocity': 1,
    'pid': [800, 0, 0],
    'pwm_homing': [0, 0],
    'pwm_limit': 885,
    'range_t': [150, 3950],
    'req_calibration': 0,
    'return_delay_time': 0,
    'stall_backoff': 0.017,
    'stall_max_effort': 10.0,
    'stall_max_time': 1.0,
    'stall_min_vel': 0.1,
    'temperature_limit': 80,
    'usb_name': '/dev/hello-dynamixel-wrist',
    'use_multiturn': 0,
    'use_pos_current_ctrl': 0,
    'zero_t': 2048,
    'baud': 115200,
    'retry_on_comm_failure': 1,
    'disable_torque_on_stop': 0,
    'float_on_stop': 1,
    'current_float_A': 0.04,
    'current_limit_A': 1.0
}

SE3_eoa_wrist_dw3_tool_sg3={
        'py_class_name': 'EOA_Wrist_DW3_Tool_SG3',
        'py_module_name': 'stretch_body.end_of_arm_tools',
        'use_group_sync_read': 1,
        'retry_on_comm_failure': 1,
        'baud': 115200,
        'dxl_latency_timer': 64,
        'stow': {
            'arm': 0.0,
            'lift': 0.3,
            'wrist_pitch': -0.52,
            'wrist_roll': 0.0,
            'wrist_yaw': 3.0,
            'stretch_gripper':0.0
        },
        'collision_mgmt': {
            'k_brake_distance': {'wrist_pitch': 0.25, 'wrist_yaw': 0.25, 'wrist_roll': 0.25, 'stretch_gripper': 0.0},
            'collision_pairs': {
                'link_wrist_pitch_TO_base_link': {'link_pts': 'link_wrist_pitch', 'link_cube': 'base_link','detect_as': 'pts'},
                'link_wrist_yaw_bottom_TO_base_link': {'link_pts': 'link_wrist_yaw_bottom', 'link_cube': 'base_link','detect_as': 'pts'},
                'link_gripper_finger_left_TO_base_link': {'link_pts': 'link_gripper_finger_left','link_cube': 'base_link', 'detect_as': 'pts'},
                'link_gripper_finger_right_TO_base_link': {'link_pts': 'link_gripper_finger_right','link_cube': 'base_link', 'detect_as': 'pts'},
                'link_gripper_fingertip_left_TO_base_link': {'link_pts': 'link_gripper_fingertip_left','link_cube': 'base_link', 'detect_as': 'pts'},
                'link_gripper_fingertip_right_TO_base_link': {'link_pts': 'link_gripper_fingertip_right','link_cube': 'base_link', 'detect_as': 'pts'},
                'link_gripper_s3_body_TO_link_arm_l0': {'link_pts': 'link_gripper_s3_body', 'link_cube': 'link_arm_l0','detect_as': 'pts'},
                'link_gripper_s3_body_TO_link_arm_l1': {'link_pts': 'link_gripper_s3_body', 'link_cube': 'link_arm_l1','detect_as': 'pts'}},
            'joints': {'lift': [{'motion_dir': 'neg', 'collision_pair': 'link_wrist_pitch_TO_base_link'},
                                {'motion_dir': 'neg', 'collision_pair': 'link_wrist_yaw_bottom_TO_base_link'},
                                {'motion_dir': 'neg', 'collision_pair': 'link_gripper_finger_left_TO_base_link'},
                                {'motion_dir': 'neg', 'collision_pair': 'link_gripper_finger_right_TO_base_link'},
                                {'motion_dir': 'neg', 'collision_pair': 'link_gripper_fingertip_left_TO_base_link'},
                                {'motion_dir': 'neg', 'collision_pair': 'link_gripper_fingertip_right_TO_base_link'}],
                       'wrist_pitch': [{'motion_dir': 'neg', 'collision_pair': 'link_gripper_finger_left_TO_base_link'},
                                       {'motion_dir': 'neg','collision_pair': 'link_gripper_finger_right_TO_base_link'},
                                       {'motion_dir': 'neg','collision_pair': 'link_gripper_fingertip_left_TO_base_link'},
                                       {'motion_dir': 'neg','collision_pair': 'link_gripper_fingertip_right_TO_base_link'},
                                       {'motion_dir': 'pos', 'collision_pair': 'link_gripper_s3_body_TO_link_arm_l0'},
                                       {'motion_dir': 'pos', 'collision_pair': 'link_gripper_s3_body_TO_link_arm_l1'}],
                       'wrist_roll': [{'motion_dir': 'neg', 'collision_pair': 'link_gripper_s3_body_TO_link_arm_l1'},
                                      {'motion_dir': 'pos', 'collision_pair': 'link_gripper_s3_body_TO_link_arm_l0'}],
                       'wrist_yaw': [{'motion_dir': 'neg', 'collision_pair': 'link_gripper_s3_body_TO_link_arm_l0'},
                                     {'motion_dir': 'pos', 'collision_pair': 'link_gripper_s3_body_TO_link_arm_l1'}]}},

        'devices': {
            'wrist_pitch': {
                'py_class_name': 'WristPitch',
                'py_module_name': 'stretch_body.wrist_pitch'
            },
            'wrist_roll': {
                'py_class_name': 'WristRoll',
                'py_module_name': 'stretch_body.wrist_roll'
            },
            'wrist_yaw': {
                'py_class_name': 'WristYaw',
                'py_module_name': 'stretch_body.wrist_yaw'
            },
            'stretch_gripper': {
                'py_class_name': 'StretchGripper3',
                'py_module_name': 'stretch_body.stretch_gripper',
            }
    }}

RE2V0_tool_stretch_gripper={
    'use_group_sync_read': 1,
    'retry_on_comm_failure': 1,
    'baud': 115200,
    'dxl_latency_timer': 64,
    'py_class_name': 'ToolStretchGripper',
    'py_module_name': 'stretch_body.end_of_arm_tools',
    'stow': {'stretch_gripper': 0, 'wrist_yaw': 3.4},
    'devices': {
        'stretch_gripper': {
            'py_class_name': 'StretchGripper',
            'py_module_name': 'stretch_body.stretch_gripper'
        },
        'wrist_yaw': {
            'py_class_name': 'WristYaw',
            'py_module_name': 'stretch_body.wrist_yaw'
        }
    }}

SE3_eoa_wrist_dw3_tool_nil={
    'py_class_name': 'EOA_Wrist_DW3_Tool_NIL',
    'py_module_name': 'stretch_body.end_of_arm_tools',
    'use_group_sync_read': 1,
    'retry_on_comm_failure': 1,
    'baud': 115200,
    'dxl_latency_timer': 64,
    'wrist': 'eoaw_dw3',
    'tool': 'eoat_nil',
    'stow': {
        'arm': 0.0,
        'lift': 0.3,
        'wrist_pitch': -0.52,
        'wrist_roll': 0.0,
        'wrist_yaw': 3.0
    },
    'collision_mgmt': {
        'k_brake_distance': {'wrist_pitch': 0.0, 'wrist_yaw': 0.0, 'wrist_roll': 0.0},
        'joints': {
            'lift': [{'motion_dir': 'neg', 'link_pts': 'link_wrist_pitch', 'link_cube': 'base_link'},
                     {'motion_dir': 'neg', 'link_pts': 'link_wrist_roll', 'link_cube': 'base_link'}, ]}},

    'devices': {
        'wrist_pitch': {
            'py_class_name': 'WristPitch3',
            'py_module_name': 'stretch_body.wrist_pitch'
        },
        'wrist_roll': {
            'py_class_name': 'WristRoll3',
            'py_module_name': 'stretch_body.wrist_roll'
        },
        'wrist_yaw': {
            'py_class_name': 'WristYaw3',
            'py_module_name': 'stretch_body.wrist_yaw'
        }}}

DEFN_RE2V0_eoa_wrist_dw3_tool_sg3={
    'eoa_wrist_dw3_tool_sg3':SE3_eoa_wrist_dw3_tool_sg3,
    'stretch_gripper': SE3_stretch_gripper,
    'wrist_yaw': RE2V0_wrist_yaw,
    'wrist_pitch':DW2_wrist_pitch,
    'wrist_roll': DW2_wrist_roll,
    'stretch_gripper_conversion':stretch_gripper_3_conversion}

DEFN_RE2V0_tool_dex_wrist={
    'tool_stretch_dex_wrist':RE2V0_tool_stretch_dex_wrist,
    'stretch_gripper': DW2_stretch_gripper,
    'wrist_yaw': RE2V0_wrist_yaw,
    'wrist_pitch':DW2_wrist_pitch,
    'wrist_roll': DW2_wrist_roll,
    'stretch_gripper_conversion':stretch_gripper_2_conversion}