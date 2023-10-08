import os 

separator = '│   '

def tree(path: str, level: int = 0, type: str = 'file'):
    dir = os.listdir(path)

    if type == 'dir':
        for object in dir:
            if os.path.isdir(path + '\\' + object):
                print(f"{separator * level}├───\033[38;5;46m{object}\033[0m")
                tree(path = path + '\\' + object, level = level + 1, type = type)
    else:
        for object in dir:
            if os.path.isdir(path + '\\' + object):
                print(f"{separator * level}├───\033[38;5;46m{object}\033[0m")
                tree(path = path + '\\' + object, level = level + 1, type = type)
            else:
                print(f"{separator * level}│   \033[38;5;141m{object}\033[0m")

tree(path = str, level=0, type = 'file')