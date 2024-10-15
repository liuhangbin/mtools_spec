# https://docs.fedoraproject.org/en-US/packaging-guidelines/SourceURL/
%global debug_package %{nil}
%global forgesetupargs -n mtools-%{version}
%global forgeurl    https://github.com/troglobit/mtools
%global gittag      v3.0

Name:               mcast-tools
Version:            3.0
Release:            1%{?dist}
Summary:            mtools for multicast debugging
%forgemeta

License:            CC0-1.0
URL:                %{forgeurl}
Source:             %{forgesource}

BuildRequires:      gcc
BuildRequires:      make

%description
This package contains tools msend and mreceive for multicast debugging.

%prep
%forgeautosetup

%build
%{make_build}
# make doc dir changeable
sed -i 's/datadir *=/datadir ?=/' Makefile

%install
%{make_install} DESTDIR=%{buildroot} prefix=%{_prefix} datadir=%{doc}

%files
%{_sbindir}/msend
%{_sbindir}/mreceive
%{_mandir}/man8/msend.8*
%{_mandir}/man8/mreceive.8*
%doc LICENSE.md ChangeLog.md README.md

%changelog
* Mon Oct 14 2024 Hangbin Liu <liuhangbin@gmail.com> - 3.0-1
- init with v3.0
