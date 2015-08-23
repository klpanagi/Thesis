#!/bin/bash

## Disable USB autosuspend mode

sudo grep -R 'usbcore.autosuspend=-1' /boot/extlinux/extlinux.conf &> /dev/null
stat=$?

if [ ${stat} == 1 ]; then
  ## Setup USB port to enable USB 3.0 support
  sudo sed -i '$s/$/ usbcore.autosuspend=-1/'  /boot/extlinux/extlinux.conf &> /dev/null
fi

