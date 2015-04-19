Name:           ros-hydro-ecto-opencv
Version:        0.5.5
Release:        1%{?dist}
Summary:        ROS ecto_opencv package

Group:          Development/Libraries
License:        BSD
URL:            http://plasmodic.github.io/ecto_opencv
Source0:        %{name}-%{version}.tar.gz

Requires:       boost-devel
Requires:       ros-hydro-ecto
Requires:       ros-hydro-opencv-candidate
BuildRequires:  boost-devel
BuildRequires:  ros-hydro-catkin
BuildRequires:  ros-hydro-ecto
BuildRequires:  ros-hydro-opencv-candidate

%description
Ecto bindings for common opencv functionality.

%prep
%setup -q

%build
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/hydro/setup.sh" ]; then . "/opt/ros/hydro/setup.sh"; fi
mkdir -p obj-%{_target_platform} && cd obj-%{_target_platform}
%cmake .. \
        -UINCLUDE_INSTALL_DIR \
        -ULIB_INSTALL_DIR \
        -USYSCONF_INSTALL_DIR \
        -USHARE_INSTALL_PREFIX \
        -ULIB_SUFFIX \
        -DCMAKE_INSTALL_PREFIX="/opt/ros/hydro" \
        -DCMAKE_PREFIX_PATH="/opt/ros/hydro" \
        -DSETUPTOOLS_DEB_LAYOUT=OFF \
        -DCATKIN_BUILD_BINARY_PACKAGE="1" \

make %{?_smp_mflags}

%install
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/hydro/setup.sh" ]; then . "/opt/ros/hydro/setup.sh"; fi
cd obj-%{_target_platform}
make %{?_smp_mflags} install DESTDIR=%{buildroot}

%files
/opt/ros/hydro

%changelog
* Sun Apr 19 2015 Vincent Rabaud <vincent.rabaud@gmail.com> - 0.5.5-1
- Autogenerated by Bloom

* Sun Mar 29 2015 Vincent Rabaud <vincent.rabaud@gmail.com> - 0.5.5-0
- Autogenerated by Bloom

