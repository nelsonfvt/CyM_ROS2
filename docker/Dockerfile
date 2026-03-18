# Set the ROS distribution as an argument, defaulting to 'jazzy'
ARG ROS_DISTRO=jazzy

# ros2-desktop-full
FROM osrf/ros:${ROS_DISTRO}-desktop-full

# Set the maintainer information for this Dockerfile
LABEL maintainer="nelsonfvt<nelsonfvt@gmail.com>"
 
# Set environment variables
ENV PIP_BREAK_SYSTEM_PACKAGES=1
ENV DEBIAN_FRONTEND=noninteractive
 
# Set the default shell to bash for RUN commands
# This ensures all RUN commands use bash instead of sh
SHELL ["/bin/bash", "-c"]

# Update the system and install essential tools
# This step upgrades all packages and installs utilities needed for development
RUN apt-get update -q && \
    apt-get upgrade -yq && \
    apt-get install -yq apt-utils && \
    apt-get install -yq --no-install-recommends wget curl git build-essential \
    vim sudo lsb-release locales bash-completion tzdata gosu gedit htop nano libserial-dev
 
# Install additional tools required for ROS 2 development
# These packages help with building and managing ROS 2 workspaces
RUN apt-get update -q && \
    apt-get install -y gnupg2 iputils-ping usbutils \
    python3-argcomplete python3-colcon-common-extensions python3-networkx python3-pip python3-rosdep python3-vcstool

# Set up the ROS 2 environment
# This ensures that ROS 2 commands are available in the shell
# rosdep is a tool for installing system dependencies for ROS packages
RUN rosdep update && \
    grep -F "source /opt/ros/${ROS_DISTRO}/setup.bash" /root/.bashrc || echo "source /opt/ros/${ROS_DISTRO}/setup.bash" >> /root/.bashrc && \
    grep -F "source /usr/share/colcon_argcomplete/hook/colcon-argcomplete.bash" /root/.bashrc || echo "source /usr/share/colcon_argcomplete/hook/colcon-argcomplete.bash" >> /root/.bashrc
 
# Install additional ROS 2 packages
RUN apt-get update && \
    apt-get install -y \
    ros-${ROS_DISTRO}-joint-state-publisher-gui \
    ros-${ROS_DISTRO}-xacro \
    ros-${ROS_DISTRO}-demo-nodes-cpp \
    ros-${ROS_DISTRO}-demo-nodes-py \
    ros-${ROS_DISTRO}-rviz2 \
    ros-${ROS_DISTRO}-rqt-reconfigure

# Install ros2_controller and additional packages
RUN apt-get install -y \
    ros-${ROS_DISTRO}-controller-manager \
    ros-${ROS_DISTRO}-gz-ros2-control \
    ros-${ROS_DISTRO}-joint-trajectory-controller \
    ros-${ROS_DISTRO}-rqt-joint-trajectory-controller
 
# Install Mesa graphics drivers
# Mesa is an open-source implementation of OpenGL and other graphics APIs
# It's crucial for 3D rendering in many applications, including RViz in ROS
RUN apt-get update && \
    apt-get install -y software-properties-common && \
    DEBIAN_FRONTEND=noninteractive add-apt-repository ppa:kisak/kisak-mesa

# Create necessary directories
RUN mkdir -p /etc/udev/rules.d && \
    mkdir -p /root/ros2_ws/ROS2_basics && \
    mkdir -p /root/ros2_ws/ROS2_sim

# Copy configuration files from docker directory
# Note the docker/ prefix since we're in the parent context
COPY docker/workspace.sh /root/
COPY docker/entrypoint.sh /root/

# Make scripts executable
RUN chmod +x /root/workspace.sh /root/entrypoint.sh

# Run the workspace setup script
# This typically installs workspace dependencies and builds the ROS 2 packages
WORKDIR /root
RUN ./workspace.sh

# Set the entrypoint for the container
# This script will be run every time the container starts
ENTRYPOINT ["/root/entrypoint.sh"]

# Set the default command
# This keeps the container running indefinitely, allowing you to exec into it
CMD ["/bin/bash", "-c", "tail -f /dev/null"]