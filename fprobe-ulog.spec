Name:		fprobe-ulog
Version:	1.1
Release:	1
Summary:	fprobe-ulog: a NetFlow probe
Group:		Network/Monitoring
License:	GPL
URL:		http://fprobe.sourceforge.net
Source0:	%{name}-%{version}.tar.bz2
Buildroot:	%{_tmppath}/%{name}-buildroot
Provides:	fprobe-ulog

%description
fprobe-ulog - libipulog-based tool that collect network traffic data and emit
it as NetFlow flows towards the specified collector.

%prep
%setup -q

%build
./configure --sbindir=%{_sbindir} --mandir=%{_mandir} $EXTRA_OPTIONS
make

%install
rm -rf %{buildroot}
make install-strip DESTDIR=%{buildroot}
gzip --best %{buildroot}%{_mandir}/man8/fprobe-ulog.8

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc AUTHORS ChangeLog NEWS README COPYING TODO
/*
