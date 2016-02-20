%global pkg_name maven-shared-io
%{?scl:%scl_package %{pkg_name}}
%{?maven_find_provides_and_requires}

Name:           %{?scl_prefix}%{pkg_name}
Version:        1.1
Release:        7.10%{?dist}
# Maven-shared defines maven-shared-io version as 1.2
Epoch:          1
Summary:        API for I/O support like logging, download or file scanning.
License:        ASL 2.0
URL:            http://maven.apache.org/shared/maven-shared-io
# svn export http://svn.apache.org/repos/asf/maven/shared/tags/maven-shared-io-1.1 maven-shared-io-1.1
# tar caf maven-shared-io-1.1.tar.xz maven-shared-io-1.1/
Source0:        %{pkg_name}-%{version}.tar.xz
# ASL mandates that the licence file be included in redistributed source
Source1:        http://www.apache.org/licenses/LICENSE-2.0.txt
BuildArch:      noarch

BuildRequires:  %{?scl_prefix_java_common}maven-local
BuildRequires:  maven30-maven-shared
BuildRequires:  %{?scl_prefix_java_common}easymock


%description
API for I/O support like logging, download or file scanning.

This is a replacement package for maven-shared-io

%package javadoc
Summary:        Javadoc for %{pkg_name}
    
%description javadoc
API documentation for %{pkg_name}.

%prep
%setup -q -n %{pkg_name}-%{version}
%{?scl:scl enable maven30 %{scl} - <<"EOF"}
set -e -x

%pom_add_dep org.apache.maven:maven-compat

# Failing tests
rm src/test/java/org/apache/maven/shared/io/location/ArtifactLocatorStrategyTest.java
rm src/test/java/org/apache/maven/shared/io/download/DefaultDownloadManagerTest.java

cp %{SOURCE1} LICENSE.txt
%{?scl:EOF}

%build
%{?scl:scl enable maven30 %{scl} - <<"EOF"}
set -e -x
%mvn_build
%{?scl:EOF}

%install
%{?scl:scl enable maven30 %{scl} - <<"EOF"}
set -e -x
%mvn_install
%{?scl:EOF}

%files -f .mfiles
%{_javadir}/%{pkg_name}
%dir %{_mavenpomdir}/%{pkg_name}
%doc LICENSE.txt

%files javadoc -f .mfiles-javadoc
%doc LICENSE.txt

%changelog
* Sat Jan 09 2016 Michal Srb <msrb@redhat.com> - 1:1.1-7.10
- maven33 rebuild

* Thu Jan 15 2015 Mikolaj Izdebski <mizdebsk@redhat.com> - 1:1.1-7.9
- Add directory ownership on %%{_mavenpomdir} subdir

* Tue Jan 13 2015 Michael Simacek <msimacek@redhat.com> - 1:1.1-7.8
- Mass rebuild 2015-01-13

* Tue Jan 06 2015 Michael Simacek <msimacek@redhat.com> - 1:1.1-7.7
- Mass rebuild 2015-01-06

* Mon May 26 2014 Mikolaj Izdebski <mizdebsk@redhat.com> - 1:1.1-7.6
- Mass rebuild 2014-05-26

* Wed Feb 19 2014 Mikolaj Izdebski <mizdebsk@redhat.com> - 1:1.1-7.5
- Mass rebuild 2014-02-19

* Tue Feb 18 2014 Mikolaj Izdebski <mizdebsk@redhat.com> - 1:1.1-7.4
- Mass rebuild 2014-02-18

* Mon Feb 17 2014 Mikolaj Izdebski <mizdebsk@redhat.com> - 1:1.1-7.3
- SCL-ize build-requires

* Thu Feb 13 2014 Mikolaj Izdebski <mizdebsk@redhat.com> - 1:1.1-7.2
- Rebuild to regenerate auto-requires

* Tue Feb 11 2014 Mikolaj Izdebski <mizdebsk@redhat.com> - 1:1.1-7.1
- First maven30 software collection build

* Fri Dec 27 2013 Daniel Mach <dmach@redhat.com> - 1:1.1-7
- Mass rebuild 2013-12-27

* Fri Jun 28 2013 Mikolaj Izdebski <mizdebsk@redhat.com> - 1:1.1-6
- Rebuild to regenerate API documentation
- Resolves: CVE-2013-1571

* Tue Feb 19 2013 Mikolaj Izdebski <mizdebsk@redhat.com> - 1:1.1-5
- Build with xmvn

* Mon Feb 18 2013 Mikolaj Izdebski <mizdebsk@redhat.com> - 1:1.1-4
- Drop dependency on plexus-container-default

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1:1.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Wed Feb 06 2013 Java SIG <java-devel@lists.fedoraproject.org> - 1:1.1-2
- Update for https://fedoraproject.org/wiki/Fedora_19_Maven_Rebuild
- Replace maven BuildRequires with maven-local

* Tue Jan 15 2013 Tomas Radej <tradej@redhat.com> - 1:1.1-1
- Initial version

