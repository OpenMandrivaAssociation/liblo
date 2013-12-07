%define major	7
%define libname	%mklibname lo %{major}
%define devname	%mklibname lo -d

Summary:	Open Sound Control protocol
Name:		liblo
Version:	0.27
Release:	5
License:	GPLv2
Group:		Sound
Url:		http://liblo.sourceforge.net/
Source0:	http://downloads.sourceforge.net/liblo/%{name}-%{version}.tar.gz
BuildRequires:	doxygen

%description
LibLO is an implementation of the Open Sound Control protocol for POSIX
systems, started by Steve Harris.

%package -n %{libname}
Summary:	Dynamic libraries from %{name}
Group:		System/Libraries

%description -n %{libname}
Dynamic libraries from %{name}.

%package -n %{devname}
Summary:	Header files and static libraries from %{name}
Group:		Development/C
Requires:	%{libname} >= %{version}-%{release}
Provides:	%{name}-devel = %{version}-%{release}

%description -n %{devname}
Libraries and includes files for developing programs based on %{name}.

%prep
%setup -q

%build
%configure2_5x \
	--disable-static 
# do not use ipv6 atm since it causes slowness when calling dssi objects
#	--enable-ipv6

%make
										
%install
%makeinstall_std

%files
%{_bindir}/*

%files -n %{libname}
%{_libdir}/liblo.so.%{major}*

%files -n %{devname}
%doc AUTHORS NEWS ChangeLog README
%{_includedir}/*
%{_libdir}/*.so
%{_libdir}/pkgconfig/*.pc

