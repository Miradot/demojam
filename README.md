# Devnet Demo Jam

## Prerequisites

* Cisco MSO
* Cisco ACI
* Cisco ACI Cloud Apic (AWS)
* Self-hosted Gitlab
* Self-hosted Netbox
* Self-hosted Linux DHCP (isc-dhcp-server)
* VMware
* AWS (free tier account possible)
* Python3 on local machine
* Git on local machine

## Installation

```
pip install -r requirements.txt
add a secret to ansible/.vault_pass.txt
enter settings to setup.yml (can be removed later, see example file located in same folder for help)
python setup.py
setup.yml can now be removed
enter customer settings to ansible/vars_files/customers.yml (see example file located in same folder for help)
```

## Usage

```
Create a project in Gitlab  
  CI/CD variables needed:  
    - ANSIBLE_VAULT_PASSWORD ; password in ansible/.vault_pass.txt
    - CI_PUSH_TOKEN ; User settings > Access Tokens > Choose a Name and check "write_repository"
    - CI_PUSH_USER ; $gitlab_user
    - CI_PUSH_URL ; $gitlab_fqdn / ip
    - CI_PROJECT_NAME ; $project_name

git clone $project_url
cp -r demojam $your_folder
cd $your_folder
git add .
git commit -m "demojam"
git push
```

## What the playbook does

Based on variables in ansible/vars_files/customers.yml

1) Reservs prefix in netbox
2) Writes down the prefix to customers.yml
3) Configures DHCP
4) Configures MSO; Tenant, Schema, Template, Contracts for external access
5) Configures ACI; dhcp-relay
6) Clones and configures VM(s) in VMware
7) Configures VM(s) in AWS

## End goal

* AWS and VMware VM will be able to communicate freely.
* AWS VM is publicly available if chosen based on L3-Rules created in Cisco MSO. 
* Cloud (AWS) workload and on-prem (VMware) workload able to use the same security policies due to the use of Cisco MSO.
* Cisco ACI handles the creation of on-prem network (even on VMware).
* Cisco Cloud APIC handles the creation of AWS networks.
* With the help of Cisco MSO all rules and networks are created on the same place and pushed to on-prem and cloud.

## Getting help

If you have questions, concerns, bug reports, etc., please create an issue against this repository.

## Getting involved

This project is supposed to work as examples to get started with automation in several areas. If you have any suggestions on what else to include, feel free to reach ut by creating an issue.

## Licensing info

`Copyright (c) 2020, Miradot AB`

This code is licensed under the MIT License. See [LICENSE](./LICENSE) for details.