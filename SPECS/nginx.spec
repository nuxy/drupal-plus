%define name    drupal+nginx
%define version 1.6.2
%define release 2

Summary:       Robust, small and high performance http and reverse proxy
Name:          %{name}
Packager:      Marc S. Brooks <devel@mbrooks.info>
Version:       %{version}
Release:       %{release}
License:       BSD
URL:           https://github.com/nuxy/drupal-plus
Group:         System Environment/Daemons
Source:        nginx-%{version}.tar.gz

BuildRequires: gcc, make, pcre-devel, openssl-devel

%description
nginx [engine x] is an HTTP and reverse proxy server, as well as a mail proxy server, written by Igor Sysoev

%prep
%setup -n nginx-%{version}

%build
./configure --prefix=%{_prefix} --sbin-path=%{_bindir}/nginx --error-log-path=%{_localstatedir}/log/nginx/error.log --lock-path=%{_localstatedir}/lock/nginx.lock --pid-path=%{_localstatedir}/run/nginx.pid --http-log-path=%{_localstatedir}/log/nginx/http.log --http-client-body-temp-path=%{_tmppath}/nginx/client-body.tmp --http-fastcgi-temp-path=%{_tmppath}/nginx/fastcgi.tmp --with-http_ssl_module --without-http_proxy_module --without-http_scgi_module --without-http_uwsgi_module

%install
%{__make} DESTDIR=$RPM_BUILD_ROOT install

%{__mkdir} -p $RPM_BUILD_ROOT%{_localstatedir}/log/nginx
%{__mkdir} -p $RPM_BUILD_ROOT%{_localstatedir}/run/nginx
%{__mkdir} -p $RPM_BUILD_ROOT%{_localstatedir}/tmp/nginx
%{__mkdir} -p $RPM_BUILD_ROOT%{_prefix}/logs

%{__rm} -f $RPM_BUILD_ROOT%{_sysconfdir}/*fastcgi*
%{__rm} -f $RPM_BUILD_ROOT%{_sysconfdir}/*params*
%{__rm} -f $RPM_BUILD_ROOT%{_sysconfdir}/nginx.conf

%files
%defattr(-,root,root)
%{_bindir}/nginx
%{_prefix}/conf
%{_prefix}/html

%dir %{_prefix}/logs

%attr(0700,nginx,nginx) %dir %{_localstatedir}/log/nginx
%attr(0700,nginx,nginx) %dir %{_localstatedir}/run/nginx
%attr(0700,nginx,nginx) %dir %{_localstatedir}/tmp/nginx

%clean
%{__rm} -rf $RPM_BUILD_ROOT

%pre
/usr/sbin/useradd -c 'nginx daemon' -s /sbin/nologin -r -d %{_localstatedir}/run/nginx nginx 2> /dev/null || :

%preun
if [ $1 = 0 ]; then
  /usr/sbin/userdel nginx
fi

%postun
if [ "$1" -ge 1 ]; then
   /sbin/service nginx restart > /dev/null 2>&1
fi

%changelog
* Wed Mar 18 2015  Marc S. Brooks <devel@mbrooks.info> beta1
- Initial release based on drupal7-plus sources.
