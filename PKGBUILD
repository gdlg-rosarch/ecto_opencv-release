# Script generated with Bloom
pkgdesc="ROS - Ecto bindings for common opencv functionality."
url='http://plasmodic.github.io/ecto_opencv'

pkgname='ros-kinetic-ecto-opencv'
pkgver='0.7.2_1'
pkgrel=1
arch=('any')
license=('BSD'
)

makedepends=('boost'
'ros-kinetic-catkin'
'ros-kinetic-ecto'
'ros-kinetic-opencv-candidate'
'ros-kinetic-rosunit'
)

depends=('boost'
'ros-kinetic-ecto'
'ros-kinetic-opencv-candidate'
)

conflicts=()
replaces=()

_dir=ecto_opencv
source=()
md5sums=()

prepare() {
    cp -R $startdir/ecto_opencv $srcdir/ecto_opencv
}

build() {
  # Use ROS environment variables
  source /usr/share/ros-build-tools/clear-ros-env.sh
  [ -f /opt/ros/kinetic/setup.bash ] && source /opt/ros/kinetic/setup.bash

  # Create build directory
  [ -d ${srcdir}/build ] || mkdir ${srcdir}/build
  cd ${srcdir}/build

  # Fix Python2/Python3 conflicts
  /usr/share/ros-build-tools/fix-python-scripts.sh -v 2 ${srcdir}/${_dir}

  # Build project
  cmake ${srcdir}/${_dir} \
        -DCMAKE_BUILD_TYPE=Release \
        -DCATKIN_BUILD_BINARY_PACKAGE=ON \
        -DCMAKE_INSTALL_PREFIX=/opt/ros/kinetic \
        -DPYTHON_EXECUTABLE=/usr/bin/python2 \
        -DPYTHON_INCLUDE_DIR=/usr/include/python2.7 \
        -DPYTHON_LIBRARY=/usr/lib/libpython2.7.so \
        -DPYTHON_BASENAME=-python2.7 \
        -DSETUPTOOLS_DEB_LAYOUT=OFF
  make
}

package() {
  cd "${srcdir}/build"
  make DESTDIR="${pkgdir}/" install
}

