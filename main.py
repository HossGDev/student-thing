import os


def clear_screen():
    os.system("clear" if os.name != "nt" else "cls")


def show_choices(options):
    for i, option in enumerate(options, 1):
        print(f"{i}. {option}")
    print()


def get_choice(max_num):
    while True:
        try:
            choice = int(input(f"Enter your choice (1-{max_num}): "))
            if 1 <= choice <= max_num:
                return choice
            print(f"Please enter a number between 1 and {max_num}")
        except ValueError:
            print("Please enter a valid number")


def scenario_sorting():
    clear_screen()
    print("=" * 60)
    print("SCENARIO 1: Sorting a List")
    print("=" * 60)
    print("\nYou have a list of names:")
    print("names = ['Charlie', 'Alice', 'Bob', 'Diana']\n")
    print("You want to sort them alphabetically.\n")
    print("LEVEL 1: Choose the correct method\n")
    show_choices(["names.sort()", "names.arrange()", "names.order()", "sort(names)"])
    choice = get_choice(4)
    if choice == 1:
        print("\n✓ Correct! names.sort() sorts the list in place.\n")
    else:
        print("\n✗ Not quite. The correct answer is names.sort()\n")
    input("Press Enter to continue...")

    clear_screen()
    print("LEVEL 2: Complete the code\n")
    print("names = ['Charlie', 'Alice', 'Bob', 'Diana']")
    print("names.______()\n")
    show_choices(["sort", "sorted", "arrange"])
    choice = get_choice(3)
    if choice == 1:
        print("\n✓ Correct!\n")
    else:
        print("\n✗ The answer is 'sort'\n")
    input("Press Enter to continue...")

    clear_screen()
    print("LEVEL 3: Write the complete line\n")
    print("You have: names = ['Charlie', 'Alice', 'Bob', 'Diana']")
    print("Write the line to sort it (hint: use .sort() method)\n")
    answer = input("Your code: ").strip()
    if "sort()" in answer and "names" in answer:
        print("\n✓ Great job!\n")
    else:
        print("\n✗ The answer is: names.sort()\n")
    input("Press Enter to continue...")


def scenario_loops():
    clear_screen()
    print("=" * 60)
    print("SCENARIO 2: Looping Through a List")
    print("=" * 60)
    print("\nYou have: numbers = [1, 2, 3, 4, 5]")
    print("You want to print each number.\n")
    print("LEVEL 1: Choose the correct loop structure\n")
    show_choices(
        [
            "for num in numbers:",
            "for numbers in num:",
            "loop num in numbers:",
            "each num in numbers:",
        ]
    )
    choice = get_choice(4)
    if choice == 1:
        print("\n✓ Correct! 'for num in numbers:' iterates through each item.\n")
    else:
        print("\n✗ The correct answer is: for num in numbers:\n")
    input("Press Enter to continue...")

    clear_screen()
    print("LEVEL 2: Complete the code\n")
    print("numbers = [1, 2, 3, 4, 5]")
    print("___ num ___ numbers:")
    print("    print(num)\n")
    show_choices(["for ... in", "while ... in", "loop ... through"])
    choice = get_choice(3)
    if choice == 1:
        print("\n✓ Correct!\n")
    else:
        print("\n✗ The answer is 'for ... in'\n")
    input("Press Enter to continue...")

    clear_screen()
    print("LEVEL 3: Write the complete loop\n")
    print("numbers = [1, 2, 3, 4, 5]")
    print("Write a for loop to print each number\n")
    line1 = input("Line 1: ").strip()
    line2 = input("Line 2 (indented): ").strip()
    if "for" in line1 and "in numbers" in line1 and "print" in line2:
        print("\n✓ Excellent work!\n")
    else:
        print("\n✗ The answer is:")
        print("for num in numbers:")
        print("    print(num)\n")
    input("Press Enter to continue...")


def scenario_conditionals():
    clear_screen()
    print("=" * 60)
    print("SCENARIO 3: If Statements")
    print("=" * 60)
    print("\nYou want to check if a number is positive.\n")
    print("x = 10\n")
    print("LEVEL 1: Choose the correct if statement\n")
    show_choices(["if x > 0:", "if x => 0:", "if (x positive):", "if x is positive:"])
    choice = get_choice(4)
    if choice == 1:
        print("\n✓ Correct! 'if x > 0:' checks if x is greater than 0.\n")
    else:
        print("\n✗ The correct answer is: if x > 0:\n")
    input("Press Enter to continue...")

    clear_screen()
    print("LEVEL 2: Complete the condition\n")
    print("x = 10")
    print("if x ___ 0:")
    print("    print('Positive')\n")
    show_choices([">", "<", "=="])
    choice = get_choice(3)
    if choice == 1:
        print("\n✓ Correct!\n")
    else:
        print("\n✗ The answer is '>'\n")
    input("Press Enter to continue...")

    clear_screen()
    print("LEVEL 3: Write the complete if statement\n")
    print("x = 10")
    print("Write code to print 'Positive' if x is greater than 0\n")
    line1 = input("Line 1: ").strip()
    line2 = input("Line 2 (indented): ").strip()
    if "if" in line1 and ">" in line1 and "0" in line1 and "print" in line2:
        print("\n✓ Perfect!\n")
    else:
        print("\n✗ The answer is:")
        print("if x > 0:")
        print("    print('Positive')\n")
    input("Press Enter to continue...")


def scenario_dictionaries():
    clear_screen()
    print("=" * 60)
    print("SCENARIO 4: Working with Dictionaries")
    print("=" * 60)
    print("\nYou have a dictionary:")
    print("person = {'name': 'Alice', 'age': 30}")
    print("You want to get the age value.\n")
    print("LEVEL 1: Choose the correct way to access 'age'\n")
    show_choices(["person['age']", "person.age", "person('age')", "person->age"])
    choice = get_choice(4)
    if choice == 1:
        print("\n✓ Correct! Use square brackets with the key name.\n")
    else:
        print("\n✗ The correct answer is: person['age']\n")
    input("Press Enter to continue...")

    clear_screen()
    print("LEVEL 2: Complete the code\n")
    print("person = {'name': 'Alice', 'age': 30}")
    print("age_value = person[____]\n")
    show_choices(["'age'", "age", '"age"'])
    choice = get_choice(3)
    if choice in [1, 3]:
        print("\n✓ Correct!\n")
    else:
        print("\n✗ The answer is 'age' (with quotes)\n")
    input("Press Enter to continue...")

    clear_screen()
    print("LEVEL 3: Write the complete line\n")
    print("person = {'name': 'Alice', 'age': 30}")
    print("Write code to get the age and store it in 'age_value'\n")
    answer = input("Your code: ").strip()
    if "person[" in answer and "age" in answer and "age_value" in answer:
        print("\n✓ Awesome!\n")
    else:
        print("\n✗ The answer is: age_value = person['age']\n")
    input("Press Enter to continue...")


def scenario_functions():
    clear_screen()
    print("=" * 60)
    print("SCENARIO 5: Creating a Function")
    print("=" * 60)
    print("\nYou want to create a function that adds two numbers.\n")
    print("LEVEL 1: Choose the correct function definition\n")
    show_choices(
        ["def add(a, b):", "function add(a, b):", "def add[a, b]:", "create add(a, b):"]
    )
    choice = get_choice(4)
    if choice == 1:
        print("\n✓ Correct! Functions start with 'def' in Python.\n")
    else:
        print("\n✗ The correct answer is: def add(a, b):\n")
    input("Press Enter to continue...")

    clear_screen()
    print("LEVEL 2: Complete the function body\n")
    print("def add(a, b):")
    print("    ______ a + b\n")
    show_choices(["return", "give", "output"])
    choice = get_choice(3)
    if choice == 1:
        print("\n✓ Correct!\n")
    else:
        print("\n✗ The answer is 'return'\n")
    input("Press Enter to continue...")

    clear_screen()
    print("LEVEL 3: Write the complete function\n")
    print("Create a function 'add' that takes two parameters and returns their sum\n")
    line1 = input("Line 1: ").strip()
    line2 = input("Line 2 (indented): ").strip()
    if "def add" in line1 and "return" in line2 and "+" in line2:
        print("\n✓ Fantastic!\n")
    else:
        print("\n✗ The answer is:")
        print("def add(a, b):")
        print("    return a + b\n")
    input("Press Enter to continue...")


def scenario_list_methods():
    clear_screen()
    print("=" * 60)
    print("SCENARIO 6: List Methods")
    print("=" * 60)
    print("\nYou have: fruits = ['apple', 'banana']")
    print("You want to add 'orange' to the end.\n")
    print("LEVEL 1: Choose the correct method\n")
    show_choices(
        [
            "fruits.append('orange')",
            "fruits.add('orange')",
            "fruits.insert('orange')",
            "fruits.push('orange')",
        ]
    )
    choice = get_choice(4)
    if choice == 1:
        print("\n✓ Correct! append() adds to the end of a list.\n")
    else:
        print("\n✗ The correct answer is: fruits.append('orange')\n")
    input("Press Enter to continue...")

    clear_screen()
    print("LEVEL 2: Complete the code\n")
    print("fruits = ['apple', 'banana']")
    print("fruits.______('orange')\n")
    show_choices(["append", "add", "push"])
    choice = get_choice(3)
    if choice == 1:
        print("\n✓ Correct!\n")
    else:
        print("\n✗ The answer is 'append'\n")
    input("Press Enter to continue...")

    clear_screen()
    print("LEVEL 3: Write the complete line\n")
    print("fruits = ['apple', 'banana']")
    print("Add 'orange' to the end of the list\n")
    answer = input("Your code: ").strip()
    if "append" in answer and "orange" in answer:
        print("\n✓ Great!\n")
    else:
        print("\n✗ The answer is: fruits.append('orange')\n")
    input("Press Enter to continue...")


def scenario_string_methods():
    clear_screen()
    print("=" * 60)
    print("SCENARIO 7: String Methods")
    print("=" * 60)
    print("\nYou have: text = 'hello world'")
    print("You want to make it uppercase.\n")
    print("LEVEL 1: Choose the correct method\n")
    show_choices(
        ["text.upper()", "text.uppercase()", "text.toUpper()", "uppercase(text)"]
    )
    choice = get_choice(4)
    if choice == 1:
        print("\n✓ Correct! .upper() converts to uppercase.\n")
    else:
        print("\n✗ The correct answer is: text.upper()\n")
    input("Press Enter to continue...")

    clear_screen()
    print("LEVEL 2: Complete the code\n")
    print("text = 'hello world'")
    print("result = text.______()\n")
    show_choices(["upper", "capitalize", "toupper"])
    choice = get_choice(3)
    if choice == 1:
        print("\n✓ Correct!\n")
    else:
        print("\n✗ The answer is 'upper'\n")
    input("Press Enter to continue...")

    clear_screen()
    print("LEVEL 3: Write the complete line\n")
    print("text = 'hello world'")
    print("Convert text to uppercase and store in 'result'\n")
    answer = input("Your code: ").strip()
    if "upper()" in answer and "result" in answer:
        print("\n✓ Perfect!\n")
    else:
        print("\n✗ The answer is: result = text.upper()\n")
    input("Press Enter to continue...")


def scenario_while_loops():
    clear_screen()
    print("=" * 60)
    print("SCENARIO 8: While Loops")
    print("=" * 60)
    print("\nYou want to count from 0 to 4.\n")
    print("LEVEL 1: Choose the correct while loop\n")
    show_choices(
        [
            "while count < 5:",
            "while count <= 4:",
            "while (count < 5)",
            "Both option 1 and 2 are correct",
        ]
    )
    choice = get_choice(4)
    if choice == 4:
        print("\n✓ Correct! Both work the same way.\n")
    else:
        print("\n✗ Both option 1 and 2 are correct!\n")
    input("Press Enter to continue...")

    clear_screen()
    print("LEVEL 2: Complete the code\n")
    print("count = 0")
    print("_____ count < 5:")
    print("    print(count)")
    print("    count += 1\n")
    show_choices(["while", "for", "loop"])
    choice = get_choice(3)
    if choice == 1:
        print("\n✓ Correct!\n")
    else:
        print("\n✗ The answer is 'while'\n")
    input("Press Enter to continue...")

    clear_screen()
    print("LEVEL 3: Write the complete loop\n")
    print("Write a while loop that prints numbers 0 to 4\n")
    print("(Start with count = 0)\n")
    line1 = input("Line 1: ").strip()
    line2 = input("Line 2: ").strip()
    line3 = input("Line 3: ").strip()
    line4 = input("Line 4: ").strip()
    if "count = 0" in line1 and "while" in line2 and "print" in line3 and "+=" in line4:
        print("\n✓ Excellent!\n")
    else:
        print("\n✗ The answer is:")
        print("count = 0")
        print("while count < 5:")
        print("    print(count)")
        print("    count += 1\n")
    input("Press Enter to continue...")


def scenario_list_comprehension():
    clear_screen()
    print("=" * 60)
    print("SCENARIO 9: List Comprehensions")
    print("=" * 60)
    print("\nYou want to create a list of squares: [0, 1, 4, 9, 16]\n")
    print("LEVEL 1: Choose the correct list comprehension\n")
    show_choices(
        [
            "[x**2 for x in range(5)]",
            "[x*2 for x in range(5)]",
            "[x^2 for x in range(5)]",
            "[square(x) for x in range(5)]",
        ]
    )
    choice = get_choice(4)
    if choice == 1:
        print("\n✓ Correct! ** is the exponent operator.\n")
    else:
        print("\n✗ The correct answer is: [x**2 for x in range(5)]\n")
    input("Press Enter to continue...")

    clear_screen()
    print("LEVEL 2: Complete the code\n")
    print("squares = [x___ for x in range(5)]\n")
    print("What goes in the blank to square each number?\n")
    show_choices(["**2", "*2", "^2"])
    choice = get_choice(3)
    if choice == 1:
        print("\n✓ Correct!\n")
    else:
        print("\n✗ The answer is '**2'\n")
    input("Press Enter to continue...")

    clear_screen()
    print("LEVEL 3: Write the complete list comprehension\n")
    print("Create a list of squares from 0 to 4 and store in 'squares'\n")
    answer = input("Your code: ").strip()
    if "**2" in answer and "for x in range(5)" in answer and "squares" in answer:
        print("\n✓ Amazing!\n")
    else:
        print("\n✗ The answer is: squares = [x**2 for x in range(5)]\n")
    input("Press Enter to continue...")


def scenario_try_except():
    clear_screen()
    print("=" * 60)
    print("SCENARIO 10: Try-Except (Error Handling)")
    print("=" * 60)
    print("\nYou want to safely convert user input to an integer.\n")
    print("LEVEL 1: Choose the correct structure\n")
    show_choices(
        [
            "try: ... except ValueError:",
            "try: ... catch ValueError:",
            "attempt: ... error ValueError:",
            "try: ... except:",
        ]
    )
    choice = get_choice(4)
    if choice == 1:
        print("\n✓ Correct! Use try-except with specific error types.\n")
    else:
        print("\n✗ The correct answer is: try: ... except ValueError:\n")
    input("Press Enter to continue...")

    clear_screen()
    print("LEVEL 2: Complete the code\n")
    print("___:")
    print("    num = int(input('Enter number: '))")
    print("______ ValueError:")
    print("    print('Not a valid number')\n")
    show_choices(["try ... except", "attempt ... error", "try ... catch"])
    choice = get_choice(3)
    if choice == 1:
        print("\n✓ Correct!\n")
    else:
        print("\n✗ The answer is 'try ... except'\n")
    input("Press Enter to continue...")

    clear_screen()
    print("LEVEL 3: Write the complete try-except\n")
    print("Safely convert input to int, print 'Invalid' if it fails\n")
    line1 = input("Line 1: ").strip()
    line2 = input("Line 2 (indented): ").strip()
    line3 = input("Line 3: ").strip()
    line4 = input("Line 4 (indented): ").strip()
    if "try" in line1 and "int(" in line2 and "except" in line3 and "print" in line4:
        print("\n✓ Well done!\n")
    else:
        print("\n✗ The answer is:")
        print("try:")
        print("    num = int(input('Enter number: '))")
        print("except ValueError:")
        print("    print('Invalid')\n")
    input("Press Enter to continue...")


def scenario_nested_loops():
    clear_screen()
    print("=" * 60)
    print("SCENARIO 11: Nested Loops")
    print("=" * 60)
    print("\nYou want to print a 3x3 grid of asterisks:\n")
    print("* * *")
    print("* * *")
    print("* * *\n")
    print("LEVEL 1: Choose the correct nested loop structure\n")
    show_choices(
        [
            "Nested for loops (for i in range(3): ...)",
            "One for loop (for i in range(3): ...)",
            "A single print statement",
            "A while loop count < 9",
        ]
    )
    choice = get_choice(4)
    if choice == 1:
        print("\n✓ Correct! Nested loops for rows and columns.\n")
    else:
        print("\n✗ The correct answer uses nested loops (option 1)\n")
    input("Press Enter to continue...")

    clear_screen()
    print("LEVEL 2: Complete the code\n")
    print("for i in range(3):")
    print("    for j in range(3):")
    print("        print('*', ___=' ')")
    print("    print()  # new line\n")
    show_choices(["end", "sep", "join"])
    choice = get_choice(3)
    if choice == 1:
        print("\n✓ Correct! end=' ' keeps printing on same line.\n")
    else:
        print("\n✗ The answer is 'end'\n")
    input("Press Enter to continue...")

    clear_screen()
    print("LEVEL 3: Write the complete nested loop\n")
    print("Print a 3x3 grid of asterisks with spaces between them\n")
    line1 = input("Line 1: ").strip()
    line2 = input("Line 2 (indented): ").strip()
    line3 = input("Line 3 (double indented): ").strip()
    line4 = input("Line 4 (indented): ").strip()
    if "for" in line1 and "for" in line2 and "print" in line3 and "print()" in line4:
        print("\n✓ Great job!\n")
    else:
        print("\n✗ The answer is:")
        print("for i in range(3):")
        print("    for j in range(3):")
        print("        print('*', end=' ')")
        print("    print()\n")
    input("Press Enter to continue...")


def scenario_classes():
    clear_screen()
    print("=" * 60)
    print("SCENARIO 12: Classes (Basic OOP)")
    print("=" * 60)
    print("\nYou want to create a Dog class with a name attribute.\n")
    print("LEVEL 1: Choose the correct class definition\n")
    show_choices(["class Dog:", "def Dog:", "create Dog:", "Dog class:"])
    choice = get_choice(4)
    if choice == 1:
        print("\n✓ Correct! Classes start with 'class' keyword.\n")
    else:
        print("\n✗ The correct answer is: class Dog:\n")
    input("Press Enter to continue...")

    clear_screen()
    print("LEVEL 2: Complete the __init__ method\n")
    print("class Dog:")
    print("    def ______(self, name):")
    print("        self.name = name\n")
    show_choices(["__init__", "init", "constructor"])
    choice = get_choice(3)
    if choice == 1:
        print("\n✓ Correct! __init__ is the constructor method.\n")
    else:
        print("\n✗ The answer is '__init__'\n")
    input("Press Enter to continue...")

    clear_screen()
    print("LEVEL 3: Write the complete class\n")
    print("Create a Dog class with __init__ that takes a name parameter\n")
    line1 = input("Line 1: ").strip()
    line2 = input("Line 2 (indented): ").strip()
    line3 = input("Line 3 (double indented): ").strip()
    if "class Dog" in line1 and "__init__" in line2 and "self.name" in line3:
        print("\n✓ Excellent!\n")
    else:
        print("\n✗ The answer is:")
        print("class Dog:")
        print("    def __init__(self, name):")
        print("        self.name = name\n")
    input("Press Enter to continue...")


def scenario_lambda():
    clear_screen()
    print("=" * 60)
    print("SCENARIO 13: Lambda Functions")
    print("=" * 60)
    print("\nYou want to create a function that doubles a number.\n")
    print("LEVEL 1: Choose the correct lambda function\n")
    show_choices(
        ["lambda x: x * 2", "lambda(x): x * 2", "def lambda x: x * 2", "x => x * 2"]
    )
    choice = get_choice(4)
    if choice == 1:
        print("\n✓ Correct! lambda parameter: expression\n")
    else:
        print("\n✗ The correct answer is: lambda x: x * 2\n")
    input("Press Enter to continue...")

    clear_screen()
    print("LEVEL 2: Complete the code\n")
    print("double = ______ x: x * 2\n")
    show_choices(["lambda", "function", "def"])
    choice = get_choice(3)
    if choice == 1:
        print("\n✓ Correct!\n")
    else:
        print("\n✗ The answer is 'lambda'\n")
    input("Press Enter to continue...")

    clear_screen()
    print("LEVEL 3: Write the complete lambda\n")
    print("Create a lambda that doubles a number and store it in 'double'\n")
    answer = input("Your code: ").strip()
    if "lambda" in answer and "x * 2" in answer and "double" in answer:
        print("\n✓ Perfect!\n")
    else:
        print("\n✗ The answer is: double = lambda x: x * 2\n")
    input("Press Enter to continue...")


def scenario_recursion():
    clear_screen()
    print("=" * 60)
    print("SCENARIO 14: Recursion Basics")
    print("=" * 60)
    print("\nYou want to calculate factorial (5! = 5*4*3*2*1 = 120)\n")
    print("LEVEL 1: Choose the correct recursive function\n")
    show_choices(
        [
            "def factorial(n): return 1 if n == 0 else n * factorial(n-1)",
            "def factorial(n): return n * factorial(n)",
            "def factorial(n): return n * n-1",
            "def factorial(n): while n > 0: return n * factorial(n-1)",
        ]
    )
    choice = get_choice(4)
    if choice == 1:
        print("\n✓ Correct! Base case and recursive case.\n")
    else:
        print("\n✗ Option 1 is correct - needs base case!\n")
    input("Press Enter to continue...")

    clear_screen()
    print("LEVEL 2: Complete the base case\n")
    print("def factorial(n):")
    print("    if n == 0:")
    print("        return ___")
    print("    return n * factorial(n-1)\n")
    show_choices(["1", "0", "n"])
    choice = get_choice(3)
    if choice == 1:
        print("\n✓ Correct! 0! = 1 by definition.\n")
    else:
        print("\n✗ The answer is '1'\n")
    input("Press Enter to continue...")

    clear_screen()
    print("LEVEL 3: Write the complete recursive function\n")
    print("Write factorial function with base case and recursive case\n")
    line1 = input("Line 1: ").strip()
    line2 = input("Line 2 (indented): ").strip()
    line3 = input("Line 3 (double indented): ").strip()
    line4 = input("Line 4 (indented): ").strip()
    if (
        "def factorial" in line1
        and "if" in line2
        and "return" in line3
        and "factorial(n-1)" in line4
    ):
        print("\n✓ Outstanding!\n")
    else:
        print("\n✗ The answer is:")
        print("def factorial(n):")
        print("    if n == 0:")
        print("        return 1")
        print("    return n * factorial(n-1)\n")
    input("Press Enter to continue...")


def scenario_big_o_intro():
    clear_screen()
    print("=" * 60)
    print("SCENARIO 15: Big O Notation - Introduction")
    print("=" * 60)
    print("\nBig O describes how code performance scales with input size.\n")
    print("Let's learn the basics!\n")
    print("LEVEL 1: What does O(1) mean?\n")
    show_choices(
        [
            "Constant time - same speed regardless of input size",
            "Linear time - doubles with input size",
            "One operation only",
            "Fastest possible algorithm",
        ]
    )
    choice = get_choice(4)
    if choice == 1:
        print("\n✓ Correct! O(1) means constant time.\n")
        print("Example: accessing an array element by index")
        print("arr[5] takes the same time whether arr has 10 or 10,000 items!\n")
    else:
        print("\n✗ O(1) means constant time - always same speed.\n")
    input("Press Enter to continue...")

    clear_screen()
    print("LEVEL 2: Identify the time complexity\n")
    print("def get_first(arr):")
    print("    return arr[0]\n")
    print("What's the time complexity?\n")
    show_choices(["O(1) - Constant", "O(n) - Linear", "O(n²) - Quadratic"])
    choice = get_choice(3)
    if choice == 1:
        print("\n✓ Correct! It's O(1) - always one operation.\n")
    else:
        print("\n✗ It's O(1) - accessing first element is constant time.\n")
    input("Press Enter to continue...")

    clear_screen()
    print("LEVEL 3: Write a function with O(1) complexity\n")
    print("Write a function that returns the last element of a list\n")
    print("(Hint: use negative indexing like arr[-1])\n")
    line1 = input("Line 1: ").strip()
    line2 = input("Line 2 (indented): ").strip()
    if "def" in line1 and "return" in line2 and "[-1]" in line2:
        print("\n✓ Perfect! That's O(1) constant time!\n")
    else:
        print("\n✗ The answer is:")
        print("def get_last(arr):")
        print("    return arr[-1]\n")
    input("Press Enter to continue...")


def scenario_big_o_linear():
    clear_screen()
    print("=" * 60)
    print("SCENARIO 16: Big O - O(n) Linear Time")
    print("=" * 60)
    print("\nO(n) means time grows linearly with input size.\n")
    print("If input doubles, time doubles.\n")
    print("LEVEL 1: Which has O(n) complexity?\n")
    show_choices(
        [
            "Looping through an array once",
            "Accessing array[0]",
            "Nested loops",
            "Binary search",
        ]
    )
    choice = get_choice(4)
    if choice == 1:
        print("\n✓ Correct! One loop = O(n).\n")
        print("Example:")
        print("for item in arr:")
        print("    print(item)")
        print("Touches each element once!\n")
    else:
        print("\n✗ Looping through entire array is O(n).\n")
    input("Press Enter to continue...")

    clear_screen()
    print("LEVEL 2: Identify the time complexity\n")
    print("def find_max(arr):")
    print("    max_val = arr[0]")
    print("    for num in arr:")
    print("        if num > max_val:")
    print("            max_val = num")
    print("    return max_val\n")
    print("What's the time complexity?\n")
    show_choices(["O(n) - Linear", "O(1) - Constant", "O(n²) - Quadratic"])
    choice = get_choice(3)
    if choice == 1:
        print("\n✓ Correct! One loop through n elements = O(n).\n")
    else:
        print("\n✗ It's O(n) - we check each element once.\n")
    input("Press Enter to continue...")

    clear_screen()
    print("LEVEL 3: Write an O(n) function\n")
    print("Write a function that sums all numbers in a list\n")
    line1 = input("Line 1: ").strip()
    line2 = input("Line 2 (indented): ").strip()
    line3 = input("Line 3 (indented): ").strip()
    _ = input("Line 4 (double indented): ").strip()
    line5 = input("Line 5 (indented): ").strip()
    if (
        "def" in line1
        and ("total = 0" in line2 or "total=0" in line2)
        and "for" in line3
        and "return" in line5
    ):
        print("\n✓ Great! That's O(n) - one pass through the list!\n")
    else:
        print("\n✗ The answer is:")
        print("def sum_list(arr):")
        print("    total = 0")
        print("    for num in arr:")
        print("        total += num")
        print("    return total\n")
    input("Press Enter to continue...")


def scenario_big_o_quadratic():
    clear_screen()
    print("=" * 60)
    print("SCENARIO 17: Big O - O(n²) Quadratic Time")
    print("=" * 60)
    print("\nO(n²) means nested loops - for each of n items, do n operations.\n")
    print("If input doubles, time quadruples!\n")
    print("LEVEL 1: Which has O(n²) complexity?\n")
    show_choices(
        [
            "Nested loops iterating through same array",
            "One loop through array",
            "Two separate loops",
            "Accessing array element",
        ]
    )
    choice = get_choice(4)
    if choice == 1:
        print("\n✓ Correct! Nested loops = O(n²).\n")
        print("Example:")
        print("for i in arr:")
        print("    for j in arr:")
        print("        print(i, j)")
        print("For array of 10, that's 100 operations!\n")
    else:
        print("\n✗ Nested loops give O(n²) complexity.\n")
    input("Press Enter to continue...")

    clear_screen()
    print("LEVEL 2: Identify the time complexity\n")
    print("def print_pairs(arr):")
    print("    for i in arr:")
    print("        for j in arr:")
    print("            print(i, j)\n")
    print("What's the time complexity?\n")
    print("O(n²) - Quadratic", "O(n) - Linear", "O(2n) - Linear")
    choice = get_choice(3)
    if choice == 1:
        print("\n✓ Correct! Nested loops = O(n²).\n")
        print("Note: O(2n) simplifies to O(n), but this is nested so O(n²)\n")
    else:
        print("\n✗ It's O(n²) - nested loops multiply!\n")
    input("Press Enter to continue...")

    clear_screen()
    print("LEVEL 3: Compare time complexities\n")
    print("You have 1000 items. Estimate operations for each:\n")
    print("A) O(1): ___")
    print("B) O(n): ___")
    print("C) O(n²): ___\n")
    a = input("A) O(1): ").strip()
    b = input("B) O(n): ").strip()
    c = input("C) O(n²): ").strip()
    if a == "1" and b == "1000" and c == "1000000":
        print("\n✓ Perfect understanding!")
        print("O(1) = 1, O(n) = 1,000, O(n²) = 1,000,000\n")
    else:
        print("\n✗ The answers are:")
        print("O(1) = 1 operation")
        print("O(n) = 1,000 operations")
        print("O(n²) = 1,000,000 operations!\n")
    input("Press Enter to continue...")


def scenario_big_o_practice():
    clear_screen()
    print("=" * 60)
    print("SCENARIO 18: Big O - Practice & Review")
    print("=" * 60)
    print("\nLet's practice identifying Big O complexity!\n")
    print("LEVEL 1: What's the complexity?\n")
    print("def example(arr):")
    print("    print(arr[0])")
    print("    for item in arr:")
    print("        print(item)\n")
    show_choices(
        [
            "O(n) - the loop dominates",
            "O(1) - just two operations",
            "O(n²) - loop with access",
        ]
    )
    choice = get_choice(3)
    if choice == 1:
        print("\n✓ Correct! O(1) + O(n) = O(n).\n")
        print("We drop constants and take the dominant term!\n")
    else:
        print("\n✗ It's O(n) - the loop is the dominant operation.\n")
    input("Press Enter to continue...")

    clear_screen()
    print("LEVEL 2: Identify the complexity\n")
    print("def example(arr):")
    print("    for i in arr:")
    print("        print(i)")
    print("    for j in arr:")
    print("        print(j)\n")
    print("What's the time complexity?\n")
    show_choices(
        [
            "O(n) - two loops don't nest",
            "O(2n) - two separate loops",
            "O(n²) - two loops total",
        ]
    )
    choice = get_choice(3)
    if choice == 1:
        print("\n✓ Correct! O(n) + O(n) = O(2n) = O(n).\n")
        print("We drop constants in Big O notation!\n")
    else:
        print("\n✗ It's O(n) - sequential loops add, not multiply.\n")
        print("We simplify O(2n) to O(n).\n")
    input("Press Enter to continue...")

    clear_screen()
    print("LEVEL 3: Calculate Big O for your own code\n")
    print("Write a function that checks if a list contains duplicates")
    print("(Hint: use nested loops to compare each pair)\n")
    _ = input("Line 1: ").strip()
    print("(Type 'skip' for remaining lines to see answer)\n")
    line2 = input("Line 2: ").strip()
    if "skip" not in line2.lower():
        _ = input("Line 3: ").strip()
        _ = input("Line 4: ").strip()
        _ = input("Line 5: ").strip()
    print("\n✓ Here's one solution:")
    print("def has_duplicates(arr):")
    print("    for i in range(len(arr)):")
    print("        for j in range(i+1, len(arr)):")
    print("            if arr[i] == arr[j]:")
    print("                return True")
    print("    return False")
    print("\nThis is O(n²) - nested loops!\n")
    print("Note: Using a set would be O(n) - much faster!")
    print("duplicates = len(arr) != len(set(arr))\n")
    input("Press Enter to continue...")


def main():
    scenarios = [
        ("1. Sorting a List", scenario_sorting),
        ("2. Looping Through a List", scenario_loops),
        ("3. If Statements", scenario_conditionals),
        ("4. Working with Dictionaries", scenario_dictionaries),
        ("5. Creating Functions", scenario_functions),
        ("6. List Methods", scenario_list_methods),
        ("7. String Methods", scenario_string_methods),
        ("8. While Loops", scenario_while_loops),
        ("9. List Comprehensions", scenario_list_comprehension),
        ("10. Try-Except", scenario_try_except),
        ("11. Nested Loops", scenario_nested_loops),
        ("12. Classes (OOP)", scenario_classes),
        ("13. Lambda Functions", scenario_lambda),
        ("14. Recursion Basics", scenario_recursion),
        ("15. Big O - Introduction", scenario_big_o_intro),
        ("16. Big O - O(n) Linear", scenario_big_o_linear),
        ("17. Big O - O(n²) Quadratic", scenario_big_o_quadratic),
        ("18. Big O - Practice", scenario_big_o_practice),
    ]

    while True:
        clear_screen()
        print("=" * 60)
        print("PYTHON LEARNING TOOL - From Basics to Big O!")
        print("=" * 60)
        print("\nSelect a scenario to practice:\n")
        for name, _ in scenarios:
            print(name)
        print(f"{len(scenarios) + 1}. Exit\n")
        choice = get_choice(len(scenarios) + 1)
        if choice == len(scenarios) + 1:
            print("\n🎉 Great work! Keep practicing and happy coding! 🎉")
            break
        scenarios[choice - 1][1]()


if __name__ == "__main__":
    main()
