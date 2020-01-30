# https://docker-py.readthedocs.io/en/stable/images.html

from client_config import client

img = client.images


def remove_images(obj, lst, force=False):
    for i in lst:
        r = obj.remove(i.id, force=force)
        print(r)


if __name__ == "__main__":
    # img.pull('nginx')
    lst = img.list()  # name='ubuntu')
    print(lst)
    # res = img.prune()
    # print(res)

    remove_images(img, lst, force=True)
