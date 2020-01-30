# https://docker-py.readthedocs.io/en/stable/containers.html

from client_config import client

cons = client.containers


def container_manage(container, stop=False):
    # GET
    container = cons.get(container)

    # ATTRS
    attrs = container.attrs["Config"]["Image"]

    # Logs
    logs = container.logs()

    # stop
    if stop:
        container.stop()


def start_log_stream(container):
    for line in container.logs(stream=True):
        print(line)


def stop_all_containers(con_lst):
    for con in con_lst:
        con.stop()


def remove_containers(obj, lst, force=False):
    for i in lst:
        r = obj.remove(i.id, force=force)
        print(r)


if __name__ == "__main__":
    # cons.run("ubuntu", "echo hello world")
    # run containers in the background:
    # cons.run("bfirsh/reticulate-splines", detach=True)

    # LIst
    con_lst = cons.list()
    print(con_lst)

    remove_containers(cons, con_lst, force=True)
    # start_log_stream(con_lst[0])
    # stop_all_containers(con_lst)
