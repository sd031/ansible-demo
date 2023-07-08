# Learn With Sandip

## Ansible Full Course For Beginers

[![N|Solid](https://learn.sandipdas.in/wp-content/uploads/sites/2/2021/08/Untitled-design-2.png)](https://learn.sandipdas.in/)

This project help you get started with Asible Ad-hoc commands, Playbook, Role ad Vault

[Watch FULL FREE Video Course here](https://youtu.be/s4cXrNEDYiw)

 [Sandip Das]: <https://www.linkedin.com/in/sandip-das-developer>
This Project Designed and developed by [Sandip Das]

## Tech

This project uses  open source  projects to work properly:

- [Ansible](https://nodejs.org/en/about/)

## Ansible Installation

First make sure [Ansible CLI is installed](https://docs.ansible.com/ansible/latest/installation_guide/intro_installation.html)

Debain/Ubuntu Installation Example

```sh
sudo apt update
sudo apt install software-properties-common
sudo add-apt-repository --yes --update ppa:ansible/ansible
sudo apt install ansible
```

Check Version

```sh
ansible --version
```

## Genereate Custom SSH Keys

Setting up ssh:

```sh
sudo apt-get install openssh-server
```

Generating new ssh keys:

```sh
ssh-keygen
```

ssh-copy-id hostname (if it's a password-based)

```sh
ssh-copy-id -i ~/.ssh/my_custom_key user@host
```

Time to check SSH Connection

```sh
ssh -i ~/.ssh/my_custom_key user@host
```

## Sample Invetory (Hosts) File

File path: /etc/ansible/hosts (or custom location by: -i /path/to/file)

```sh

#un-grouped
192.0.2.40
192.0.3.56
aserver.example.org
bserver.example.org
#by group called appservers
[appservers]
sample1.example.com ansible_host = 10.0.0.3 #ssh to 10.0.0.3
sample2.example.com ansible_ssh_user = xyz #ssh as user xyz
#host (DNS will resolve automatically)
[dbservers]
one.example.com
two.example.com
three.example.com
#dev_servers1 is a group containing other groups
[dev_servers1:children] 
appservers 
dbservers
```

## Ansible Ad-hoc Commands

## Rebooting servers

Reboot all servers in appservers group

```sh
ansible appservers -a "/sbin/reboot"
```

Reboot the appservers hosts with 10 parallel forks

```sh
ansible appservers -a "/sbin/reboot" -f 10
```

To run To run /usr/bin/ansible from a differet user account (not root)

```sh
ansible appservers -a "/sbin/reboot" -f 10 -u username
```

run commands through privilege escalation

```sh
ansible appservers -a "/sbin/reboot" -f 10 -u username --become [--ask-become-pass]
```

## Managing files (Copy and moving file)

copy file

```sh
ansible appservers -m ansible.builtin.copy -a "src=/etc/hosts dest=/tmp/hosts"
```

changing permissions

```sh
ansible appservers -m ansible.builtin.file -a "dest=/srv/foo/a.txt mode=600"
ansible appservers -m ansible.builtin.file -a "dest=/srv/foo/b.txt mode=600 owner=sandip group=sandip"
```

create directores

```sh
ansible appservers -m ansible.builtin.file -a "dest=/path/to/c mode=755 owner=sandip group=sandip state=directory"
```

Remove Directory/File

```sh
ansible appservers -m ansible.builtin.file -a "dest=/path/to/c state=absent"
```

## Managing packages (Install, update and remove packages)

using yum package manager to install and uninstall packages

```sh
ansible appservers -m ansible.builtin.yum -a "name=acme state=present"
ansible appservers -m ansible.builtin.yum -a "name=acme-1.5 state=present"
ansible appservers -m ansible.builtin.yum -a "name=acme state=latest"
ansible appservers -m ansible.builtin.yum -a "name=acme state=absent"
```

using apt package manager to install and uninstall packages

```sh
ansible appservers -m apt -a "name=acme state=latest"
ansible appservers -m apt -a "name=acme-1.5 state=present"
```

## Managing users and groups (adding , removing users and/or groups )

```sh
ansible all -m ansible.builtin.user -a "name=foo password=<crypted password here>"
ansible all -m ansible.builtin.user -a "name=foo state=absent"
```

## Managing services (Start, Stop, Restart Services)

```sh
ansible appservers -m ansible.builtin.service -a "name=httpd state=started"
ansible appservers -m ansible.builtin.service -a "name=httpd state=restarted"
ansible appservers -m ansible.builtin.service -a "name=httpd state=stopped"
```

Deploying From Source Control

```sh
ansible appservers -m git -a "repo=<https://foo.example.org/repo.git> dest=/src/myapp version=HEAD"
```

Gathering facts

```sh
ansible all -m ansible.builtin.setup
```

## Sample Playbook

Normal
playbook_sample.yml

```sh
---
- name: Installl and Verify apache installation
  hosts: appservers
  vars:
    http_port: 80
    max_clients: 200
  remote_user: ubuntu
  become: yes
  become_method: sudo
  tasks:
  - name: Ensure apache is at the latest version
    ansible.builtin.apt:
      name: apache2
      state: latest

  - name: Ensure apache is running
    ansible.builtin.service:
      name: apache2
      state: started
```

Role bases
playbook_role_example.yml

```sh
---
- hosts: appservers
  remote_user: ubuntu
  become: yes
  become_method: sudo
  roles:
    - example_role
```
Sample Commands to Execute PLaybooks
```sh
ansible-playbook platbook_sample.yml -i demo_hosts --private-key=/path/to/your/key

ansible-playbook playbook_role_example.yml -i demo_hosts --private-key=/path/to/your/key
```

## Asible Vault

Creating a New Encrypted File
```sh
ansible-vault create encrypted_playbook.yml
```


Encrypting an Existing Ansible File
```sh
ansible-vault encrypt encrypted_playbook.yml
```


View encrypted file
```sh
ansible-vault view encrypted_playbook.yml
```


Edit encrypted file
```sh
ansible-vault edit encrypted_playbook.yml
```


Permanently Decrypt a file
```sh
ansible-vault decrypt encrypted_playbook.yml
```


Using Multiple Vault Passwords for multiple environments 
 We can have dedicated vault passwords for different environments, such as development, testing, and production environments 
 ```sh
ansible-vault create --vault-id dev@prompt credentials_dev.yml
ansible-vault create --vault-id prod@prompt credentials_prod.yml
```

To Edit/edit have to provide the same id
 ```sh
ansible-vault edit credentials_dev.yml --vault-id dev@prompt
```


Using a Password File
```sh
ansible-vault create --vault-password-file path/to/passfile credentials_dev.yml
ansible-vault create --vault-id dev@path/to/passfile credentials_dev.yml

ansible-vault encrypt --vault-password-file vault_pass encrypted_playbook.yml
ansible-vault decrypt --vault-password-file vault_pass encrypted_playbook.yml
```





## License

MIT

**Free Software, Hell Yeah!**
