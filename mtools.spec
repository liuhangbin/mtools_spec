# https://docs.fedoraproject.org/en-US/packaging-guidelines/SourceURL/
%global debug_package %{nil}
%global forgeurl    https://github.com/troglobit/mtools
%global gittag      v3.0

Name:               mtools
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
rm -rf $RPM_BUILD_ROOT/ChangeLog.md
rm -rf $RPM_BUILD_ROOT/README.md

%install
%{make_install} DESTDIR=%{buildroot} prefix=%{_prefix}

%files
%{_sbindir}/msend
%{_sbindir}/mreceive
%{_mandir}/man8/msend.8*
%{_mandir}/man8/mreceive.8*
%doc LICENSE.md
%doc ChangeLog.md
%doc README.md

%changelog
* Mon Oct 14 2024 Hangbin Liu <liuhangbin@gmail.com> - 3.0-1
- init with v3.0
