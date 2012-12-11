%define _enable_debug_packages %{nil}
%define debug_package          %{nil}

Summary:	Tool to start LTSP sessions
Name:		startsess
Version:	1.1
Release:	%mkrel 5
License:	GPL
Group:		System/Servers
URL:		http://www.ltsp.org
Source0:	http://www.ltsp.org/tarballs/%{name}-%{version}.tar.bz2
BuildRequires:	dietlibc-devel
Patch0:		startsess.patch
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot

%description
This program is used in LTSP to start the sessions (shell, telnet, startx).

%prep

%setup -n %{name}-%{version}
%patch0 -p0

%build
diet gcc -Os -o %{name} %{name}.c

%install
rm -rf %{buildroot}

install -d %{buildroot}/bin
install -m0755 %{name} %{buildroot}/bin/

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc COPYING README
%attr(0755,root,root) /bin/%{name}


%changelog
* Tue Sep 08 2009 Thierry Vignaud <tvignaud@mandriva.com> 1.1-5mdv2010.0
+ Revision: 434112
- rebuild

* Fri Aug 08 2008 Thierry Vignaud <tvignaud@mandriva.com> 1.1-4mdv2009.0
+ Revision: 269357
- rebuild early 2009.0 package (before pixel changes)

* Tue Jun 10 2008 Oden Eriksson <oeriksson@mandriva.com> 1.1-3mdv2009.0
+ Revision: 217547
- rebuilt against dietlibc-devel-0.32

* Fri Dec 21 2007 Olivier Blin <oblin@mandriva.com> 1.1-2mdv2008.1
+ Revision: 136523
- restore BuildRoot

  + Thierry Vignaud <tvignaud@mandriva.com>
    - kill re-definition of %%buildroot on Pixel's request


* Mon Mar 05 2007 Oden Eriksson <oeriksson@mandriva.com> 1.1-2mdv2007.0
+ Revision: 133051
- use dietlibc instead

* Wed Feb 07 2007 Oden Eriksson <oeriksson@mandriva.com> 1.1-1mdv2007.1
+ Revision: 117142
- Import startsess

* Fri Sep 29 2006 Oden Eriksson <oeriksson@mandriva.com> 1.1-1mdk
- initial Mandriva package (mille-xterm import)

