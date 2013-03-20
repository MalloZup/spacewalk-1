Name:       spacewalk-branding
Version:    1.10.9
Release:    1%{?dist}
Summary:    Spacewalk branding data

Group:      Applications/Internet
License:    GPLv2
URL:        https://fedorahosted.org/spacewalk/
Source0:    https://fedorahosted.org/releases/s/p/spacewalk/%{name}-%{version}.tar.gz
BuildRoot:  %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:  noarch

BuildRequires: java-devel >= 1.5.0
Requires:   httpd

%description
Spacewalk specific branding, CSS, and images.

%prep
%setup -q

%build

javac java/code/src/com/redhat/rhn/branding/strings/StringPackage.java
rm -f java/code/src/com/redhat/rhn/branding/strings/StringPackage.java
jar -cf java-branding.jar -C java/code/src com

%install
rm -rf %{buildroot}
install -d -m 755 %{buildroot}%{_var}/www/html
install -d -m 755 %{buildroot}%{_datadir}/spacewalk
install -d -m 755 %{buildroot}%{_datadir}/spacewalk/web
install -d -m 755 %{buildroot}%{_datadir}/spacewalk/web/nav
install -d -m 755 %{buildroot}%{_datadir}/rhn/lib/
%if  0%{?rhel} && 0%{?rhel} < 6
install -d -m 755 %{buildroot}%{_var}/lib/tomcat5/webapps/rhn/WEB-INF/lib/
%else
%if 0%{?fedora}
install -d -m 755 %{buildroot}%{_var}/lib/tomcat/webapps/rhn/WEB-INF/lib/
%else
install -d -m 755 %{buildroot}%{_var}/lib/tomcat6/webapps/rhn/WEB-INF/lib/
%endif
%endif
install -d -m 755 %{buildroot}/%{_sysconfdir}/rhn
install -d -m 755 %{buildroot}/%{_prefix}/share/rhn/config-defaults
cp -pR css %{buildroot}/%{_var}/www/html/
cp -pR img %{buildroot}/%{_var}/www/html/
# Appplication expects two favicon's for some reason, copy it so there's just
# one in source:
cp -p img/favicon.ico %{buildroot}/%{_var}/www/html/
cp -pR templates %{buildroot}%{_datadir}/spacewalk/web/
cp -pR styles %{buildroot}%{_datadir}/spacewalk/web/nav/
cp -pR setup  %{buildroot}%{_datadir}/spacewalk/
cp -pR java-branding.jar %{buildroot}%{_datadir}/rhn/lib/
%if  0%{?rhel} && 0%{?rhel} < 6
ln -s %{_datadir}/rhn/lib/java-branding.jar %{buildroot}%{_var}/lib/tomcat5/webapps/rhn/WEB-INF/lib/java-branding.jar
%else
%if 0%{?fedora}
ln -s %{_datadir}/rhn/lib/java-branding.jar %{buildroot}%{_var}/lib/tomcat/webapps/rhn/WEB-INF/lib/java-branding.jar
%else
ln -s %{_datadir}/rhn/lib/java-branding.jar %{buildroot}%{_var}/lib/tomcat6/webapps/rhn/WEB-INF/lib/java-branding.jar
%endif
%endif
cp -p conf/rhn_docs.conf %{buildroot}/%{_prefix}/share/rhn/config-defaults/rhn_docs.conf

%clean
rm -rf %{buildroot}


%files
%dir %{_var}/www/html/css
%{_var}/www/html/css/*
%dir /%{_var}/www/html/img
%{_var}/www/html/img/*
%{_var}/www/html/favicon.ico
%{_datadir}/spacewalk/
%{_datadir}/rhn/lib/java-branding.jar
%if  0%{?rhel} && 0%{?rhel} < 6
%{_var}/lib/tomcat5/webapps/rhn/WEB-INF/lib/java-branding.jar
%else
%if 0%{?fedora}
%{_var}/lib/tomcat/webapps/rhn/WEB-INF/lib/java-branding.jar
%else
%{_var}/lib/tomcat6/webapps/rhn/WEB-INF/lib/java-branding.jar
%endif
%endif
%{_prefix}/share/rhn/config-defaults/rhn_docs.conf
%doc LICENSE

%changelog
* Wed Mar 20 2013 Tomas Kasparek <tkasparek@redhat.com> 1.10.9-1
- changing structure of css files

* Sun Mar 17 2013 Tomas Kasparek <tkasparek@redhat.com> 1.10.8-1
- removing unreferenced images from spacewalk-branding

* Thu Mar 14 2013 Jan Pazdziora 1.10.7-1
- rhn-iecompat.css is never used - delete it

* Thu Mar 14 2013 Tomas Kasparek <tkasparek@redhat.com> 1.10.6-1
- removing unused styles from rhn-basic.css
- removing unused styles from blue-docs.css

* Wed Mar 13 2013 Tomas Kasparek <tkasparek@redhat.com> 1.10.5-1
- removing unused styles and refactoring blue-nav-top.css and adjacent files
- removing unused styles from rhn-header.css
- removing unused styles from rhn-listview.css
- removing unused styles from rhn-messaging.css
- removing unused styles from rhn-nav-sidenav.css
- rmoving some unused styles from rhn-status.css

* Tue Mar 12 2013 Tomas Kasparek <tkasparek@redhat.com> 1.10.4-1
- clean up of rhn-special-styles.css and adjacent files
- removing css hacks for vintage versions of IE

* Mon Mar 11 2013 Tomas Kasparek <tkasparek@redhat.com> 1.10.3-1
- removing duplicate css
- removing -moz- in front of border-radius
- css changes - table borders

* Fri Mar 08 2013 Milan Zazrivec <mzazrivec@redhat.com> 1.10.2-1
- removing filter input from page when printing

* Wed Mar 06 2013 Tomas Kasparek <tkasparek@redhat.com> 1.10.1-1
- using css3 border-radius instead of images to render round edges
- Bumping package versions for 1.9

* Fri Mar 01 2013 Tomas Lestach <tlestach@redhat.com> 1.9.6-1
- introducing crash logo
- Purging %%changelog entries preceding Spacewalk 1.0, in active packages.

* Thu Jan 31 2013 Michael Mraka <michael.mraka@redhat.com> 1.9.5-1
- removed no longer necessary directory definitions
- pack branding template files outside of document root

* Tue Dec 04 2012 Jan Pazdziora 1.9.4-1
- On Fedoras, start to use tomcat >= 7.

* Wed Nov 28 2012 Tomas Lestach <tlestach@redhat.com> 1.9.3-1
- 470463 - fixing xmllint issue

* Mon Nov 12 2012 Tomas Lestach <tlestach@redhat.com> 1.9.2-1
- Fix typos

* Mon Nov 12 2012 Tomas Lestach <tlestach@redhat.com> 1.9.1-1
- 866326 - customize KickstartFileDownloadAdvanced.do page in case of kickstart
  file DownloadException
- reformated using xmllint -format
- Bumping package versions for 1.9.

* Wed Oct 24 2012 Jan Pazdziora 1.8.7-1
- WebUI - css for @media print

* Tue Oct 23 2012 Tomas Lestach <tlestach@redhat.com> 1.8.6-1
- make the white image background transparent
- Expose extra packages / systems with extra packages

* Fri Oct 19 2012 Jan Pazdziora 1.8.5-1
- Edit colors in highlightning of :hovered rows in list views
- Highlightning of :hover row in list views

* Wed Oct 10 2012 Jan Pazdziora 1.8.4-1
- The Sniglets::Utils is no longer needed in footer.pxt.
- The rhn-bugzilla-link generates emply paragraph.

* Mon Jun 04 2012 Miroslav Suchý <msuchy@redhat.com> 1.8.3-1
- Add support for studio image deployments (web UI) (jrenner@suse.de)
- %%defattr is not needed since rpm 4.4 (msuchy@redhat.com)

* Fri Apr 27 2012 Jan Pazdziora 1.8.2-1
- Missing icon for the systems that need reboot list (dmacvicar@suse.de)

* Thu Apr 19 2012 Jan Pazdziora 1.8.1-1
- Update the copyright year info on .pxt pages.

* Mon Feb 27 2012 Jan Pazdziora 1.7.1-1
- automatically focus search form (msuchy@redhat.com)

* Fri Sep 30 2011 Jan Pazdziora 1.6.4-1
- 621531 - move /etc/rhn/default to /usr/share/rhn/config-defaults (branding).

* Fri Sep 02 2011 Jan Pazdziora 1.6.3-1
- 558972 - making the navigational bar nice on 2000+ px wide screens.

* Fri Aug 05 2011 Jan Pazdziora 1.6.2-1
- 458413 - hide the bubble help links since we do not ship the documentation
  with Spacewalk.

* Fri Jul 22 2011 Jan Pazdziora 1.6.1-1
- cleanup: revhistory style is not used (msuchy@redhat.com)
- fix typos in css (msuchy@redhat.com)

* Tue Jun 21 2011 Jan Pazdziora 1.5.2-1
- 708957 - remove RHN Satellite Proxy Release Notes link (tlestach@redhat.com)

* Tue May 10 2011 Jan Pazdziora 1.5.1-1
- 484895 - Point the release notes dispatcher to fedorahosted.org.

* Wed Mar 30 2011 Jan Pazdziora 1.4.3-1
- update copyright years (msuchy@redhat.com)
- implement common access keys (msuchy@redhat.com)

* Fri Feb 18 2011 Jan Pazdziora 1.4.2-1
- The LOGGED IN and SIGN OUT are not images since Satellite 5.0 (rhn-360.css),
  removing.

* Wed Feb 09 2011 Michael Mraka <michael.mraka@redhat.com> 1.4.1-1
- made system legend of the same width as side navigation

* Fri Dec 17 2010 Michael Mraka <michael.mraka@redhat.com> 1.3.2-1
- let import PXT modules on fly

* Thu Nov 25 2010 Miroslav Suchý <msuchy@redhat.com> 1.3.1-1
- add GPLv2 license (msuchy@redhat.com)
- cleanup spec (msuchy@redhat.com)
- remove .htaccess file (msuchy@redhat.com)
- point to url where we store tar.gz (msuchy@redhat.com)
- Bumping package versions for 1.3. (jpazdziora@redhat.com)

* Mon Sep 27 2010 Miroslav Suchý <msuchy@redhat.com> 1.2.2-1
- 627920 - Added a larger config file icon for symlinks. Thanks to Joshua Roys
  (paji@redhat.com)

* Wed Sep 01 2010 Jan Pazdziora 1.2.1-1
- 567885 - "Spacewalk release 0.9" leads to 404 (coec@war.coesta.com)

* Mon May 31 2010 Michael Mraka <michael.mraka@redhat.com> 1.1.2-1
- Adding the correct checkstyle for inactive systems
- Added the dupe compare css and javascript magic
- 572714 - fixing css issues with docs

* Mon Apr 19 2010 Michael Mraka <michael.mraka@redhat.com> 1.1.1-1
- bumping spec files to 1.1 packages

