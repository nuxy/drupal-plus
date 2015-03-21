%define name    drupal
%define version 8.0.0
%define release beta1

Summary:   Open Source CMS
Name:      %{name}
Packager:  Marc S. Brooks <devel@mbrooks.info>
Version:   %{version}
Release:   %{release}
License:   GPL
URL:       https://github.com/nuxy/drupal8-plus
Group:     Application/Web
Source:    drupal-%{version}-%{release}.tar.gz

Requires(pre): drupal+config, drupal+php5, drupal+nginx
AutoReq:       0

%description
Drupal is an open source content management platform powering millions of websites
and applications. It's built, used, and supported by an active and diverse
community of people around the world.

%prep
%setup -n drupal-%{version}-%{release}

%install
%{__mkdir} -p $RPM_BUILD_ROOT%{_prefix}/php-bin
%{__cp} -r ./ $RPM_BUILD_ROOT%{_prefix}/php-bin

%files
%{_prefix}/php-bin

%clean
%{__rm} -rf $RPM_BUILD_ROOT

%post
%{__chown} -R php-fpm:php-fpm %{_prefix}/php-bin/sites

%preun
BACKUP=drupal-$(date +%s).tar.gz

%{__tar} cfz %{_prefix}/$BACKUP %{_prefix}/php-bin > /dev/null 2>&1

%{__cat} <<EOF

drupal+ php-bin sources have been backed up to:
   %{_prefix}/$BACKUP

EOF

%changelog
* Sat Mar 21 2015  Marc S. Brooks <devel@mbrooks.info> beta1
