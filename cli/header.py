from pyfiglet import print_figlet
from termcolor import colored


def header():
    print_figlet("SHSH2", font="slant")

    print(colored("AutoBlobSaver - v0.1.0a", attrs=["bold"]))
    print("Saving SHSH2 Blobs automatically - Made by fxrcha with love")
    print()
