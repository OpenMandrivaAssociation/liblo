%define major		7
%define libname		%mklibname lo %{major}
%define develname	%mklibname lo -d

Summary:	Open Sound Control protocol
Name:		liblo
Version:	0.26
Release:	%mkrel 3
License:	GPLv2
Group:		Sound
URL:		http://liblo.sourceforge.net/
Source0:	http://downloads.sourceforge.net/liblo/%{name}-%{version}.tar.bz2
BuildRequires:	doxygen
BuildRoot:	%{_tmppath}/%{name}-%{version}-buildroot

%description
LibLO is an implementation of the Open Sound Control protocol for POSIX
systems, started by Steve Harris.

%package -n %{libname}
Summary:	Dynamic libraries from %{name}
Group:		System/Libraries
Obsoletes:	%{mklibname lo 0}

%description -n %{libname}
Dynamic libraries from %{name}.

%package -n %{develname}
Summary:	Header files and static libraries from %{name}
Group:		Development/C
Requires:	%{libname} >= %{version}-%{release}
Provides:	%{name}-devel = %{version}-%{release}
Obsoletes:	%{mklibname lo 0 -d}

%description -n %{develname}
Libraries and includes files for developing programs based on %{name}.

%prep
%setup -q

%build
%configure2_5x \
	--enable-static 
# do not use ipv6 atm since it causes slowness when calling dssi objects
#	--enable-ipv6

%make
										
%install
rm -rf %{buildroot}
%makeinstall_std

%clean
rm -rf %{buildroot}

%if %mdkversion < 200900
%post -n %{libname} -p /sbin/ldconfig
%endif
%if %mdkversion < 200900
%postun -n %{libname} -p /sbin/ldconfig
%endif

%files
%defattr(-,root,root)
%{_bindir}/*

%files -n %{libname}
%defattr(-,root,root)
%{_libdir}/*.so.%{major}*

%files -n %{develname}
%defattr(-,root,root)
%doc AUTHORS NEWS ChangeLog README
%{_includedir}/*
%{_libdir}/*.so
%{_libdir}/*.a
%{_libdir}/*.la
%{_libdir}/pkgconfig/*.pc
