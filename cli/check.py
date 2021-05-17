import platform


def check_os():
    if platform.system() == "Windows":
        return False

    return True
