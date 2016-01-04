ISC-DHCP-SERVER Configurations
-----------------------------

# Install ISC-DHCP-SERVER

```shell
$ sudo apt-get install isc-dhcp-server
```

# Apply DHCP Server for a specific interface(s)

Copy **isc-dhcp_server** file under **/etc/default** directory

```shell
$ sudo cp isc-dhcp_server /etc/default/
```

# DHCP Server Configuration file

Copy the **dhcpd.conf** file under **/etc/dhcp/** directory
Keep a backup!

```shell
$ sudo mv /etc/dhcp/dhcpd.conf /etc/dhcp/dhcpd.cong.org
$ sudo cp dhcpd.conf /etc/dhcp/
```
