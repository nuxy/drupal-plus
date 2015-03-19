%define name    drupal+php5
%define version 5.5.22
%define release 2

Summary:       PHP: Hypertext Preprocessor
Name:          %{name}
Packager:      Marc S. Brooks <devel@mbrooks.info>
Version:       %{version}
Release:       %{release}
License:       The PHP license (see "LICENSE" file included in distribution)
URL:           https://github.com/nuxy/drupal-plus
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
%{configure} --prefix=%{_prefix} --bindir=%{_bindir} --sysconfdir=%{_sysconfdir} --with-pdo-mysql --with-gd --with-jpeg-dir=%{_libdir} --enable-mbstring --enable-fpm

%install
%{__make} INSTALL_ROOT=$RPM_BUILD_ROOT install

%{__rm} -f $RPM_BUILD_ROOT/%{_bindir}/phar
cd $RPM_BUILD_ROOT/%{_bindir}
%{__ln_s} phar.phar phar

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
%exclude /.channels
%exclude /.depdb
%exclude /.depdblock
%exclude /.filemap
%exclude /.lock
%exclude /.registry

%pre
/usr/sbin/useradd -c 'php-fpm user' -s /sbin/nologin -r -d %{_localstatedir}/run/php-fpm php-fpm 2> /dev/null || :

%preun
if [ $1 = 0 ]; then
  /usr/sbin/userdel php-fpm
fi

%postun
if [ "$1" -ge 1 ]; then
   /sbin/service php-fpm restart > /dev/null 2>&1
fi

%changelog
* Wed Mar 18 2015  Marc S. Brooks <devel@mbrooks.info> beta1
- Initial release based on drupal7-plus sources.
