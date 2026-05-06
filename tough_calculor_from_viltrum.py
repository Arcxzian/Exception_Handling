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

    def calculate(self) -> float:
        """
        MUST be overridden by every subclass.
        Raises NotImplementedError if called directly on base class.
        """
        raise NotImplementedError(
            f"{self.__class__.__name__} must implement calculate()"
        )
 
    def display_result(self):
        """
        Shared method (inherited by ALL subclasses).
        Formats and prints the equation neatly.
        """
        print(f"\n{color.GREEN}{color.BOLD}"
              f"  {self.num1} {self.OPERATION_SYMBOL} {self.num2} = {self.result}"
              f"{color.RESET}\n")
    
   
# CLASS 1 ADDITION
class AddCalculator(Calculator):
    """
    Inherits from Calculator.
    Overrides calculate() to perform addition.
    """
    OPERATION_SYMBOL = "+"

    def calculate(self) -> float:
        self.result = self.num1 + self.num2
        return self.result

#CLASS 2 SUBTRACTION
class SubtractCalculator(Calculator):
    """
    Inherits from Calculator. 
    overrides calculate() to perform subraction.
    """
    OPERATION_SYMBOL = "-"

    def calculate(self) -> float:
        self.result = self.num1 - self.num2
        return self.result

#CLASS 3 MULTIPLICATION
class MultiplyCalculator(Calculator):
    """
    Inherits from Calculator.
    oveerides calculate() to perform Multiplication.
    """
    OPERATION_SYMBOL= "*"

    def calculate(self) -> float:
        self.result = self.num1 * self.num2
        return self.result

# CLASS 4 DIVISION
class DivideCalculator(Calculator):
    """
    Inherits from Calculator.
    Overrides calculate() with EXTRA guard for division by zero.
    Raises ZeroDivisionError so the app can catch and handle it.
    """
      
    OPERATION_SYMBOL = "÷"

    def calculate(self) -> float:
        if self.num2 == 0:
            raise ZeroDivisionError("Cannot Divide by zero!")
        self.result = self.num1 / self.num2
        return self.result
    
# ══════════════════════════════════════════════
#  MANAGER CLASS — CalculatorApp
#  (Controller; uses all 4 subclasses above)
# ══════════════════════════════════════════════

class CalculatorApp:
     """
    Controls the entire user experience:
      - Shows the menu
      - Gets and validates user input (with exceptions)
      - Picks the correct Calculator subclass (factory method)
      - Loops until the user quits
      - Tracks a session history of calculations (bonus feature!)
    """
     MENU = {
         "1": ("Addition",      AddCalculator),
         "2": ("Subtraction",        SubtractCalculator),
         "3": ("Multiplication",        MultiplyCalculator),
         "4": ("Division",      DivideCalculator)
     }
    
def __init__(self):
    self.history = []

    def get_calculator(self, choice: str, num1: float, num2: float) -> Calculator:
        """Returns the correct subclass instance based on menu choice.
        This is the Factory Pattern — one method, many possible objects.
        """
        _, calc_class = self.MENU[choice]
        return calc_class(num1, num2)
    
    def get_operation_choice(self) -> str:
        """Show the operations menu and get a valid choice."""
        print(f"{color.CYAN}{"-"*44}")
        print(f" Choose an operation:")
        for key, (name, _) in self.MENU.items():
            print(f" [{key}] {name}")
        print(f"{'-'*44}{color.RESET}")

        while True:
            choice = input("f{color.YELLOW} Enter choise (1-4): {color.RESET}").strip()
            if choice in self.MENU:
                return choice
            print(f"{color.RED} ⚠ Invalid choice, Please enter 1, 2, 3, or 4 {color.RESET}")

    def get_number(self, prompt: str) -> float:
         """
        Asks the user for a number and keeps asking until valid.
        Catches ValueError when the user types something non-numeric.
        """
         while True:
             try:
                 return float(input(f"{color.YELLOW}    {prompt}:   {color.RESET}"))
             except ValueError:
                 print(f"{color.RED}  ⚠ Thats not a valid number. Try again. {color.RESET}")
                
    def show_history(self):
        """Prints all calculations done in this sesion."""
        if not self.history:
            return
        print(f"\n{color.BLUE}{color.BOLD} Session History:{color.RESET}")
        for i, entry in enumerate(self.history, 1):
            print(f"{color.BLUE} {i}. {entry}{color.RESET}")
