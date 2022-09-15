%bcond_without tests
%bcond_without weak_deps

%global __os_install_post %(echo '%{__os_install_post}' | sed -e 's!/usr/lib[^[:space:]]*/brp-python-bytecompile[[:space:]].*$!!g')
%global __provides_exclude_from ^/opt/ros/galactic/.*$
%global __requires_exclude_from ^/opt/ros/galactic/.*$

Name:           ros-galactic-turtlebot4-diagnostics
Version:        0.1.3
Release:        1%{?dist}%{?release_suffix}
Summary:        ROS turtlebot4_diagnostics package

License:        Apache 2.0
Source0:        %{name}-%{version}.tar.gz

Requires:       ros-galactic-diagnostic-aggregator
Requires:       ros-galactic-diagnostic-msgs
Requires:       ros-galactic-diagnostic-updater
Requires:       ros-galactic-irobot-create-msgs
Requires:       ros-galactic-rclpy
Requires:       ros-galactic-sensor-msgs
Requires:       ros-galactic-ros-workspace
BuildRequires:  python%{python3_pkgversion}-devel
BuildRequires:  ros-galactic-diagnostic-aggregator
BuildRequires:  ros-galactic-diagnostic-msgs
BuildRequires:  ros-galactic-diagnostic-updater
BuildRequires:  ros-galactic-irobot-create-msgs
BuildRequires:  ros-galactic-rclpy
BuildRequires:  ros-galactic-ros-workspace
BuildRequires:  ros-galactic-sensor-msgs
Provides:       %{name}-devel = %{version}-%{release}
Provides:       %{name}-doc = %{version}-%{release}
Provides:       %{name}-runtime = %{version}-%{release}

%if 0%{?with_tests}
BuildRequires:  python%{python3_pkgversion}-pytest
BuildRequires:  ros-galactic-ament-copyright
BuildRequires:  ros-galactic-ament-flake8
BuildRequires:  ros-galactic-ament-pep257
%endif

%description
Turtlebot4 Diagnostics

%prep
%autosetup -p1

%build
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree and source it.  It will set things like
# CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/galactic/setup.sh" ]; then . "/opt/ros/galactic/setup.sh"; fi
%py3_build

%install
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree and source it.  It will set things like
# CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/galactic/setup.sh" ]; then . "/opt/ros/galactic/setup.sh"; fi
%py3_install -- --prefix "/opt/ros/galactic"

%if 0%{?with_tests}
%check
# Look for a directory with a name indicating that it contains tests
TEST_TARGET=$(ls -d * | grep -m1 "\(test\|tests\)" ||:)
if [ -n "$TEST_TARGET" ] && %__python3 -m pytest --version; then
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree and source it.  It will set things like
# CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/galactic/setup.sh" ]; then . "/opt/ros/galactic/setup.sh"; fi
%__python3 -m pytest $TEST_TARGET || echo "RPM TESTS FAILED"
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

