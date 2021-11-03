#Using a Custom SSH Key, checking remote connections
ansible all -m ping --private-key=~/.ssh/my_custom_key
#For PLaybook:
ansible-playbook myplaybook.yml --private-key=~/.ssh/my_custom_key
#Using password:
ansible all -m ping --ask-pass
ansible-playbook myplaybook.yml --ask-pass
