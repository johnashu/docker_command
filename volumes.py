# https://docker-py.readthedocs.io/en/stable/volumes.html

from client_config import client

vol = client.volumes


def remove_volumes(obj, lst, force=False):
    for i in lst:
        r = obj.get(i.id)
        s = r.remove(force=force)
        print(s)


if __name__ == "__main__":
    # volumes
    lst = vol.list()
    print(lst)
    vol.prune()
    remove_volumes(vol, lst, force=True)
