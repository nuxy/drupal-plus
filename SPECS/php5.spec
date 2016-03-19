%define name    drupal+php7
%define version 7.0.4
%define release 1

Summary:       PHP: Hypertext Preprocessor
Name:          %{name}
Packager:      Marc S. Brooks <devel@mbrooks.info>
Version:       %{version}
Release:       %{release}
License:       The PHP license (see "LICENSE" file included in distribution)
URL:           https://github.com/nuxy/drupal8-plus
Group:         Development/Languages
Source:        php-%{version}.tar.gz

BuildRequires: gcc, make, libxml2-devel, libjpeg-devel, libpng-devel, pcre-devel
AutoReq:       no

%description
PHP is an HTML-embedded scripting language. Much of its syntax is
borrowed from C, Java and Perl with a couple of unique PHP-specific
features thrown in. The goal of the language is to allow web
developers to write dynamically generated pages quickly.

%prep
%setup -n php-%{version}

%build
%{configure} --prefix=%{_prefix} --bindir=%{_bindir} --sysconfdir=%{_sysconfdir} --with-openssl --with-pdo-mysql --with-gd --with-jpeg-dir=%{_libdir} --with-zlib-dir=%{_libdir} --enable-mbstring --enable-fpm --enable-opcache

%install
%{__make} INSTALL_ROOT=$RPM_BUILD_ROOT install

%{__rm} -f $RPM_BUILD_ROOT/%{_bindir}/phar
cd $RPM_BUILD_ROOT/%{_bindir}
%{__ln_s} phar.phar phar

curl -sS https://getcomposer.org/installer | $RPM_BUILD_ROOT%{_bindir}/php

if [ ! -e $RPM_BUILD_ROOT%{_bindir}/composer ]; then
  %{__ln_s} composer.phar composer
fi

%files
%defattr(-,root,root)
%{_bindir}
%{_datadir}
%{_includedir}
%{_libdir}
%{_mandir}

%dir %{_sysconfdir}

%config(noreplace) %{_sysconfdir}/pear.conf

%exclude %{_prefix}/conf/php-fpm.conf.default
%exclude %{_prefix}/conf/php-fpm.d/www.conf.default
%exclude /.channels
%exclude /.depdb
%exclude /.depdblock
%exclude /.filemap
%exclude /.lock
%exclude /.registry

%pre
/usr/sbin/useradd -c 'php-fpm user' -s /sbin/nologin -r -d %{_localstatedir}/run/php-fpm php-fpm 2> /dev/null || :

%preun

# REMOVE: Stop the service and remove the user.
if [ $1 -eq 0 ]; then
    %{_prefix}/init.d/php-fpm stop > /dev/null 2>&1
    /usr/sbin/userdel php-fpm
fi

%postun

# UPGRADE: Restart the service.
if [ $1 -ge 1 ]; then
    %{_prefix}/init.d/php-fpm restart > /dev/null 2>&1
fi

%changelog
* Fri Jan 18 2016  Marc S. Brooks <devel@mbrooks.info> r1
- Updated to latest stable release.

* Fri Jan  1 2016  Marc S. Brooks <devel@mbrooks.info> r4
- Enabled zLib library.

* Mon Dec 28 2015  Marc S. Brooks <devel@mbrooks.info> r3
- Fixed bugs in the Composer installation process.
- Enabled support for PHP OPcode caching.
- Updated php5 dependency package name (now php7)

* Fri Dec 25 2015  Marc S. Brooks <devel@mbrooks.info> r2
- Updating package to PHP7 (stable)
- Removed composer %{_ls} since it's now part of the install process.
- Added php-www.conf %exclude to %files

* Sat Aug 22 2015  Marc S. Brooks <devel@mbrooks.info> r1
- Update to latest stable release

* Sun Mar 22 2015 Marc S. Brooks <devel@mbrooks.info> r2
- Removed -o argument since this fails on x86_64

* Sat Mar 21 2015  Marc S. Brooks <devel@mbrooks.info> r1
- Initial release based on drupal7-plus sources.
- Added support for Composer package management tool.
