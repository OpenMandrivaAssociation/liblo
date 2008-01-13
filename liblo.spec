%define name	liblo
%define version	0.24
%define release %mkrel 2

%define major		0
%define libname 	%{mklibname lo %major}
%define develname	%{mklibname lo -d}

Name: 	 	%{name}
Summary: 	Open Sound Control protocol
Version: 	%{version}
Release: 	%{release}

Source:		http://plugin.org.uk/liblo/releases/%{name}-%{version}.tar.gz
URL:		http://plugin.org.uk/liblo/
License:	GPLv2
Group:		Sound
BuildRoot:	%{_tmppath}/%{name}-buildroot
BuildRequires:	doxygen

%description
LibLO is an implementation of the Open Sound Control protocol for POSIX
systems, started by Steve Harris.

%package -n 	%{libname}
Summary:        Dynamic libraries from %name
Group:          System/Libraries

%description -n %{libname}
Dynamic libraries from %name.

%package -n 	%{develname}
Summary: 	Header files and static libraries from %name
Group: 		Development/C
Requires: 	%{libname} >= %{version}-%{release}
Provides: 	%{name}-devel = %{version}-%{release}
Obsoletes:	%{mklibname lo 0 -d}

%description -n %{develname}
Libraries and includes files for developing programs based on %name.

%prep
%setup -q

%build
%configure2_5x --enable-static
%make
										
%install
rm -rf $RPM_BUILD_ROOT
%makeinstall

%clean
rm -rf $RPM_BUILD_ROOT

%post -n %{libname} -p /sbin/ldconfig
%postun -n %{libname} -p /sbin/ldconfig

%files -n %{libname}
%defattr(-,root,root)
%{_libdir}/*.so.*

%files -n %{develname}
%defattr(-,root,root)
%doc AUTHORS NEWS ChangeLog README
%{_includedir}/*
%{_libdir}/*.so
%{_libdir}/*.a
%{_libdir}/*.la
%{_libdir}/pkgconfig/*.pc
