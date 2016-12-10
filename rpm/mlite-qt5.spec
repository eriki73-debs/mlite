Name:       mlite-qt5
Summary:    Useful classes originating from MeeGo Touch
Version:    0.2.21.1
Release:    1
Group:      System/Libraries
License:    LGPLv2.1
URL:        http://github.com/nemomobile/mlite
Source0:    %{name}-%{version}.tar.bz2
Requires(post): /sbin/ldconfig
Requires(postun): /sbin/ldconfig
BuildRequires:  pkgconfig(Qt5DBus)
BuildRequires:  pkgconfig(Qt5Core)
BuildRequires:  pkgconfig(Qt5Gui)
BuildRequires:  pkgconfig(Qt5Test)
BuildRequires:  pkgconfig(dconf)
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  qt5-qttools-linguist

%description
Select set of useful classes from meegotouch that do not require
taking in all of meegotouch.


%package notificationtool
Summary:    mlite notification tool package
Group:      System/Libraries
Requires:   %{name} = %{version}-%{release}

%description notificationtool
%{summary}.


%package devel
Summary:    mlite development package
Group:      System/Libraries
Requires:   %{name} = %{version}-%{release}

%description devel
Development files needed for using the mlite library


%package tests
Summary:    Test suite for mlite-qt5
Group:      System/Libraries
Requires:   %{name} = %{version}-%{release}
Requires:   dbus-x11

%description tests
Test suite for mlite-qt5.


%prep
%setup -q -n %{name}-%{version}

%build
export QT_SELECT=5
%qmake5 VERSION=%{version}
make %{?_smp_mflags}

%install
rm -rf %{buildroot}
%qmake5_install

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%files
%defattr(-,root,root,-)
%{_libdir}/libmlite5.so.*
%{_libexecdir}/mliteremoteaction

%files notificationtool
%defattr(-,root,root,-)
%{_bindir}/mlitenotificationtool

%files devel
%defattr(-,root,root,-)
%{_includedir}/mlite5
%{_libdir}/pkgconfig/*.pc
%{_libdir}/libmlite5.so

%files tests
%defattr(-,root,root,-)
/opt/tests/mlite-qt5/*
