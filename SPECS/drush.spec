%define name    drupal+drush
%define version 5.11.0
%define release 2

Summary:   Open Source CMS
Name:      %{name}
Packager:  Marc S. Brooks <devel@mbrooks.info>
Version:   %{version}
Release:   %{release}
License:   GPL
URL:       https://github.com/nuxy/drupal-plus
Group:     Application/Web
Source:    drush-%{version}.tar.gz

Requires(pre): drupal+config
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
if [ $1 == 1 ]; then
    %{__ln_s} %{_prefix}/drush/drush %{_prefix}/bin
fi

%{__cat} <<EOF

drush has been installed in:
   /usr/local/drupal+/bin

To use drush you must add drupal+ to your session PATH
  $ export PATH=\$PATH:/usr/local/drupal+/bin

EOF

%clean
%{__rm} -rf $RPM_BUILD_ROOT

%changelog
* Wed Mar 18 2015  Marc S. Brooks <devel@mbrooks.info> beta1
- Initial release based on drupal7-plus sources.
