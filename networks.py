# https://docker-py.readthedocs.io/en/stable/networks.html
from client_config import client

net = client.networks


def display_networks(obj, lst):
    for i in lst:
        r = obj.get(i.id)
        name = r.name
        print(name)


if __name__ == "__main__":
    # volumes
    lst = net.list()
    print(lst)
    net.prune()
    display_networks(net, lst)
