%define name    drupal+drush
%define version 8.0.1
%define release 2

Summary:   Open Source CMS
Name:      %{name}
Packager:  Marc S. Brooks <devel@mbrooks.info>
Version:   %{version}
Release:   %{release}
License:   GPL
URL:       https://github.com/nuxy/drupal8-plus
Group:     Application/Web
Source:    drush-%{version}.tar.gz

Requires(pre): drupal+config, drupal+php7
AutoReq:       0

%description
Drush is a command-line shell and scripting interface for Drupal, a veritable
Swiss Army knife designed to make life easier for those who spend their
working hours hacking away at the command prompt.

%prep
%setup -n drush-%{version}

%build
%{__mkdir} -p $RPM_BUILD_ROOT%{_prefix}

%install
%{__cp} -ar %{_topdir}/BUILD/drush-%{version} $RPM_BUILD_ROOT%{_prefix}/drush

%files
%{_prefix}/drush

%post

# INSTALL: Install the Drush binary using Composer.
if [ $1 -eq 1 ]; then
    %{__ln_s} %{_prefix}/drush/drush %{_bindir}/drush

    cd %{_prefix}/drush
    %{_bindir}/php %{_bindir}/composer install -q
fi

%{__cat} <<EOF
drush has been installed in:
  /usr/local/drupal+/bin

To use drush you must add drupal+ to your session PATH
  $ export PATH=\$PATH:/usr/local/drupal+/bin

EOF

%preun
%{__rm} -rf %{_prefix}/bin/drush
%{__rm} -rf %{_prefix}/drush/vendor

%clean
%{__rm} -rf $RPM_BUILD_ROOT

%changelog
* Mon Dec 28 2015 Marc S. Brooks <devel@mbrooks.info> 2
- Added %preun to remove Composer install artifacts.
- Updated operator in conditional check.
- Added --quiet to disable Composer STDOUT
- Updated php5 dependency package name (now php7)

* Sun Dec 26 2015 Marc S. Brooks <devel@mbrooks.info> 1
- Updated package to latest stable release

* Sun Mar 22 2015 Marc S. Brooks <devel@mbrooks.info> alpha9
- Added missing comma to dependency list
- Added full path to PHP binary in composer install

* Sat Mar 21 2015  Marc S. Brooks <devel@mbrooks.info> alpha9
- Initial release based on drupal7-plus sources.
