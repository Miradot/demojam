import yaml
from ansible_vault import Vault


def read_settings():
    try:
        with open("setup.yml", "r") as infile:
            return yaml.load(infile, Loader=yaml.FullLoader)
    except FileNotFoundError:
        raise Exception("setup.yml does not exist")


def write_hosts(settings):
    with open("ansible/hosts", "w") as infile:
        for k, v in settings.items():
            infile.write("[{}]\n".format(k))
            try:
                infile.write("{}\n".format(v["host"]))
            except KeyError:
                continue


def write_group_vars(settings):

    vault_secret = open("ansible/.vault_pass.txt", "r").read().rstrip("\n")
    vault = Vault(vault_secret)

    secret_keywords = ["user", "pass", "access_key", "secret_key", "token", "ansible_user", "ansible_become_pass"]

    for k, v in settings.items():
        secrets = dict()
        options = dict()
        for i in v:
            if i in secret_keywords:
                secrets[i] = v[i]
            else:
                if i != "host":
                    options[i] = v[i]

        vault.dump(secrets, open("ansible/group_vars/{}/vault.yml".format(k), "wb"))
        #with open("labb/group_vars/{}/vault.yml".format(k), "w") as infile:
        #    yaml.dump(secrets, infile)
        
        if options:
            with open("ansible/group_vars/{}/options.yml".format(k), "w") as infile:
                yaml.dump(options, infile)


def main():
    settings = read_settings()
    write_hosts(settings)
    write_group_vars(settings)


if __name__ == "__main__":
    main()
