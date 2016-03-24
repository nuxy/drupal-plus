<img src="https://github.com/nuxy/drupal8-plus/raw/master/preview.jpg" alt="drupal-plus" />

(**Updated** **3/18/2016**)

## Project

The overall goal of this project is to create a standard RPM bundle for installing/configuring Drupal 8 and related server dependencies.

## Provides

The following packages are installed and pre-configured in /usr/local/drupal+

*   [PHP](http://php.net) 7.0.4 / [php-fpm (Fast Process Manager)](http://php-fpm.org) / [pdo_mysql](http://www.php.net/manual/en/ref.pdo-mysql.php) / [Composer](https://getcomposer.org)
*   [nginx](http://nginx.org) 1.8.1
*   [memcached](http://memcached.org) 1.4.25
*   [Drupal](http://drupal.org) 8.0.4
*   [Drush](https://github.com/drush-ops/drush) 8.0.1

## Supported Systems

The RPMs provided with this bundle have been tested to work on both [32bit](https://mbrooks.info/files/rpm/drupal8-plus/i386) and [64bit](https://mbrooks.info/files/rpm/drupal8-plus/x86_64) servers running RHEL and CentOS 5+

## Directory Structure

In order to avoid conflicts with existing server packages the RPM build installs in its own directory.  This keeps your server and application contained to a single working directory that can be relocated or removed without affecting the main host.

The directory structure is as follows:

    /usr/local/drupal+
    /usr/local/drupal+/bin                 PHP5, composer, nginx, drush, memcached binaries
    /usr/local/drupal+/conf                PHP, PHP FPM, Memcached, nginx configurations
    /usr/local/drupal+/html                static content including error pages
    /usr/local/drupal+/init.d              package init scripts
    /usr/local/drupal+/include
    /usr/local/drupal+/lib
    /usr/local/drupal+/logs                HTTP request logs (enable in nginx.conf)
    /usr/local/drupal+/man
    /usr/local/drupal+/php-bin             Drupal 8 installation
    /usr/local/drupal+/share

## RPM Releases

For the lazy, I have provided pre-compiled [RPM](https://mbrooks.info/files/rpm/drupal8-plus)s for i386 and x86_64 architectures.  I will be updating these packages when either a dependency releases a new stable build, or in the event of a critical security fix.

## Get up and running in seconds

    $ rpm -i  drupal*.rpm
    $ service drupal+ start

Server runs on port 80 - It couldn't get any easier than this.

## Post Configuration

The server installation has been configured with some fairly conservative values.  It is recommended that you fine-tune these components based on system resources available to get the best performance for your Drupal application.

## Build Prerequisites

In order to compile custom RPMs the following packages must be installed on your server:

    gcc
    make
    pcre-devel
    libevent-devel
    libjpeg-devel
    libpng-devel
    libxml2-devel
    openssl-devel
    rpmdevtools

## Compiling

To create RPM packages specific to your host architecture:

1.  Install the rpm-build package and build prerequisites as listed above
2.  Pull the master branch contents into $HOME/rpmbuild (Note: Bundling as root is NOT recommended)
3.  In that same directory execute **BUILD.sh** shell script.

## Updating

To update post-installed packages:

    $ rpm -Uvh drupal-<package>.rpm

## Development

If you plan on doing PHP development or just need to run drush locally. It is important that *drupal+* is within your PATH

    $ export PATH=$PATH:/usr/local/drupal+/bin

## Package Sources

Due to space limitations, general bloatness, and other convincing reasons, *drupal+* dependencies will no longer stored in the Github repository. They will, however, be available and distributed as .src.rpm and can be accessed as such.

Download the RPMs and related sources [here](https://mbrooks.info/files/rpm/drupal8-plus).

## License and Warranty

This package is distributed in the hope that it will be useful, but without any warranty; without even the implied warranty of merchantability or fitness for a particular purpose.

*drupal+* is provided under the terms of the [MIT license](http://www.opensource.org/licenses/mit-license.php)

[Drupal](http://drupal.com) is a registered trademark of [Dries Buytaert](http://buytaert.net).

## Maintainer

[Marc S. Brooks](https://github.com/nuxy)
