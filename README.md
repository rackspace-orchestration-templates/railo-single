[![Circle CI](https://circleci.com/gh/rackspace-orchestration-templates/railo-single/tree/master.png?style=shield)](https://circleci.com/gh/rackspace-orchestration-templates/railo-single)
Description
===========

A template that deploys open source Railo onto a single Linux server.


Instructions
===========

#### Welcome to Railo
This will deploy a single Linux server running
[Railo](http://www.getrailo.org/index.cfm/documentation/).
This deployment does not come with any preconfigured Railo applications.
You will need to [add sites to the server manually](https://github.com/getrailo/railo/wiki/Installation-InstallerDocumentation-LinAddingSites).

#### Logging in via SSH
The private key provided in the passwords section can be used to login as
root via SSH.  We have an article on how to use these keys with [Mac OS X and
Linux](http://www.rackspace.com/knowledge_center/article/logging-in-with-a-ssh-private-key-on-linuxmac)
as well as [Windows using
PuTTY](http://www.rackspace.com/knowledge_center/article/logging-in-with-a-ssh-private-key-on-windows).

#### Admin Interface
The admin interface for Railo runs on port 8888 which isn't exposed
by default by this deployment. If you didn't provide an admin user
ip address during setup, login using ssh and issue the following command
where <ip> is replaced by your IP address:
'ufw allow from <ip> to any port 8888'

#### Railo Service
Railo can be controlled using the standard 'service' command.

service railo_ctl status
service railo_ctl stop
service railo_ctl start
service railo_ctl restart


Requirements
============
* A Heat provider that supports the following:
  * OS::Heat::RandomString
  * OS::Nova::KeyPair
  * Rackspace::Cloud::Server
* An OpenStack username, password, and tenant id.
* [python-heatclient](https://github.com/openstack/python-heatclient)
`>= v0.2.8`:

```bash
pip install python-heatclient
```

We recommend installing the client within a [Python virtual
environment](http://www.virtualenv.org/).

Parameters
==========
Parameters can be replaced with your own values when standing up a stack. Use
the `-P` flag to specify a custom parameter.

* `flavor`: Rackspace Cloud Server flavor to use. The size is based on the amount of
RAM for the provisioned server.
 (Default: 1 GB Performance)
* `image`: Server image used for all servers that are created as a part of this
deployment
 (Default: Ubuntu 14.04 LTS (Trusty Tahr) (PVHVM))
* `server_name`: The instance name (Default: railo)
* `railo_user`: The user Railo runs as. (Default: railo)
* `railo_admin_ip`: The IP address from where the administrator should have access. (Default: 127.0.0.1)
* `railo_installer_location`: Location of the Railo installer file. (Default: http://www.getrailo.org/railo/remote/download42/4.2.1.008/tomcat/linux/railo-4.2.1.008-pl0-linux-x64-installer.run
)

Outputs
=======
Once a stack comes online, use `heat output-list` to see all available outputs.
Use `heat output-show <OUTPUT NAME>` to get the value of a specific output.

* `private_key`: SSH Private Key
* `railo_admin_pass`: Railo Administration Password
* `railo_url`: Railo URL
* `server_ip`: Server IP

For multi-line values, the response will come in an escaped form. To get rid of
the escapes, use `echo -e '<STRING>' > file.txt`. For vim users, a substitution
can be done within a file using `%s/\\n/\r/g`.
