%bcond_without tests
%bcond_without weak_deps

%global __os_install_post %(echo '%{__os_install_post}' | sed -e 's!/usr/lib[^[:space:]]*/brp-python-bytecompile[[:space:]].*$!!g')
%global __provides_exclude_from ^/opt/ros/galactic/.*$
%global __requires_exclude_from ^/opt/ros/galactic/.*$

Name:           ros-galactic-turtlebot4-base
Version:        0.1.3
Release:        1%{?dist}%{?release_suffix}
Summary:        ROS turtlebot4_base package

License:        Apache 2.0
Source0:        %{name}-%{version}.tar.gz

Requires:       libgpiod-devel
Requires:       ros-galactic-irobot-create-msgs
Requires:       ros-galactic-rclcpp
Requires:       ros-galactic-rclcpp-action
Requires:       ros-galactic-rcutils
Requires:       ros-galactic-sensor-msgs
Requires:       ros-galactic-std-msgs
Requires:       ros-galactic-turtlebot4-msgs
Requires:       ros-galactic-turtlebot4-node
Requires:       ros-galactic-ros-workspace
BuildRequires:  libgpiod-devel
BuildRequires:  ros-galactic-ament-cmake
BuildRequires:  ros-galactic-irobot-create-msgs
BuildRequires:  ros-galactic-rclcpp
BuildRequires:  ros-galactic-rclcpp-action
BuildRequires:  ros-galactic-rcutils
BuildRequires:  ros-galactic-sensor-msgs
BuildRequires:  ros-galactic-std-msgs
BuildRequires:  ros-galactic-turtlebot4-msgs
BuildRequires:  ros-galactic-turtlebot4-node
BuildRequires:  ros-galactic-ros-workspace
Provides:       %{name}-devel = %{version}-%{release}
Provides:       %{name}-doc = %{version}-%{release}
Provides:       %{name}-runtime = %{version}-%{release}

%if 0%{?with_tests}
BuildRequires:  ros-galactic-ament-lint-auto
BuildRequires:  ros-galactic-ament-lint-common
%endif

%description
Turtlebot4 Base Node

%prep
%autosetup -p1

%build
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree and source it.  It will set things like
# CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/galactic/setup.sh" ]; then . "/opt/ros/galactic/setup.sh"; fi
mkdir -p .obj-%{_target_platform} && cd .obj-%{_target_platform}
%cmake3 \
    -UINCLUDE_INSTALL_DIR \
    -ULIB_INSTALL_DIR \
    -USYSCONF_INSTALL_DIR \
    -USHARE_INSTALL_PREFIX \
    -ULIB_SUFFIX \
    -DCMAKE_INSTALL_PREFIX="/opt/ros/galactic" \
    -DAMENT_PREFIX_PATH="/opt/ros/galactic" \
    -DCMAKE_PREFIX_PATH="/opt/ros/galactic" \
    -DSETUPTOOLS_DEB_LAYOUT=OFF \
%if !0%{?with_tests}
    -DBUILD_TESTING=OFF \
%endif
    ..

%make_build

%install
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree and source it.  It will set things like
# CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/galactic/setup.sh" ]; then . "/opt/ros/galactic/setup.sh"; fi
%make_install -C .obj-%{_target_platform}

%if 0%{?with_tests}
%check
# Look for a Makefile target with a name indicating that it runs tests
TEST_TARGET=$(%__make -qp -C .obj-%{_target_platform} | sed "s/^\(test\|check\):.*/\\1/;t f;d;:f;q0")
if [ -n "$TEST_TARGET" ]; then
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree and source it.  It will set things like
# CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/galactic/setup.sh" ]; then . "/opt/ros/galactic/setup.sh"; fi
CTEST_OUTPUT_ON_FAILURE=1 \
    %make_build -C .obj-%{_target_platform} $TEST_TARGET || echo "RPM TESTS FAILED"
else echo "RPM TESTS SKIPPED"; fi
%endif

%files
/opt/ros/galactic

%changelog
* Thu Sep 15 2022 rkreinin <rkreinin@clearpathrobotics.com> - 0.1.3-1
- Autogenerated by Bloom

* Mon May 30 2022 rkreinin <rkreinin@clearpathrobotics.com> - 0.1.2-1
- Autogenerated by Bloom

* Tue May 24 2022 rkreinin <rkreinin@clearpathrobotics.com> - 0.1.1-1
- Autogenerated by Bloom

* Tue May 24 2022 rkreinin <rkreinin@clearpathrobotics.com> - 0.1.0-1
- Autogenerated by Bloom

