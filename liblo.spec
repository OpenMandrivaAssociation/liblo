%define major		7
%define libname		%mklibname lo %{major}
%define develname	%mklibname lo -d

Summary:	Open Sound Control protocol
Name:		liblo
Version:	0.26
Release:	6
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
	--disable-static 
# do not use ipv6 atm since it causes slowness when calling dssi objects
#	--enable-ipv6

%make
										
%install
rm -rf %{buildroot}
%makeinstall_std
rm -rf %{buildroot}%{_libdir}/*.la

%clean
rm -rf %{buildroot}

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
%{_libdir}/pkgconfig/*.pc


%changelog
* Mon May 02 2011 Oden Eriksson <oeriksson@mandriva.com> 0.26-5mdv2011.0
+ Revision: 661481
- mass rebuild

* Sun Nov 28 2010 Oden Eriksson <oeriksson@mandriva.com> 0.26-4mdv2011.0
+ Revision: 602568
- rebuild

* Sat May 15 2010 Frank Kober <emuse@mandriva.org> 0.26-3mdv2010.1
+ Revision: 544850
- do not use --enable-ipv6 configure option causing slowness
  when no ipv6 address is setup in /etc/hosts

* Tue Mar 16 2010 Oden Eriksson <oeriksson@mandriva.com> 0.26-2mdv2010.1
+ Revision: 520878
- rebuilt for 2010.1

* Sat Jun 06 2009 Tomasz Pawel Gajc <tpg@mandriva.org> 0.26-1mdv2010.0
+ Revision: 383273
- update to new version 0.26
- major has changed from 0 to 7 (?)
- enable ipv6 support
- spec file clean

* Wed Aug 13 2008 Funda Wang <fwang@mandriva.org> 0.25-1mdv2009.0
+ Revision: 271455
- New version 0.25

* Tue Jun 17 2008 Thierry Vignaud <tv@mandriva.org> 0.24-4mdv2009.0
+ Revision: 222921
- rebuild

  + Pixel <pixel@mandriva.com>
    - do not call ldconfig in %%post/%%postun, it is now handled by filetriggers

* Tue Mar 04 2008 Oden Eriksson <oeriksson@mandriva.com> 0.24-3mdv2008.1
+ Revision: 178963
- rebuild

  + Thierry Vignaud <tv@mandriva.org>
    - rebuild
    - kill re-definition of %%buildroot on Pixel's request

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

* Wed Jul 25 2007 Adam Williamson <awilliamson@mandriva.org> 0.24-1mdv2008.0
+ Revision: 55104
- rebuild for 2008
- new devel policy
- new release 0.24
- Import liblo



* Sun Jul 23 2006 Emmanuel Andry <eandry@mandriva.org> 0.23-1mdv2007.0
- 0.23
- %%mkrel

* Sun Jan 01 2006 Mandriva Linux Team <http://www.mandrivaexpert.com/> 0.18pp-2mdk
- Rebuild

* Sat Jul 2 2005 Austin Acton <austin@mandriva.org> 0.18pp-1mdk
- 0.18
- patches (pp) from http://freebob.sourceforge.net/

* Sun Aug 8 2004 Austin Acton <austin@mandrake.org> 0.8-1mdk
- initial package
