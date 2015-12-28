%define name    drupal
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
Source:    drupal-%{version}.tar.gz

Requires(pre): drupal+config, drupal+php7, drupal+nginx
AutoReq:       0

%description
Drupal is an open source content management platform powering millions of websites
and applications. It's built, used, and supported by an active and diverse
community of people around the world.

%prep
%setup -n drupal-%{version}

%install
%{__mkdir} -p $RPM_BUILD_ROOT%{_prefix}/php-bin
%{__cp} -r ./ $RPM_BUILD_ROOT%{_prefix}/php-bin

%files
%{_prefix}/php-bin

%clean
%{__rm} -rf $RPM_BUILD_ROOT

%post

# REMOVE:
if [ $1 -eq 0 ]; then
    %{__rm} -rf %{_prefix}/php-bin
fi

# INSTALL: Create sites/files directory if doesn't exist.
if [ $1 -eq 1 ] && [ ! -e %{_prefix}/php-bin/sites/default/files ]; then
    %{__mkdir} -p %{_prefix}/php-bin/sites/default/files
    %{__chown} -R php-fpm:php-fpm %{_prefix}/php-bin/sites/default/files

    %{__cp} %{_prefix}/php-bin/sites/default/default.settings.php %{_prefix}/php-bin/sites/default/settings.php
    %{__chmod} 666 %{_prefix}/php-bin/sites/default/settings.php
fi

# UPGRADE: Replace sites directory with preserved files.
if [ $1 -gt 1 ] && [ -d %{_tmppath}/sites ]; then
    %{__mv} %{_tmppath}/sites %{_prefix}/php-bin/sites
fi

%preun

# REMOVE: Backup Drupal sources prior to uninstall process.
if [ $1 -eq 0 ]; then
    BACKUP=drupal-$(date +%s).tar.gz

    %{__tar} cfz %{_prefix}/$BACKUP %{_prefix}/php-bin > /dev/null 2>&1

    %{__cat} <<EOF
drupal+ php-bin sources have been backed up to:
  %{_prefix}/$BACKUP

EOF
fi

# UPGRADE: Preserve the current sites directory.
if [ $1 -gt 1 ] && [ -d %{_prefix}/php-bin/sites ]; then
    %{__mv} %{_prefix}/php-bin/sites %{_tmppath}/sites
fi

%changelog
* Mon Dec 28 2015  Marc S. Brooks <devel@mbrooks.info> r2
- Fixed incorrect value of $1 in state check.
- Added conditional checks to %post and %preun build states.
- Updated php5 dependency package name (now php7)

* Fri Dec 25 2015  Marc S. Brooks <devel@mbrooks.info> r1
- Drupal 8 production release is here.
- Update %preun/post to handle install and upgrade states.
