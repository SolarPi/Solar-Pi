#!/bin/bash
find "/usr/local/bin/Solar Pi" -type f -iname "*.sh" -exec chmod +x {} \;

sudo service apache2 stop
sudo htcacheclean -d60 -n -t -p /var/cache/apache2/mod_cache_disk -l 50M -i
sudo service apache2 start