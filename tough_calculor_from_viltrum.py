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
    print(f"""
{color.CYAN}{color.BOLD}
╔══════════════════════════════════════════╗
║   🧮  SUPER CALCULATOR 3000  🧮          ║
║   Built with OOP + Inheritance (Python)  ║
╚══════════════════════════════════════════╝
{color.RESET}""")
    
# ══════════════════════════════════════════════
#  BASE CLASS — Calculator
# ══════════════════════════════════════════════

class Calculator:
    """
    BASE CLASS (Parent).
 
    Stores num1 and num2, keeps the result, and defines
    the interface that every child class must follow.
 
    `calculate()` raises NotImplementedError by default —
    this forces every subclass to provide its own version.
    This is Python's way of mimicking abstract methods
    without using the `abc` module.
    """

    OPERATION_SYMBOL = "?"   # each child overrides this
 
    def __init__(self, num1: float, num2: float):
        self.num1   = num1
        self.num2   = num2
        self.result = None
