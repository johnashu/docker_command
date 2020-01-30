# https://docker-py.readthedocs.io/en/stable/client.html#

# https://docker-py.readthedocs.io/en/stable/configs.html

import docker

client = docker.from_env()


def get_config_info():
    cfg = client.configs.list()
    print(cfg)
    # c = cfg.get(cfg.id)
    # print(c.name)


if __name__ == "__main__":
    get_config_info()
