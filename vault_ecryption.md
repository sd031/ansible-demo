#Creating a New Encrypted File
ansible-vault create encrypted_playbook.yml

#Encrypting an Existing Ansible File
ansible-vault encrypt encrypted_playbook.yml

#View encrypted file
ansible-vault view encrypted_playbook.yml

#Edit encrypted file
ansible-vault edit encrypted_playbook.yml

#Permanently Decrypt a file
ansible-vault decrypt encrypted_playbook.yml

#Using Multiple Vault Passwords for multiple environments 
 We can have dedicated vault passwords for different environments, such as development, testing, and production environments 
ansible-vault create --vault-id dev@prompt credentials_dev.yml
ansible-vault create --vault-id prod@prompt credentials_prod.yml
To Edit/edit have to provide the same id
ansible-vault edit credentials_dev.yml --vault-id dev@prompt

#Using a Password File
ansible-vault create --vault-password-file path/to/passfile credentials_dev.yml
ansible-vault create --vault-id dev@path/to/passfile credentials_dev.yml

ansible-vault encrypt --vault-password-file vault_pass encrypted_playbook.yml
ansible-vault decrypt --vault-password-file vault_pass encrypted_playbook.yml