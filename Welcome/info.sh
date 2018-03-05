#!/bin/bash
cd "/usr/local/bin/Solar Pi/Welcome"
uname -r > sysinfo
df -h --output=size,used,avail,pcent >> sysinfo
cat /etc/*release* > osinfo
