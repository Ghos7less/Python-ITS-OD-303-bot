import random
import os

questions = {

#1.1:

1: {'question': 'Which of the following is a sequence of characters enclosed in single quotes or double quotes?',
'options': ['Integers', 'Strings', 'Floats', 'Booleans'],
'answer': 'Strings'},
2: {'question': 'What is the data type of the variable "age" in the following code snippet?\nage = 30',
'options': ['String', 'Integer', 'Float', 'Boolean'],
'answer': 'Integer'},
3: {'question': 'What is the data type of the variable "price" in the following code snippet?\nprice = 9.99',
'options': ['String', 'Integer', 'Float', 'Boolean'],
'answer': 'Float'},
4: {'question': 'What is the data type of the variable "is_student" in the following code snippet?\nis_student = True',
'options': ['String', 'Integer', 'Float', 'Boolean'],
'answer': 'Boolean'},
5: {'question': 'Which of the following data types can be used to represent logical values?',
'options': ['String', 'Integer', 'Float', 'Boolean'],
'answer': 'Boolean'},
6: {'question': 'What is the data type of the variable "name" in the following code snippet?\nname = "John Smith"',
'options': ['String', 'Integer', 'Float', 'Boolean'],
'answer': 'String'},
7: {'question': 'Which of the following can be used to store and manipulate numerical data with decimal points?',
'options': ['String', 'Integer', 'Float', 'Boolean'],
'answer': 'Float'},
8: {'question': 'Which of the following can be used to store and manipulate numerical data?',
'options': ['String', 'Integer', 'Float', 'Boolean'],
'answer': 'Integer'},

#1.2:

9: {'question': 'How can you convert a string to an integer in Python?',
'options': ['int()', 'float()', 'str()', 'bool()'],
'answer': 'int()'},
10: {'question': 'What is the output of the following code?\nx = "5"\nx = int(x)\nprint(x)',
'options': [' "5" ', '5', 'Error', 'None'],
'answer': '5'},
11: {'question': 'What is the output of the following code?\nx = [1, 2, 3, 4, 5]\nprint(x[0])',
'options': ['0', '1', '5', 'Error'],
'answer': '1'},
12: {'question': 'What is the output of the following code?\nx = [1, 2, 3, 4, 5]\nprint(x[1:4])',
'options': ['[1, 2, 3]', '[2, 3, 4]', '[4, 5]', 'Error'],
'answer': '[2, 3, 4]'},
13: {'question': 'What is the output of the following code?\nx = [1,2,3,4]\ny = [5,6,7,8]\nz = x + y\nprint(z)',
'options': ['[1,2,3,4,5,6,7,8]', '[2,4,6,8]', '[1,2,3,4]', 'Error'],
'answer': '[1,2,3,4,5,6,7,8]'},
14: {'question': 'What is the output of the following code?\nx = [1,2,3,4]\nx.append(5)\nprint(x)',
'options': ['[1, 2, 3, 4, 5]', '[5]', 'Error', 'None'],
'answer': '[1, 2, 3, 4, 5]'},
15: {'question': 'How can you remove an element from a list?',
'options': ['x.add(element)', 'x.remove(element)', 'x.pop(element)', 'x.delete(element)'],
'answer': 'x.remove(element)'},
16: {'question': 'How can you sort a list in ascending order?',
'options': ['x.sort()', 'x.reverse()', 'x.sort(reverse=True)', 'x.sort(ascending=True)'],
'answer': 'x.sort()'},
17: {'question': 'How can you reverse the elements in a list?',
'options': ['x.sort()', 'x.reverse()', 'x.sort(reverse=True)', 'x.reverse(ascending=True)'],
'answer': 'x.reverse()'},
18: {'question': 'What is the main use of lists in python?',
'options': ['To store multiple items in a single variable', 'To store strings', 'To store integers', 'To store floats'],
'answer': 'To store multiple items in a single variable'},

19: {'question': 'What is the output of the following code?\nx = [1, 2, 3, 4, 5]\nprint(x[-1])',
'options': ['0', '1', '5', 'Error'],
'answer': '5'},
20: {'question': 'How can you convert an integer to a string in Python?',
'options': ['int()', 'float()', 'str()', 'bool()'],
'answer': 'str()'},
21: {'question': 'What is the output of the following code?\ny = 5\ny = str(y)\nprint(y)',
'options': [' "5" ', '5', 'Error', 'None'],
'answer': ' "5" '},
22: {'question': 'How can you access a range of elements in a list using slicing?',
'options': ['x[start:end]', 'x[start:end:step]', 'x[start]', 'x[end]'],
'answer': 'x[start:end]'},
23: {'question': 'How can you perform various operations on lists such as adding, removing, sorting, and reversing elements?',
'options': ['Using list functions and methods', 'Using indexing', 'Using slicing', 'Using data type conversion'],
'answer': 'Using list functions and methods'},
#1.3:

24: {'question': 'What is the order of execution of operators in Python?',
'options': ['Parentheses, Exponentiation, Unary, Multiplication/Division/Modulo, Addition/Subtraction, Bitwise shift, Comparison, Bitwise AND/OR/XOR, Identity, Membership, Logical',
'Parentheses, Exponentiation, Multiplication/Division/Modulo, Unary, Addition/Subtraction, Bitwise shift, Comparison, Bitwise AND/OR/XOR, Identity, Membership, Logical',
'Exponentiation, Parentheses, Unary, Multiplication/Division/Modulo, Addition/Subtraction, Bitwise shift, Comparison, Bitwise AND/OR/XOR, Identity, Membership, Logical',
'Parentheses, Exponentiation, Unary, Addition/Subtraction, Multiplication/Division/Modulo, Bitwise shift, Comparison, Bitwise AND/OR/XOR, Identity, Membership, Logical'],
'answer': 'Parentheses, Exponentiation, Unary, Multiplication/Division/Modulo, Addition/Subtraction, Bitwise shift, Comparison, Bitwise AND/OR/XOR, Identity, Membership, Logical'},
25: {'question': 'What is the output of the following code?\nx = 3\ny = 5\nz = x + y * 2',
'options': ['13', '8', '15', '20'],
'answer': '13'},
26: {'question': 'What is the output of the following code?\nx = 3\ny = 5\nz = (x + y) * 2',
'options': ['13', '8', '16', '20'],
'answer': '16'},
27: {'question': 'What is the output of the following code?\nx = 2\ny = x + 5\nprint(y)',
'options': ['2', '5', '7', '10'],
'answer': '7'},
28: {'question': 'What is the output of the following code?\nx = 5\ny = 2\nif x > y: print("x is greater than y")',
'options': ['x is greater than y', 'y is greater than x', 'x and y are equal', 'Error'],
'answer': 'x is greater than y'},
29: {'question': 'What is the output of the following code?\nx = [1, 2, 3, 4]\nprint(2 in x)',
'options': ['True', 'False', '2', 'Error'],
'answer': 'True'},

#1.4:
30: {'question': 'What is the output of the following code?\nx = 3\ny = 5\nprint(x > y)',
'options': ['True', 'False', 'Error', 'None'],
'answer': 'False'},
31: {'question': 'What is the output of the following code?\nx = 3\ny = 5\nz = 7\nprint((x < y) and (x < z))',
'options': ['True', 'False', 'Error', 'None'],
'answer': 'True'},
32: {'question': 'What is the output of the following code?\nx = 3\ny = 5\nprint(x + y)',
'options': ['8', '13', '-2', 'Error'],
'answer': '8'},
33: {'question': 'What is the output of the following code?\nx = [1,2,3]\ny = [1,2,3]\nprint(x is y)',
'options': ['True', 'False', 'Error', 'None'],
'answer': 'False'},
34: {'question': 'What is the output of the following code?\nx = [1,2,3,4]\nprint(3 in x)',
'options': ['True', 'False', 'Error', 'None'],
'answer': 'True'},
35: {'question': 'What is the use of assignment operator(=) in python?',
'options': ['Assign a value to a variable', 'Compare values', 'Combine logical expressions', 'Perform mathematical operations'],
'answer': 'Assign a value to a variable'},
36: {'question': 'Which operator is used to check if two variables refer to the same object in memory?',
'options': ['is', 'is not', 'in', 'not in'],
'answer': 'is'},
37: {'question': 'Which operator is used to check if an element is present in a container such as a list, tuple or a string?',
'options': ['Assignment operator(=)', 'Comparison operator(==)', 'Containment operator(in)', 'Identity operator(is)'],
'answer': 'Containment operator(in)'},
#2.1:
38: {'question': 'Which type of statement is used to check if a certain condition is True and execute a code block if it is?',
'options': ['If', 'Elif', 'Else', 'Nested'],
'answer': 'If'},

39: {'question': 'Which type of statement is used to check if a previous if statement condition was False and execute a code block if the current condition is True?',
'options': ['If', 'Elif', 'Else', 'Nested'],
'answer': 'Elif'},

40: {'question': 'Which type of statement is used to execute a code block if none of the previous conditions were True?',
'options': ['If', 'Elif', 'Else', 'Nested'],
'answer': 'Else'},

41: {'question': 'Which type of conditional statement is used when an if statement is used within another if statement?',
'options': ['If', 'Elif', 'Else', 'Nested'],
'answer': 'Nested'},

42: {'question': 'Which type of conditional statement is used when multiple conditions are combined using logical operators?',
'options': ['If', 'Elif', 'Else', 'Compound'],
'answer': 'Compound'},

43:{'question': 'What is the output of the following code?\nx = 3\ny = 5\nif x > 2 and y > 4:\n print("x is greater than 2 and y is greater than 4")',
'options': ['x is greater than 2', 'y is greater than 4', 'x is greater than 2 and y is greater than 4', 'None'],
'answer': 'x is greater than 2 and y is greater than 4'},

44: {'question': 'What is the output of the following code?\nx = 3\nif x > 4:\n print("x is greater than 4")\nelif x > 2:\n print("x is greater than 2")\nelse:\n print("x is less than or equal to 2")',
'options': ['x is greater than 4', 'x is greater than 2', 'x is less than or equal to 2', 'None'],
'answer': 'x is greater than 2'},

45: {'question': 'What is the output of the following code?\nx = 3\ny = 5\nif x > 2:\n if y > 4:\n print("x is greater than 2 and y is greater than 4")',
'options': ['x is greater than 2', 'y is greater than 4', 'x is greater than 2 and y is greater than 4', 'None'],
'answer': 'x is greater than 2 and y is greater than 4'},
#2.2:
46: {'question': 'Which looping statement is used to repeatedly execute a code block as long as a certain condition is True?',
'options': ['For loop', 'While loop', 'Break statement', 'Continue statement'],
'answer': 'While loop'},

47: {'question': 'Which looping statement is used to iterate over a sequence and execute a code block for each item in the sequence?',
'options': ['For loop', 'While loop', 'Break statement', 'Continue statement'],
'answer': 'For loop'},

48: {'question': 'Which statement is used to exit a loop early, before the loop condition is no longer True?',
'options': ['For loop', 'While loop', 'Break statement', 'Continue statement'],
'answer': 'Break statement'},

49: {'question': 'Which statement is used to skip the current iteration of a loop and move on to the next iteration?',
'options': ['For loop', 'While loop', 'Break statement', 'Continue statement'],
'answer': 'Continue statement'},

50: {'question': 'Which statement is used as a placeholder in a code block when a statement is required but no action needs to be taken?',
'options': ['Pass statement', 'For loop', 'While loop', 'Break statement'],
'answer': 'Pass statement'},

51: {'question': 'Which type of loops involve a loop within another loop?',
'options': ['Nested loops', 'Compound conditional loops', 'While loops', 'For loops'],
'answer': 'Nested loops'},

#3.1:
52: {'question': 'What function is used to open a file and return a file object in Python?',
'options': ['open()', 'read()', 'write()', 'close()'],
'answer': 'open()'},

53: {'question': 'What function is used to close a file in Python?',
'options': ['open()', 'read()', 'write()', 'close()'],
'answer': 'close()'},

54: {'question': 'What function is used to read the contents of a file in Python?',
'options': ['open()', 'read()', 'write()', 'close()'],
'answer': 'read()'},

55: {'question': 'What function is used to write a string to a file in Python?',
'options': ['open()', 'read()', 'write()', 'close()'],
'answer': 'write()'},

56: {'question': 'What function is used to append a string to a file in Python?',
'options': ['open()', 'read()', 'write()', 'append()'],
'answer': 'append()'},

57: {'question': 'What statement is used to open and close a file automatically in Python?',
'options': ['open()', 'read()', 'write()', 'with statement'],
'answer': 'with statement'},

58: {'question': 'Which method in os.path module can be used to check the existence of a file in Python?',
'options': ['os.path.open()', 'os.path.exists()', 'os.path.remove()', 'os.path.getsize()'],
'answer': 'os.path.exists()'},

59: {'question': 'Which method in os.path module can be used to delete a file in Python?',
'options': ['os.path.open()', 'os.path.exists()', 'os.path.remove()', 'os.path.getsize()'],
'answer': 'os.path.remove()'},

#3.2:

60: {'question': 'Which function is used to read input from the console?',
'options': ['input()', 'console()', 'read()', 'get()'],
'answer': 'input()'},
61: {'question': 'Which method is used to insert values into a string?',
'options': ['string.insert()', 'string.append()', 'string.format()', 'string.replace()'],
'answer': 'string.format()'},
62: {'question': 'Which method is used to embed expressions inside string literals?',
'options': ['f-string', 'string.embed()', 'string.format()', 'string.insert()'],
'answer': 'f-string'},
63: {'question': 'Which list is used to access command-line arguments passed to the script?',
'options': ['args', 'sys.args', 'sys.argv', 'argv'],
'answer': 'sys.argv'},
64: {'question': 'Which function is used to close a file?',
'options': ['close()', 'end()', 'finish()', 'terminate()'],
'answer': 'close()'},
65: {'question': 'Which function is used to read the contents of a file?',
'options': ['read()', 'get()', 'fetch()', 'extract()'],
'answer': 'read()'},
66: {'question': 'Which function is used to write a string to a file?',
'options': ['write()', 'put()', 'store()', 'insert()'],
'answer': 'write()'},

#4.1:

67: {'question': 'What is the purpose of indentation in code?',
'options': ['To indicate the structure of the code', 'To add visual appeal to the code', 'To separate elements in the code', 'To add notes and explanations to the code'],
'answer': 'To indicate the structure of the code'},
68: {'question': 'What is the purpose of white space in code?',
'options': ['To indicate the structure of the code', 'To add visual appeal to the code', 'To separate elements in the code', 'To add notes and explanations to the code'],
'answer': 'To add visual appeal to the code'},
69: {'question': 'What is the purpose of comments in code?',
'options': ['To indicate the structure of the code', 'To add visual appeal to the code', 'To separate elements in the code', 'To add notes and explanations to the code'],
'answer': 'To add notes and explanations to the code'},
70: {'question': 'What are documentation strings used for in code?',
'options': ['To indicate the structure of the code', 'To add visual appeal to the code', 'To separate elements in the code', 'To add documentation to functions, classes and modules'],
'answer': 'To add documentation to functions, classes and modules'},
71: {'question': 'How are comments added in code?',
'options': ['Using indentation', 'Using white space', 'Using the # symbol', 'Using triple quotes'],
'answer': 'Using the # symbol'},
72: {'question': 'What is the tool used to generate documentation from code?',
'options': ['pydoc', 'docstring', 'indentation', 'comments'],
'answer': 'pydoc'},
73: {'question': 'What is the command used to generate documentation for a specific function or class in pydoc?',
'options': ['pydoc modulename', 'pydoc functionname', 'pydoc classname', 'pydoc module_name.functionname or module_name.classname'],
'answer': 'pydoc module_name.functionname or module_name.classname'},

#4.2:

74: {'question': 'What is the purpose of the return statement?',
'options': ['To return a value from a function', 'To define a function', 'To assign default values to arguments', 'To define the number and types of arguments a function takes'],
'answer': 'To return a value from a function'},
75: {'question': 'What is the purpose of the def keyword?',
'options': ['To define a function', 'To return a value from a function', 'To assign default values to arguments', 'To define the number and types of arguments a function takes'],
'answer': 'To define a function'},
76: {'question': 'What is the purpose of the pass statement?',
'options': ['To be used as a placeholder in a code block', 'To define a function', 'To assign default values to arguments', 'To define the number and types of arguments a function takes'],
'answer': 'To be used as a placeholder in a code block'},
77: {'question': 'What is the purpose of function call signatures?',
'options': ['To define the number and types of arguments a function takes', 'To return a value from a function', 'To assign default values to arguments', 'To define a function'],
'answer': 'To define the number and types of arguments a function takes'},

#5.1:
78: {'question': 'What is a syntax error?',
'options': ['An error that occurs when the code is not written according to the proper syntax of the programming language',
'An error that occurs when the code is written correctly but doesnt produce the intended result',
'An error that occurs when the code is executed and the interpreter encounters an error that stops the program from running',
'An error that occurs when trying to divide by zero'],
'answer': 'An error that occurs when the code is not written according to the proper syntax of the programming language'},
79: {'question': 'What is a logic error?',
'options': ['An error that occurs when the code is not written according to the proper syntax of the programming language',
'An error that occurs when the code is written correctly but doesnt produce the intended result',
'An error that occurs when the code is executed and the interpreter encounters an error that stops the program from running',
'An error that occurs when trying to divide by zero'],
'answer': 'An error that occurs when the code is written correctly but doesnt produce the intended result'},
80: {'question': 'What is a runtime error?',
'options': ['An error that occurs when the code is not written according to the proper syntax of the programming language',
'An error that occurs when the code is written correctly but doesnt produce the intended result',
'An error that occurs when the code is executed and the interpreter encounters an error that stops the program from running',
'An error that occurs when trying to divide by zero'],
'answer': 'An error that occurs when the code is executed and the interpreter encounters an error that stops the program from running'},
81: {'question': 'What is the purpose of function call signatures?',
'options': ['To define the number and types of arguments a function takes', 'To return a value from a function', 'To assign default values to arguments', 'To define a function'],
'answer': 'To define the number and types of arguments a function'},
#5.2:

82: {'question': 'What is the purpose of the try statement?',
'options': ['To enclose a block of code that may raise an exception', 'To define a block of code that will be executed if an exception is raised', 'To define a block of code that will be executed if no exception is raised', 'To define a block of code that will always be executed'],
'answer': 'To enclose a block of code that may raise an exception'},

83: {'question': 'What is the purpose of the except statement?',
'options': ['To enclose a block of code that may raise an exception', 'To define a block of code that will be executed if an exception is raised', 'To define a block of code that will be executed if no exception is raised', 'To define a block of code that will always be executed'],
'answer': 'To define a block of code that will be executed if an exception is raised'},

84: {'question': 'What is the purpose of the else statement?',
'options': ['To enclose a block of code that may raise an exception', 'To define a block of code that will be executed if an exception is raised', 'To define a block of code that will be executed if no exception is raised', 'To define a block of code that will always be executed'],
'answer': 'To define a block of code that will be executed if no exception is raised'},

85: {'question': 'What is the purpose of the finally statement?',
'options': ['To enclose a block of code that may raise an exception', 'To define a block of code that will be executed if an exception is raised', 'To define a block of code that will be executed if no exception is raised', 'To define a block of code that will always be executed'],
'answer': 'To define a block of code that will always be executed'},

#5.3:

86: {'question': 'What is the purpose of the unittest module?',
'options': ['To provide a framework for writing and running unit tests', 'To define the number and types of arguments a function takes', 'To return a value from a function', 'To assign default values to arguments'],
'answer': 'To provide a framework for writing and running unit tests'},
87: {'question': 'Which method is used to check if a is equal to b?',
'options': ['assertEqual(a, b)', 'assertTrue(x)', 'assertIs(a, b)', 'assertIsInstance(a, b)'],
'answer': 'assertEqual(a, b)'},
88: {'question': 'Which method is used to check if x is True?',
'options': ['assertEqual(a, b)', 'assertTrue(x)', 'assertIs(a, b)', 'assertIsInstance(a, b)'],
'answer': 'assertTrue(x)'},
89: {'question': 'Which method is used to check if a is a member of b?',
'options': ['assertEqual(a, b)', 'assertTrue(x)', 'assertIs(a, b)', 'assertIn(a, b)'],
'answer': 'assertIn(a, b)'},
90: {'question': 'Which method is used to check if a is an instance of b?',
'options': ['assertEqual(a, b)', 'assertTrue(x)', 'assertIs(a, b)', 'assertIsInstance(a, b)'],
'answer': 'assertIsInstance(a, b)'},

#6.1:

91: {'question': 'What is the purpose of the io module?',
'options': ['To perform various input and output operations on files', 'To create and delete directories', 'To check if a file or directory exists', 'To access system-specific parameters and functions'],
'answer': 'To perform various input and output operations on files'},

92: {'question': 'What is the purpose of the os module?',
'options': ['To perform various input and output operations on files', 'To create and delete directories', 'To check if a file or directory exists', 'To execute command-line commands'],
'answer': 'To create and delete directories and execute command-line commands'},

93: {'question': 'What is the purpose of the os.path module?',
'options': ['To perform various input and output operations on files', 'To create and delete directories', 'To check if a file or directory exists', 'To check file paths and filenames'],
'answer': 'To check file paths and filenames'},

94: {'question': 'What is the purpose of the sys module?',
'options': ['To perform various input and output operations on files', 'To create and delete directories', 'To check if a file or directory exists', 'To access system-specific parameters and functions'],
'answer': 'To access system-specific parameters and functions'},

95: {'question': 'What is the method used to check if a file or directory exists in os.path module?',
'options': ['os.path.exists()', 'os.path.getsize()', 'os.path.splitext()', 'os.mkdir()'],
'answer': 'os.path.exists()'},

#6.2:
96: {'question': 'What is the purpose of the math modules fabs function?',
'options': ['To calculate the absolute value of a number', 'To round up to the nearest integer', 'To round down to the nearest integer', 'To calculate the square root of a number'],
'answer': 'To calculate the absolute value of a number'},

97: {'question': 'What does the datetime modules now() method return?',
'options': ['The current date and time', 'The current day of the week', 'The current year', 'The current month'],
'answer': 'The current date and time'},

98: {'question': 'What does the random modules randrange method do?',
'options': ['Generates a random integer within a given range', 'Randomly shuffles a list', 'Randomly chooses an element from a list', 'Generates a random float between 0 and 1'],
'answer': 'Generates a random integer within a given range'},

99: {'question': 'What does the random modules shuffle method do?',
'options': ['Generates a random integer within a given range', 'Randomly shuffles a list', 'Randomly chooses an element from a list', 'Generates a random float between 0 and 1'],
'answer': 'Randomly shuffles a list'},

100: {'question': 'What does the random modules sample method do?',
'options': ['Generates a random integer within a given range', 'Randomly shuffles a list', 'Randomly chooses multiple elements from a list without replacement', 'Generates a random float between 0 and 1'],
'answer': 'Randomly chooses multiple elements from a list without replacement'}

}

score = 0

for question_num, question in questions.items():
    os.system('cls' if os.name == 'nt' else 'clear')  # This command clears the terminal screen
    print(question['question'])
    options = question['options']
    random.shuffle(options)
    for i, option in enumerate(options):
        print(f"{i+1}. {option}")
    user_answer = input("\nEnter the number of your answer:\n ")
    if options[int(user_answer)-1] == question['answer']:
        print("\nCorrect!")
        score += 1
        print("Current score:", score)
        input("Press enter to continue")
        os.system('cls' if os.name == 'nt' else 'clear') # This command clears the terminal screen again

    else:
        print("\nIncorrect.")
        print("Current score:", score)
        input("Press enter to continue")
        os.system('cls' if os.name == 'nt' else 'clear') # This command clears the terminal screen again


    print()

percentage = score / len(questions) * 100
print(f"Your final score is {score} out of {len(questions)} ({percentage:.2f}%).")