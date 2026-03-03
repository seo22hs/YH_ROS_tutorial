# ROS devlopment
    Ubuntu 20.04
    Ros noetic

# ROS install
1. souce list
```bash
$ sudo sh -c 'echo "deb http://packages.ros.org/ros/ubuntu $(lsb_release -sc) main" > /etc/apt/sources.list.d/ros-latest.list'
```

2. Set up keys
```bash
$ sudo apt install curl
$ curl -s https://raw.githubusercontent.com/ros/rosdistro/master/ros.asc | sudo apt-key add -
```

3. Installation
```bash
$ sudo apt update
$ sudo apt install ros-noetic-desktop-full
```

3-1. git install & SSH key
```bash
$ sudo apt install git -y
$ ssh-keygen -t ed25519 -C "lsc584727@gmail.com"
at /home/seohee/
$ cat /home/seohee/id_ed25519.pub
$ cat /home/seohee/.ssh/id_ed25519.pub
$ git --version
$ git config --global user.name "seo22hs"
$ git config --global user.email "lsc584727@gmail.com"
$ git config --list
```

4. Environment setup
```bash
#위치 : cd /opt/ros/noetic/

$ source /opt/ros/noetic/setup.bash

#Catkin
$ mkdir -p ~/catkin_ws/src
$ cd ~/catkin_ws/
$ catkin_make

$ source devel/setup.bash
$ echo $ROS_PACKAGE_PATH

$ echo "source ~/catkin_ws/devel/setup.bash" >> ~/.bashrc
$ source ~/.bashrc

#확인 : nano ~/.bashrc
```

# 과제 2 - /turtle1/pose 관찰

```bash
#준비
터미널1 : roscore
터미널2 : rosnode list 확인 후 > rosrun turtlesim turtlesim_node
터미널3 : rosrun turtlesim turtle_teleop_key
```

```bash
# /turtle1/pose 필드 분석
$ rostopic echo /turtle1/pose

- x: 거북이의 X 좌표. 우측으로 이동하면 값이 증가한다
- y: 거북이의 Y 좌표. 위로 이동하면 값이 증가한다
- theta: 거북이의 방향 (라디안). 좌회전하면 값이 증가, 우회전하면 감소한다
- linear_velocity: 현재 직진 속도. 방향키 위,아래 를 누르면 2.0이 된다.
- angular_velocity: 현재 회전 속도. 방향키 좌를 누르면 2.0이 된다, 아래를 누르면 -2.0이 된다.
```

# 과제 3 - 토픽/메시지 구조 정리

```bash
#1 . 토픽 목록 확인

$ rostopic list

/rosout
/rosout_agg
/turtle1/cmd_vel
/turtle1/color_sensor
/turtle1/pose
```

```bash
# 2. 토픽의 메시지 타입 확인

$ rostopic type /turtle1/cmd_vel

geometry_msgs/Twist
```

```bash
# 3. 토픽의 메시지 구조 확인

$ rosmsg show geometry_msgs/Twist

geometry_msgs/Vector3 linear
  float64 x
  float64 y
  float64 z
geometry_msgs/Vector3 angular
  float64 x
  float64 y
  float64 z
```

## turtlesim 토픽 정리


### 1. /turtle1/cmd_vel (geometry_msgs/Twist)

거북이에게 보내는 속도 명령

- linear.x: 직진 속도 (앞/뒤)

- linear.y: 좌/우 이동 (사용 안 함)

- linear.z: 상/하 이동 (사용 안 함)

- angular.x: Roll (사용 안 함)

- angular.y: Pitch (사용 안 함)

- angular.z: 회전 속도 (좌/우 회전)

### 2. /turtle1/pose (turtlesim/Pose)

거북이의 현재 위치와 방향

- x: X 좌표

- y: Y 좌표

- theta: 방향 (라디안)

- linear_velocity: 현재 직진 속도

- angular_velocity: 현재 회전 속도

### 3. /turtle1/color_sensor (turtlesim/Color)

거북이 발 아래의 배경 색상

- r: 빨강 (0~255)

- g: 초록 (0~255)

- b: 파랑 (0~255)
