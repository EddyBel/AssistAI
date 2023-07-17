from settings import INTERFACE


if INTERFACE == "ui":
    import ui_interface.main
elif INTERFACE == "terminal":
    import terminal_interface.main

print("Finish tu run")
