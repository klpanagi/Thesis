## IP-Forwarding on Host PC


In order to forward traffic between two interfaces, we need to enable ip-forwarding kernel option on host-pc.
This way we can forward traffic from an iface connected to the public web (e.g eth0)
to a device connected on another iface (e.g. eth1)

### Check if IP Forwarding is enabled
We have to query the sysctl kernel value net.ipv4.ip_forward to see if forwarding is enabled or not: Using sysctl:

```bash
sysctl net.ipv4.ip_forward
```

### Enable IP Forwarding on the fly
As with any sysctl kernel parameters we can change the value of net.ipv4.ip_forward on the fly (without rebooting the system):

```bash
sysctl -w net.ipv4.ip_forward=1
```

### Permanent setting using /etc/sysctl.conf
If we want to make this configuration permanent the best way to do it is using the file
/etc/sysctl.conf where we can add a line containing net.ipv4.ip_forward = 1

```
/etc/sysctl.conf:
net.ipv4.ip_forward = 1
```

If you already have an entry net.ipv4.ip_forward with the value 0 you can change that 1.

To enable the changes made in sysctl.conf you will need to run the command:

```
sysctl -p /etc/sysctl.conf
```



