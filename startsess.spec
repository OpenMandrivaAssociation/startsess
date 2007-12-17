%define _enable_debug_packages %{nil}
%define debug_package          %{nil}

Summary:	Tool to start LTSP sessions
Name:		startsess
Version:	1.1
Release:	%mkrel 2
License:	GPL
Group:		System/Servers
URL:		http://www.ltsp.org
Source0:	http://www.ltsp.org/tarballs/%{name}-%{version}.tar.bz2
BuildRequires:	dietlibc-devel
Patch0:		startsess.patch

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


