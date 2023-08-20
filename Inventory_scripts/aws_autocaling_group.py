#!/usr/bin/env python

import boto3
import json

def get_instances_from_asg(asg_name):
    client = boto3.client('autoscaling')
    ec2 = boto3.resource('ec2')

    # Get details of the ASG
    response = client.describe_auto_scaling_groups(AutoScalingGroupNames=[asg_name])
    instance_ids = [i['InstanceId'] for i in response['AutoScalingGroups'][0]['Instances']]

    # Get the public IP addresses of the instances
    instances = ec2.instances.filter(InstanceIds=instance_ids)
    ips = [instance.public_ip_address for instance in instances if instance.public_ip_address]

    return ips

def main():
    asg_name = "ProductionGroup"
    hosts = get_instances_from_asg(asg_name)

    # Format the output for Ansible
    inventory = {
        asg_name: {
            'hosts': hosts,
            'vars': {}
        },
        '_meta': {
            'hostvars': {}
        }
    }

    print(json.dumps(inventory, indent=2))

if __name__ == "__main__":
    main()



# chmod +x inventory_scripts/aws_autocaling_group.py.py
# ansible-playbook -i inventory_scripts/aws_autocaling_group.py.py your_playbook.yml

