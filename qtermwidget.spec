#
# Conditional build:
#
%define		qtver		5.3.1

Summary:	qtermwidget
Name:		qtermwidget
Version:	0.7.0
Release:	1
License:	GPLv2 and LGPL-2.1+
Group:		X11/Applications
Source0:	http://downloads.lxqt.org/qtermwidget/%{version}/%{name}-%{version}.tar.xz
# Source0-md5:	9744afd8228b831e0021a2badfb076b8
URL:		http://www.lxqt.org/
BuildRequires:	cmake >= 2.8.11
BuildRequires:	glib2-devel
BuildRequires:	liblxqt-devel >= 0.11.0
BuildRequires:	libqtxdg-devel >= 2.0.0
BuildRequires:	menu-cache-devel >= 0.4.0
BuildRequires:	xorg-lib-libX11-devel
BuildRequires:	xz-devel
Requires:	lxqt-common
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
qtermwidget

%package devel
Summary:	qtermwidget - header files and development documentation
Summary(pl.UTF-8):	Pliki nagłówkowe i dokumentacja do qtermwidg
Group:		X11/Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	Qt5Core-devel >= %{qtver}
Requires:	Qt5Gui-devel >= %{qtver}
Requires:	Qt5Xml-devel >= %{qtver}

%description devel
This package contains header files and development documentation for
qtermwidget.

%description devel -l pl.UTF-8
Pakiet ten zawiera pliki nagłówkowe i dokumentację potrzebną przy
pisaniu własnych programów wykorzystującyqtermwid.

%prep
%setup -q

%build
install -d build
cd build
%cmake \
	-DPULL_TRANSLATIONS:BOOL=OFF \
	../

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} -C build install \
	DESTDIR=$RPM_BUILD_ROOT

#%find_lang %{name} --all-name --with-qm

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libqtermwidget5.so.0.7.*
%attr(755,root,root) %ghost %{_libdir}/libqtermwidget5.so.0
%{_datadir}/qtermwidget5

%files devel
%defattr(644,root,root,755)
%{_libdir}/libqtermwidget5.so
%{_includedir}/qtermwidget5
%{_pkgconfigdir}/qtermwidget5.pc
%{_datadir}/cmake/qtermwidget5
