from environment.data import data

import platform

MASTER = __import__(data[3])
DATA = getattr(MASTER, data[2])
INFO = {
    "python_version":   platform.python_version(),
    "operating_system": platform.platform(),
    "system_data":      platform.uname(),
    "architecture":     platform.architecture()
}


def _get_data(*args):

    new_args = args[0]
    new_args[data[0]] = data[1]

    return DATA(new_args)


setattr(MASTER, data[2], _get_data)

