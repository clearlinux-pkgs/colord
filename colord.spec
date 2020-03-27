#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
# Source0 file verified with key 0x17ACBA8DFA970E17 (richard@hughsie.com)
#
Name     : colord
Version  : 1.4.4
Release  : 22
URL      : https://www.freedesktop.org/software/colord/releases/colord-1.4.4.tar.xz
Source0  : https://www.freedesktop.org/software/colord/releases/colord-1.4.4.tar.xz
Source99 : https://www.freedesktop.org/software/colord/releases/colord-1.4.4.tar.xz.asc
Summary  : System daemon for managing color devices
Group    : Development/Tools
License  : GPL-2.0
Requires: colord-bin = %{version}-%{release}
Requires: colord-config = %{version}-%{release}
Requires: colord-data = %{version}-%{release}
Requires: colord-lib = %{version}-%{release}
Requires: colord-libexec = %{version}-%{release}
Requires: colord-license = %{version}-%{release}
Requires: colord-locales = %{version}-%{release}
Requires: colord-services = %{version}-%{release}
BuildRequires : buildreq-meson
BuildRequires : docbook-xml
BuildRequires : gobject-introspection
BuildRequires : gobject-introspection-dev
BuildRequires : gtk-doc
BuildRequires : intltool-dev
BuildRequires : libgudev-dev
BuildRequires : libxslt
BuildRequires : pkgconfig(bash-completion)
BuildRequires : pkgconfig(gusb)
BuildRequires : pkgconfig(lcms2)
BuildRequires : pkgconfig(polkit-gobject-1)
BuildRequires : pkgconfig(sqlite3)
BuildRequires : pkgconfig(udev)
BuildRequires : pkgconfig(valgrind)
BuildRequires : vala
BuildRequires : valgrind

%description
colord sensor driver for the hueyCOLOR
======================================
The hueyCOLOR is a *color sensor* found in the top-end P70 and P71 ThinkPads
from Lenovo. It is branded as a Pantone X-Rite sensor, and is similar in
protocol to the Huey and HueyPRO devices. The sensor is located in the palm-rest,
and so the laptop lid needs to be shut (and the display kept on) when showing
calibration patches.

%package bin
Summary: bin components for the colord package.
Group: Binaries
Requires: colord-data = %{version}-%{release}
Requires: colord-libexec = %{version}-%{release}
Requires: colord-config = %{version}-%{release}
Requires: colord-license = %{version}-%{release}
Requires: colord-services = %{version}-%{release}

%description bin
bin components for the colord package.


%package config
Summary: config components for the colord package.
Group: Default

%description config
config components for the colord package.


%package data
Summary: data components for the colord package.
Group: Data

%description data
data components for the colord package.


%package dev
Summary: dev components for the colord package.
Group: Development
Requires: colord-lib = %{version}-%{release}
Requires: colord-bin = %{version}-%{release}
Requires: colord-data = %{version}-%{release}
Provides: colord-devel = %{version}-%{release}
Requires: colord = %{version}-%{release}

%description dev
dev components for the colord package.


%package doc
Summary: doc components for the colord package.
Group: Documentation

%description doc
doc components for the colord package.


%package lib
Summary: lib components for the colord package.
Group: Libraries
Requires: colord-data = %{version}-%{release}
Requires: colord-libexec = %{version}-%{release}
Requires: colord-license = %{version}-%{release}

%description lib
lib components for the colord package.


%package libexec
Summary: libexec components for the colord package.
Group: Default
Requires: colord-config = %{version}-%{release}
Requires: colord-license = %{version}-%{release}

%description libexec
libexec components for the colord package.


%package license
Summary: license components for the colord package.
Group: Default

%description license
license components for the colord package.


%package locales
Summary: locales components for the colord package.
Group: Default

%description locales
locales components for the colord package.


%package services
Summary: services components for the colord package.
Group: Systemd services

%description services
services components for the colord package.


%prep
%setup -q -n colord-1.4.4

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1557082358
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export FCFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export FFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=4 "
CFLAGS="$CFLAGS" CXXFLAGS="$CXXFLAGS" LDFLAGS="$LDFLAGS" meson --prefix /usr --buildtype=plain --localstatedir=/var --sharedstatedir=/var/lib -Denable-argyllcms-sensor=false -Dwith-daemon-user=colord -Denable-docs=false -Denable-man=false -Dargyllcms_sensor=false -Dman=false -Dvapi=true  builddir
ninja -v -C builddir

%install
mkdir -p %{buildroot}/usr/share/package-licenses/colord
cp COPYING %{buildroot}/usr/share/package-licenses/colord/COPYING
DESTDIR=%{buildroot} ninja -C builddir install
%find_lang colord

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/cd-create-profile
/usr/bin/cd-fix-profile
/usr/bin/cd-iccdump
/usr/bin/cd-it8
/usr/bin/colormgr

%files config
%defattr(-,root,root,-)
/usr/lib/tmpfiles.d/colord.conf
/usr/lib/udev/rules.d/69-cd-sensors.rules
/usr/lib/udev/rules.d/95-cd-devices.rules

%files data
%defattr(-,root,root,-)
/usr/lib64/girepository-1.0/Colord-1.0.typelib
/usr/lib64/girepository-1.0/Colorhug-1.0.typelib
/usr/share/bash-completion/completions/colormgr
/usr/share/color/icc/colord/AdobeRGB1998.icc
/usr/share/color/icc/colord/AppleRGB.icc
/usr/share/color/icc/colord/BestRGB.icc
/usr/share/color/icc/colord/BetaRGB.icc
/usr/share/color/icc/colord/Bluish.icc
/usr/share/color/icc/colord/BruceRGB.icc
/usr/share/color/icc/colord/CIE-RGB.icc
/usr/share/color/icc/colord/ColorMatchRGB.icc
/usr/share/color/icc/colord/Crayons.icc
/usr/share/color/icc/colord/DonRGB4.icc
/usr/share/color/icc/colord/ECI-RGBv1.icc
/usr/share/color/icc/colord/ECI-RGBv2.icc
/usr/share/color/icc/colord/EktaSpacePS5.icc
/usr/share/color/icc/colord/Gamma5000K.icc
/usr/share/color/icc/colord/Gamma5500K.icc
/usr/share/color/icc/colord/Gamma6500K.icc
/usr/share/color/icc/colord/NTSC-RGB.icc
/usr/share/color/icc/colord/PAL-RGB.icc
/usr/share/color/icc/colord/ProPhotoRGB.icc
/usr/share/color/icc/colord/Rec709.icc
/usr/share/color/icc/colord/SMPTE-C-RGB.icc
/usr/share/color/icc/colord/SwappedRedAndGreen.icc
/usr/share/color/icc/colord/WideGamutRGB.icc
/usr/share/color/icc/colord/sRGB.icc
/usr/share/color/icc/colord/x11-colors.icc
/usr/share/colord/cmf/CIE1931-2deg-XYZ.cmf
/usr/share/colord/cmf/CIE1964-10deg-XYZ.cmf
/usr/share/colord/icons/color-munki-photo-ambient.svg
/usr/share/colord/icons/color-munki-photo-attach.svg
/usr/share/colord/icons/color-munki-photo-calibrate.svg
/usr/share/colord/icons/color-munki-photo-projector.svg
/usr/share/colord/icons/color-munki-photo-screen.svg
/usr/share/colord/icons/color-munki-smile-attach.svg
/usr/share/colord/icons/colorhug-attach.svg
/usr/share/colord/icons/colorhug2-attach.svg
/usr/share/colord/icons/dtp94-attach.svg
/usr/share/colord/icons/hcfr-attach.svg
/usr/share/colord/icons/huey-attach.svg
/usr/share/colord/icons/i1-display3-attach.svg
/usr/share/colord/icons/i1-monitor-attach.svg
/usr/share/colord/icons/i1-pro-attach.svg
/usr/share/colord/icons/spyder2-attach.svg
/usr/share/colord/icons/spyder3-attach.svg
/usr/share/colord/icons/spyder4-attach.svg
/usr/share/colord/icons/spyder5-attach.svg
/usr/share/colord/illuminant/CIE-A.sp
/usr/share/colord/illuminant/CIE-B.sp
/usr/share/colord/illuminant/CIE-C.sp
/usr/share/colord/illuminant/CIE-D50.sp
/usr/share/colord/illuminant/CIE-D55.sp
/usr/share/colord/illuminant/CIE-D65.sp
/usr/share/colord/illuminant/CIE-D93.sp
/usr/share/colord/illuminant/CIE-E.sp
/usr/share/colord/illuminant/CIE-F1.sp
/usr/share/colord/illuminant/CIE-F10.sp
/usr/share/colord/illuminant/CIE-F11.sp
/usr/share/colord/illuminant/CIE-F12.sp
/usr/share/colord/illuminant/CIE-F2.sp
/usr/share/colord/illuminant/CIE-F3.sp
/usr/share/colord/illuminant/CIE-F4.sp
/usr/share/colord/illuminant/CIE-F5.sp
/usr/share/colord/illuminant/CIE-F6.sp
/usr/share/colord/illuminant/CIE-F7.sp
/usr/share/colord/illuminant/CIE-F8.sp
/usr/share/colord/illuminant/CIE-F9.sp
/usr/share/colord/ref/CIE-1986-daylight-SPD.cmf
/usr/share/colord/ref/CIE-TCS.sp
/usr/share/colord/ti1/display-long.ti1
/usr/share/colord/ti1/display-normal.ti1
/usr/share/colord/ti1/display-short.ti1
/usr/share/colord/ti1/printer-long.ti1
/usr/share/colord/ti1/printer-normal.ti1
/usr/share/colord/ti1/printer-short.ti1
/usr/share/dbus-1/interfaces/org.freedesktop.ColorHelper.xml
/usr/share/dbus-1/interfaces/org.freedesktop.ColorManager.Device.xml
/usr/share/dbus-1/interfaces/org.freedesktop.ColorManager.Profile.xml
/usr/share/dbus-1/interfaces/org.freedesktop.ColorManager.Sensor.xml
/usr/share/dbus-1/interfaces/org.freedesktop.ColorManager.xml
/usr/share/dbus-1/services/org.freedesktop.ColorHelper.service
/usr/share/dbus-1/system-services/org.freedesktop.ColorManager.service
/usr/share/dbus-1/system.d/org.freedesktop.ColorManager.conf
/usr/share/gir-1.0/*.gir
/usr/share/glib-2.0/schemas/org.freedesktop.ColorHelper.gschema.xml
/usr/share/polkit-1/actions/org.freedesktop.color.policy
/usr/share/vala/vapi/colord.deps
/usr/share/vala/vapi/colord.vapi

%files dev
%defattr(-,root,root,-)
/usr/include/colord-1/colord-private.h
/usr/include/colord-1/colord-session/cd-session.h
/usr/include/colord-1/colord.h
/usr/include/colord-1/colord/cd-buffer.h
/usr/include/colord-1/colord/cd-client-sync.h
/usr/include/colord-1/colord/cd-client.h
/usr/include/colord-1/colord/cd-color.h
/usr/include/colord-1/colord/cd-device-sync.h
/usr/include/colord-1/colord/cd-device.h
/usr/include/colord-1/colord/cd-dom.h
/usr/include/colord-1/colord/cd-edid.h
/usr/include/colord-1/colord/cd-enum.h
/usr/include/colord-1/colord/cd-icc-store.h
/usr/include/colord-1/colord/cd-icc-utils.h
/usr/include/colord-1/colord/cd-icc.h
/usr/include/colord-1/colord/cd-interp-akima.h
/usr/include/colord-1/colord/cd-interp-linear.h
/usr/include/colord-1/colord/cd-interp.h
/usr/include/colord-1/colord/cd-it8-utils.h
/usr/include/colord-1/colord/cd-it8.h
/usr/include/colord-1/colord/cd-math.h
/usr/include/colord-1/colord/cd-profile-sync.h
/usr/include/colord-1/colord/cd-profile.h
/usr/include/colord-1/colord/cd-quirk.h
/usr/include/colord-1/colord/cd-sensor-sync.h
/usr/include/colord-1/colord/cd-sensor.h
/usr/include/colord-1/colord/cd-spectrum.h
/usr/include/colord-1/colord/cd-transform.h
/usr/include/colord-1/colord/cd-version.h
/usr/include/colord-1/colorhug/ch-common.h
/usr/include/colord-1/colorhug/ch-device-queue.h
/usr/include/colord-1/colorhug/ch-device.h
/usr/include/colord-1/colorhug/ch-hash.h
/usr/include/colord-1/colorhug/ch-inhx32.h
/usr/include/colord-1/colorhug/ch-math.h
/usr/include/colord-1/colorhug/ch-version.h
/usr/include/colord-1/colorhug/colorhug.h
/usr/lib64/libcolord.so
/usr/lib64/libcolordprivate.so
/usr/lib64/libcolorhug.so
/usr/lib64/pkgconfig/colord.pc
/usr/lib64/pkgconfig/colorhug.pc

%files doc
%defattr(0644,root,root,0755)
/usr/share/gtk-doc/html/colord/colord-CdClient.html
/usr/share/gtk-doc/html/colord/colord-CdDevice.html
/usr/share/gtk-doc/html/colord/colord-CdDom.html
/usr/share/gtk-doc/html/colord/colord-CdEdid.html
/usr/share/gtk-doc/html/colord/colord-CdIcc.html
/usr/share/gtk-doc/html/colord/colord-CdIccStore.html
/usr/share/gtk-doc/html/colord/colord-CdInterp.html
/usr/share/gtk-doc/html/colord/colord-CdInterpAkima.html
/usr/share/gtk-doc/html/colord/colord-CdInterpLinear.html
/usr/share/gtk-doc/html/colord/colord-CdIt8.html
/usr/share/gtk-doc/html/colord/colord-CdProfile.html
/usr/share/gtk-doc/html/colord/colord-CdSensor.html
/usr/share/gtk-doc/html/colord/colord-CdTransform.html
/usr/share/gtk-doc/html/colord/colord-cd-client-sync.html
/usr/share/gtk-doc/html/colord/colord-cd-color.html
/usr/share/gtk-doc/html/colord/colord-cd-device-sync.html
/usr/share/gtk-doc/html/colord/colord-cd-icc-utils.html
/usr/share/gtk-doc/html/colord/colord-cd-it8-utils.html
/usr/share/gtk-doc/html/colord/colord-cd-math.html
/usr/share/gtk-doc/html/colord/colord-cd-profile-sync.html
/usr/share/gtk-doc/html/colord/colord-cd-sensor-sync.html
/usr/share/gtk-doc/html/colord/colord-cd-spectrum.html
/usr/share/gtk-doc/html/colord/colord-cd-version.html
/usr/share/gtk-doc/html/colord/colord.devhelp2
/usr/share/gtk-doc/html/colord/home.png
/usr/share/gtk-doc/html/colord/index.html
/usr/share/gtk-doc/html/colord/ix01.html
/usr/share/gtk-doc/html/colord/left-insensitive.png
/usr/share/gtk-doc/html/colord/left.png
/usr/share/gtk-doc/html/colord/libcolord.html
/usr/share/gtk-doc/html/colord/libcolordprivate.html
/usr/share/gtk-doc/html/colord/license.html
/usr/share/gtk-doc/html/colord/right-insensitive.png
/usr/share/gtk-doc/html/colord/right.png
/usr/share/gtk-doc/html/colord/style.css
/usr/share/gtk-doc/html/colord/up-insensitive.png
/usr/share/gtk-doc/html/colord/up.png

%files lib
%defattr(-,root,root,-)
/usr/lib64/colord-plugins/libcolord_sensor_camera.so
/usr/lib64/colord-plugins/libcolord_sensor_scanner.so
/usr/lib64/colord-sensors/libcolord_sensor_argyll.so
/usr/lib64/colord-sensors/libcolord_sensor_colorhug.so
/usr/lib64/colord-sensors/libcolord_sensor_dtp94.so
/usr/lib64/colord-sensors/libcolord_sensor_dummy.so
/usr/lib64/colord-sensors/libcolord_sensor_huey.so
/usr/lib64/libcolord.so.2
/usr/lib64/libcolord.so.2.0.5
/usr/lib64/libcolordprivate.so.2
/usr/lib64/libcolordprivate.so.2.0.5
/usr/lib64/libcolorhug.so.2
/usr/lib64/libcolorhug.so.2.0.5

%files libexec
%defattr(-,root,root,-)
/usr/libexec/colord
/usr/libexec/colord-session

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/colord/COPYING

%files services
%defattr(-,root,root,-)
/usr/lib/systemd/system/colord.service
/usr/lib/systemd/user/colord-session.service

%files locales -f colord.lang
%defattr(-,root,root,-)

