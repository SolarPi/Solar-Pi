#!/bin/bash
sudo mkdir -p "/usr/local/bin/Solar Pi/ramdisk"
sudo mount -t tmpfs -o size=1M tmpfs "/usr/local/bin/Solar Pi/ramdisk"
sudo chown -R pi: "/usr/local/bin/Solar Pi/ramdisk"