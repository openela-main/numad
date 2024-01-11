%global systemctl_bin /usr/bin/systemctl

Name: numad
Version: 0.5
Release: 26.20150602git%{?dist}
Summary: NUMA user daemon

License: LGPLv2
Group: System Environment/Daemons
URL: https://pagure.io/numad
# The source for this package was pulled from upstream's vcs.  Use the
# following commands to generate the tarball:
#   git clone https://pagure.io/numad.git numad-0.5git
#   tar --exclude-vcs -cJf numad-0.5git.tar.xz numad-0.5git/
Source0: %{name}-%{version}git.tar.xz

Requires: systemd-units
Requires(post): systemd-units
Requires(preun): systemd-units
BuildRequires: systemd-units

ExcludeArch: s390 %{arm}

%description
Numad, a daemon for NUMA (Non-Uniform Memory Architecture) systems,
that monitors NUMA characteristics and manages placement of processes
and memory to minimize memory latency and thus provide optimum performance.

%prep
%setup -q -n %{name}-%{version}git

%build
make CFLAGS="$RPM_OPT_FLAGS -std=gnu99" LDFLAGS="$RPM_LD_FLAGS -lpthread -lrt -lm"

%install
mkdir -p %{buildroot}%{_bindir}
mkdir -p %{buildroot}%{_sysconfdir}/logrotate.d
mkdir -p %{buildroot}%{_unitdir}
mkdir -p %{buildroot}%{_mandir}/man8/
install -p -m 644 numad.service %{buildroot}%{_unitdir}/
install -p -m 644 numad.logrotate %{buildroot}%{_sysconfdir}/logrotate.d/%{name}
make install prefix=%{buildroot}/usr

%files
%{_bindir}/numad
%{_unitdir}/numad.service
%config(noreplace) %{_sysconfdir}/logrotate.d/numad
%doc %{_mandir}/man8/numad.8.gz

%post
%systemd_post numad.service

%preun
%systemd_preun numad.service

%postun
%systemd_postun numad.service

%changelog
* Tue Jun 19 2018 Jan Synáček <jsynacek@redhat.com> - 0.5-26.20150602git
- Remove initscripts from Requires (#1610280)

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.5-25.20150602git
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.5-24.20150602git
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.5-23.20150602git
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Dan Horák <dan[at]danny.cz> - 0.5-22.20150602git
- Enable on s390x

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.5-21.20150602git
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.5-20.20150602git
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Tue Jun  2 2015 Jan Synáček <jsynacek@redhat.com> - 0.5-19.20150602git
- Update to 20150602

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.5-18.20140620git
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Mon Jun 23 2014 Jan Synáček <jsynacek@redhat.com> - 0.5-17.20140620git
- Update to 20140620

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.5-16.20140225git
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Tue Mar 25 2014 Jan Synáček <jsynacek@redhat.com> - 0.5-15.20140225git
- Update to the correct upstream version of 20140225

* Fri Feb 28 2014 Jan Synáček <jsynacek@redhat.com> - 0.5-14.20140225git
- Update to 20140225
- Resolves: #1071221

* Mon Jan 20 2014 Ville Skyttä <ville.skytta@iki.fi> - 0.5-13.20130814git
- Don't order service after syslog.target (#1055209).
- Build with $RPM_OPT_FLAGS and $RPM_LD_FLAGS.
- Fix build with -Werror=format-security.

* Wed Aug 14 2013 Jan Synáček <jsynacek@redhat.com> - 0.5-12.20130814git
- Update to 20130814

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.5-11.20121130git
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.5-10.20121130git
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Tue Dec 11 2012 Jan Synáček <jsynacek@redhat.com> - 0.5-9.20121130git
- Update and comment the Makefile patch
- Related: #825153

* Mon Dec 03 2012 Jan Synáček <jsynacek@redhat.com> - 0.5-8.20121130git
- Update to 20121130
- Update spec: fix command to generate tarball

* Tue Oct 16 2012 Jan Synáček <jsynacek@redhat.com> - 0.5-7.20121015git
- Update to 20121015
- Add Makefile patch
- Update spec: update command to generate tarball

* Wed Aug 22 2012 Jan Synáček <jsynacek@redhat.com> - 0.5-6.20120522git
- add systemd-rpm macros
- Resolves: #850236

* Fri Jul 20 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.5-5.20120522git
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Wed May 23 2012 Jan Synáček <jsynacek@redhat.com> - 0.5-4.20120522git
- update source (20120522) and manpage

* Tue Mar 06 2012 Jan Synáček <jsynacek@redhat.com> 0.5-3.20120221git
- update source
- drop the patch

* Fri Feb 24 2012 Jan Synáček <jsynacek@redhat.com> 0.5-2.20120221git
- add BuildRequires: systemd-units

* Wed Feb 15 2012 Jan Synáček <jsynacek@redhat.com> 0.5-1.20120221git
- spec update

* Fri Feb 10 2012 Bill Burns <bburns@redhat.com> 0.5-1
- initial version
