#Creating a New Encrypted File
ansible-vault create credentials.yml

#Encrypting an Existing Ansible File
ansible-vault encrypt credentials.yml

#View encrypted file
ansible-vault view credentials.yml

#Edit encrypted file
ansible-vault edit credentials.yml

#Permanently Decrypt a file
ansible-vault decrypt credentials.yml

#Using Multiple Vault Passwords for multiple environments 
 We can have dedicated vault passwords for different environments, such as development, testing, and production environments 
ansible-vault create --vault-id dev@prompt credentials_dev.yml
ansible-vault create --vault-id prod@prompt credentials_prod.yml
To Edit/edit have to provide the same id
ansible-vault edit credentials_dev.yml --vault-id dev@prompt

#Using a Password File
ansible-vault create --vault-password-file path/to/passfile credentials_dev.yml
ansible-vault create --vault-id dev@path/to/passfile credentials_dev.yml