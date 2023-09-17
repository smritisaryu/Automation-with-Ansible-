# Automation-with-Ansible-
Keywords - Flask app, HAProxy, Bastion, SSH, Ansible-playbook, YAML, Python


" site.yaml " is a playbook file that runs the network - automation (HAproxy, Bastion and three back-end servers- devA,devB,devC) and HAproxy loadbalances the backend servers when the service is requested from the Internet.

"haproxy.cfg.j2" -- it is the configuration file of haproxy using jinja2 template for it to communicate with ansible-playbook for loadbalancing
"hosts" -- this file has all hosts specified that are part of the development network


# Provoked by

ansible-playbook -i hosts site.yaml
