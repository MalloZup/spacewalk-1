%define registry	%{_sysconfdir}/rc.d/np.d/apachereg
Name:         status_log_acceptor
Source0:      %{name}-%{version}.tar.gz
Version:      0.12.5
Release:      8%{?dist}
Summary:      Current state log acceptor
# This src.rpm is cannonical upstream
# You can obtain it using this set of commands
# git clone git://git.fedorahosted.org/git/spacewalk.git/
# cd monitoring/status_log_acceptor
# make srpm
URL:          https://fedorahosted.org/spacewalk
BuildArch:    noarch
Requires:     perl(:MODULE_COMPAT_%(eval "`%{__perl} -V:version`"; echo $version))
Requires:	  SatConfig-general
Group:        Applications/Internet
License:      GPLv2
Buildroot:     %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

%description
Provides the cgi that accepts a status log, parses it, and stores the 
information.

%prep
%setup -q

%build
#Nothing to build

%install
rm -rf $RPM_BUILD_ROOT
 
mkdir -p $RPM_BUILD_ROOT%{perl_vendorlib}/NOCpulse
#mkdir -p $RPM_BUILD_ROOT%{perl_vendorlib}/NOCpulse/AcceptStatusLog/test
mkdir -p $RPM_BUILD_ROOT%{registry}
 
install -m 444 AcceptStatusLog.pm $RPM_BUILD_ROOT%{perl_vendorlib}/NOCpulse
install -m 444 Apache.status_log_acceptor $RPM_BUILD_ROOT%{registry}
#install -m 444 test/TestAcceptStatusLog.pm $RPM_BUILD_ROOT%{perl_vendorlib}/NOCpulse/AcceptStatusLog/test

%files
%defattr(-,root,root,-)
%{perl_vendorlib}/NOCpulse/*
%{registry}/Apache.status_log_acceptor

%clean
rm -rf $RPM_BUILD_ROOT

%changelog
* Thu Sep 25 2008 Miroslav Suchý <msuchy@redhat.com> 
- spec cleanup for Fedora

* Mon Jun 16 2008 Milan Zazrivec <mzazrivec@redhat.com> 0.12.5-8
- cvs.dist import
