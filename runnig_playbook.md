# Run on all hosts defined
ansible-playbook <YAML>                  
# Run 10 hosts parallel
ansible-playbook <YAML> -f 10           
 # Verbose on successful tasks
ansible-playbook <YAML> --verbose        
 # Test run
ansible-playbook <YAML> -C              
 # Dry run
ansible-playbook <YAML> -C -D          
 # Run on single host using -l or -limit ( -l stands for limit )
ansible-playbook <YAML> -l <host>        
e.g. ansible-playbook new_playbook.yml

