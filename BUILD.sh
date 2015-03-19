#!/bin/sh

SPEC='php5.spec memcached.spec nginx.spec drupal.spec drush.spec config.spec'

for file in $SPEC
do
    rpmbuild -v -ba --macros=/usr/lib/rpm/macros:~/rpmbuild/.rpmmacros --clean SPECS/$file
done
