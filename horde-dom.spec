%define prj     Horde_DOM

%define xmldir  %{_var}/lib/pear
%define peardir %(pear config-get php_dir 2> /dev/null)

Name:          horde-dom
Version:       0.1.0
Release:       3
Summary:       Wrapper classes for PHP4 domxml compatibility using PHP5's dom functions
License:       LGPL
Group:         Networking/Mail
Url:           https://pear.horde.org/index.php?package=%{prj}
Source0:       %{prj}-%{version}.tgz
BuildArch:     noarch
Requires(pre): php-pear
Requires:      php-pear-channel-horde
BuildRequires: php-pear
BuildRequires: php-pear-channel-horde

%description
These classes allow the use of code written for PHP4's domxml implementation
to work using PHP5's dom implementation.


%prep
%setup -q -n %{prj}-%{version}

%build
%__mv ../package.xml .

%install
pear install --packagingroot %{buildroot} --nodeps package.xml

%__rm -rf %{buildroot}/%{peardir}/.{filemap,lock,registry,channels,depdb,depdblock}

%__mkdir_p %{buildroot}%{xmldir}
%__cp package.xml %{buildroot}%{xmldir}/%{prj}.xml

%clean
%__rm -rf %{buildroot}

%post
pear install --nodeps --soft --force --register-only %{xmldir}/%{prj}.xml

%postun
if [ "$1" -eq "0" ]; then
  pear uninstall --nodeps --ignore-errors --register-only pear.horde.org/%{prj}
fi

%files
%defattr(-, root, root)
%{xmldir}/%{prj}.xml
%dir %{peardir}/Horde
%{peardir}/Horde/DOM.php



%changelog
* Mon Jul 26 2010 Thomas Spuhler <tspuhler@mandriva.org> 0.1.0-2mdv2011.0
+ Revision: 560543
- Increased release for rebuild

* Sat Feb 20 2010 Thomas Spuhler <tspuhler@mandriva.org> 0.1.0-1mdv2010.1
+ Revision: 508846
- corrected Group
- corrected group
- import horde-dom


