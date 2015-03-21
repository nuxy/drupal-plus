%define name    drupal+config
%define version 0.01
%define release 1

Summary:   drupal+ configuration files
Name:      %{name}
Packager:  Marc S. Brooks <devel@mbrooks.info>
Version:   %{version}
Release:   %{release}
License:   MIT
URL:       https://github.com/nuxy/drupal8-plus
Group:     Application/Web

Requires(pre): drupal, drupal+php5, drupal+memcached, drupal+nginx

%description
None

%build
%{__mkdir} -p $RPM_BUILD_ROOT%{_prefix}/init.d

%install
%{__cp} -ar %{_topdir}/FILES/init.d $RPM_BUILD_ROOT%{_prefix}

%{__mkdir} -p $RPM_BUILD_ROOT%{_sysconfdir}

%{__cp} %{_topdir}/FILES/conf/memcached.conf $RPM_BUILD_ROOT%{_sysconfdir}
%{__cp} %{_topdir}/FILES/conf/nginx.conf     $RPM_BUILD_ROOT%{_sysconfdir}
%{__cp} %{_topdir}/FILES/conf/php-fpm.conf   $RPM_BUILD_ROOT%{_sysconfdir}
%{__cp} %{_topdir}/FILES/conf/php.ini        $RPM_BUILD_ROOT%{_sysconfdir}

%files
%defattr(-,root,root)
%{_prefix}/init.d

%config(noreplace) %{_sysconfdir}/memcached.conf
%config(noreplace) %{_sysconfdir}/nginx.conf
%config(noreplace) %{_sysconfdir}/php-fpm.conf
%config(noreplace) %{_sysconfdir}/php.ini

%post
%{__mv} %{_prefix}/init.d/drupal+ /etc/init.d

/sbin/chkconfig --add drupal+

%{__cat} <<EOF

drupal+ configuration files have been installed in:
   /usr/local/drupal+/conf

To start the server run:
   service drupal+ start

EOF

%preun
if [ $1 = 0 ]; then
    /sbin/service drupal+ stop > /dev/null 2>&1
    /sbin/chkconfig --del drupal+
fi

%postun
if [ "$1" -ge 1 ]; then
   /sbin/service drupal+ restart > /dev/null 2>&1
fi

%{__rm} -f /etc/init.d/drupal+

%clean
%{__rm} -rf $RPM_BUILD_ROOT

%changelog
* Sat Mar 21 2015  Marc S. Brooks <devel@mbrooks.info> 1
- Initial release based on drupal7-plus sources.
