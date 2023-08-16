from settings import INTERFACE


if INTERFACE == "ui":
    import interface.main
elif INTERFACE == "terminal":
    import cmd.main

print("Finish tu run")
