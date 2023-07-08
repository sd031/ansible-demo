Setting up ssh:
sudo apt-get install openssh-server

Generating new ssh keys:
ssh-keygen

ssh-copy-id hostname (if it's a password-based)
ssh-copy-id -i ~/.ssh/my_custom_key user@host

Time to check SSH Connection
ssh -i ~/.ssh/my_custom_key user@host