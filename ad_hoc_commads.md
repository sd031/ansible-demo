#Rebooting servers
#reboot all servers in appservers group 
ansible appservers -a "/sbin/reboot"
#reboot the appservers hosts with 10 parallel forks
ansible appservers -a "/sbin/reboot" -f 10
#to run To run /usr/bin/ansible from a differet user account (not root)
ansible appservers -a "/sbin/reboot" -f 10 -u username
#run commands through privilege escalation 
ansible appservers -a "/sbin/reboot" -f 10 -u username --become [--ask-become-pass]


Managing files (Copy and moving file)
#copy file
ansible appservers -m ansible.builtin.copy -a "src=/etc/hosts dest=/tmp/hosts"
#changing permissions 
ansible appservers -m ansible.builtin.file -a "dest=/srv/foo/a.txt mode=600"
ansible appservers -m ansible.builtin.file -a "dest=/srv/foo/b.txt mode=600 owner=sandip group=sandip"
#create directores
ansible appservers -m ansible.builtin.file -a "dest=/path/to/c mode=755 owner=sandip group=sandip state=directory"
#Remove Directory/File
ansible appservers -m ansible.builtin.file -a "dest=/path/to/c state=absent"

Managing packages (Install, update and remove packages)
#using yum package manager to install and uninstall packages
ansible appservers -m ansible.builtin.yum -a "name=acme state=present"
ansible appservers -m ansible.builtin.yum -a "name=acme-1.5 state=present"
ansible appservers -m ansible.builtin.yum -a "name=acme state=latest"
ansible appservers -m ansible.builtin.yum -a "name=acme state=absent"
#using apt package manager to install and uninstall packages
ansible appservers -m apt -a "name=acme state=latest"
ansible appservers -m apt -a "name=acme-1.5 state=present"

Managing users and groups (adding , removing users and/or groups )
ansible all -m ansible.builtin.user -a "name=foo password=<crypted password here>"
ansible all -m ansible.builtin.user -a "name=foo state=absent"

Managing services (Start, Stop, Restart Services)
ansible appservers -m ansible.builtin.service -a "name=httpd state=started"
ansible appservers -m ansible.builtin.service -a "name=httpd state=restarted"
ansible appservers -m ansible.builtin.service -a "name=httpd state=stopped"

Deploying From Source Control
ansible appservers -m git -a "repo=https://foo.example.org/repo.git dest=/src/myapp version=HEAD"
Gathering facts
ansible all -m ansible.builtin.setup