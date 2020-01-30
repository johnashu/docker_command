# https://docker-py.readthedocs.io/en/stable/secrets.html
from client_config import client

sec = client.secrets


def display_secrets(obj, lst):
    for i in lst:
        r = obj.get(i.id)
        name = r.name
        print(s)


if __name__ == "__main__":
    # volumes
    lst = sec.list()
    print(lst)
    display_secrets(sec, lst)
