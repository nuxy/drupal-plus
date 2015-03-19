%define name    drupal+memcached
%define version 1.4.22
%define release 2

Summary:       High Performance, Distributed Memory Object Cache
Name:          %{name}
Packager:      Marc S. Brooks <devel@mbrooks.info>
Version:       %{version}
Release:       %{release}
License:       BSD
URL:           https://github.com/nuxy/drupal-plus
Group:         System Environment/Daemons
Source:        memcached-%{version}.tar.gz

BuildRequires: gcc, make, libevent-devel

%description
memcached is a high-performance, distributed memory object caching
system, generic in nature, but intended for use in speeding up dynamic
web applications by alleviating database load.

%prep
%setup -n memcached-%{version}

%build

%ifarch i386
    export CFLAGS='-pthread -march=i386'
%endif

%{configure} --prefix=%{_prefix} --datarootdir=%{_datarootdir}

%install
%{__make} DESTDIR=$RPM_BUILD_ROOT install

%files
%defattr(-,root,root)
%{_prefix}

%clean
%{__rm} -rf $RPM_BUILD_ROOT

%pre
/usr/sbin/useradd -c 'memcached daemon' -s /sbin/nologin -r -d /var/run/memcached memcached 2> /dev/null || :

%preun
if [ $1 = 0 ]; then
  /usr/sbin/userdel memcached
fi

%postun
if [ "$1" -ge 1 ]; then
   /sbin/service memcached restart > /dev/null 2>&1
fi

%changelog
* Wed Mar 18 2015  Marc S. Brooks <devel@mbrooks.info> beta1
- Initial release based on drupal7-plus sources.
