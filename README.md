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
