#!/bin/bash

sudo grep -R 'usb_port_owner_info=0'
stat=$?

if [ ${stat} == 1 ]; then
  ## Setup USB port to enable USB 3.0 support
  sudo sed -i 's/usb_port_owner_info=0/usb_port_owner_info=2/' /boot/extlinux/extlinux.conf
fi

