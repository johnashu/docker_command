# https://docker-py.readthedocs.io/en/stable/services.html
from client_config import client

ser = client.services


def display_services(obj, lst):
    for i in lst:
        r = obj.get(i.id)
        name = r.name
        print(name)


if __name__ == "__main__":
    # volumes
    lst = ser.list()
    print(lst)
    ser.prune()
    display_services(ser, lst)
