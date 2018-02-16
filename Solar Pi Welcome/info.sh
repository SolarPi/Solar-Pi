#!/bin/bash
uname -r > sysinfo
df -h --output=size,used,avail,pcent >> sysinfo
cat /etc/*release* > osinfo