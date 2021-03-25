# CloudLabVM

### To run:
* Install Ansible and Ovirt SDK using pip
* Create vault using `ansible-vault create vault.yml` and add IaaS ULL password
* Change variable `ovirt_login` to your account in all playbooks
* Set new `root_password` in the build playbooks
* Change internal IPs of manager and workers as these are taken 
* Add the same IPs to machines file in manager (edit line 112 in build_Manager.yaml)
* Build manager with `ansible-playbook --ask-vault-pass build_Manager.yaml` and wait for it to reboot
* Build workers with `ansible-playbook --ask-vault-pass build_Workers.yaml`
* Once all nodes are running SSH into all other nodes from manager node once
* Add build_and_run script to cloud directory in manager node with SCP for less typing
* SCP any MPI code into cloud directory in manager node and build and run using `bash build_and_run name_of_binary name_of_code.c`
