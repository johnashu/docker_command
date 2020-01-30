# https://docker-py.readthedocs.io/en/stable/nodes.html
from client_config import client

node = client.nodes


def display_nodes(obj, lst):
    for i in lst:
        r = obj.get(i.id)
        name = r.name
        print(s)


if __name__ == "__main__":
    # volumes
    lst = node.list()
    print(lst)
    node.prune()
    display_nodes(node, lst)
