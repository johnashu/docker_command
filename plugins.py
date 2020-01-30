# https://docker-py.readthedocs.io/en/stable/plugins.html
from client_config import client

plugin = client.plugins


def display_plugins(obj, lst):
    for i in lst:
        r = obj.get(i.id)
        name = r.name
        print(s)


if __name__ == "__main__":
    # volumes
    lst = plugin.list()
    print(lst)
    display_plugins(plugin, lst)
