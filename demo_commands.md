for example with aws:

ansible appservers -i demo_hosts -m ansible.builtin.copy  -a "src=./sample_file.txt dest=/home/ubuntu" -u ubuntu --private-key=/Users/sandipdas/AwsDevOps.pem 

ansible-playbook platbook_sample.yml -i demo_hosts --private-key=/Users/sandipdas/AwsDevOps.pem 

ansible-playbook playbook_role_example.yml -i demo_hosts --private-key=/Users/sandipdas/AwsDevOps.pem 


ssh -i "AwsDevOps.pem" ubuntu@ec2-34-213-232-34.us-west-2.compute.amazonaws.com 