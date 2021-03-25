# CloudLabVM

### To run:
* Install Ansible and Ovirt SDK using pip
* Create vault using `ansible-vault create vault.yml` and add IaaS ULL password
* Change variable `ovirt_login` to your account in all playbooks
* Set new `root_password` in the build playbooks
* Change internal IPs of manager and workers as these are taken
* Build manager with `ansible-playbook --ask-vault-pass build_Manager.yaml` and wait for it to reboot
* Build workers with `ansible-playbook --ask-vault-pass build_Workers.yaml`
* Add build_and_run script to manager node with scp for less typing
