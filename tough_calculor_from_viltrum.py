class color:
    RESET = "\033[0m"
    BOLD   = "\033[1m"
    CYAN   = "\033[96m"
    GREEN  = "\033[92m"
    YELLOW = "\033[93m"
    RED    = "\033[91m"
    MAGENTA= "\033[95m"
    BLUE   = "\033[94m"


def banner():
    """print a stylish welcome banner."""
    print(f"{color.CYAN}{color.BOLD}")
    