%define name    drupal
%define version 8.0.1
%define release 1

Summary:   Open Source CMS
Name:      %{name}
Packager:  Marc S. Brooks <devel@mbrooks.info>
Version:   %{version}
Release:   %{release}
License:   GPL
URL:       https://github.com/nuxy/drupal8-plus
Group:     Application/Web
Source:    drupal-%{version}.tar.gz

Requires(pre): drupal+config, drupal+php5, drupal+nginx
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

# On install, update sites/files directory permissions.
if [ $1 -eq 0 ]; then
  %{__chown} -R php-fpm:php-fpm %{_prefix}/php-bin/sites/files
fi

# On upgrade, replace sites directory with backup.
if [ $1 -gt 1 ] && [ -d %{_tmppath}/sites ]; then
  %{__mv} %{_tmppath}/sites %{_prefix}/php-bin/sites
fi

%preun

# Backup Drupal sources prior to uninstall process.
if [ $1 -eq 0 ]; then
  BACKUP=drupal-$(date +%s).tar.gz

  %{__tar} cfz %{_prefix}/$BACKUP %{_prefix}/php-bin > /dev/null 2>&1

  %{__cat} <<EOF
drupal+ php-bin sources have been backed up to:
   %{_prefix}/$BACKUP
EOF
fi

# On upgrade, preserve the sites directory.
if [ $1 -gt 1 ] && [ -d %{_prefix}/php-bin/sites ]; then
  %{__mv} %{_prefix}/php-bin/sites %{_tmppath}/sites
fi

%changelog
* Fri Dec 25 2015  Marc S. Brooks <devel@mbrooks.info> 2
- Drupal 8 production release is here.
- Update %preun/post to handle install and upgrade states.

* Sat Aug 22 2015  Marc S. Brooks <devel@mbrooks.info> beta14
- Latest Drupal development release.

* Sat Mar 21 2015  Marc S. Brooks <devel@mbrooks.info> beta1
- Updated package URL to current Github repository endpoint
