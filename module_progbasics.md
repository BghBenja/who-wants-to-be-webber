# Programming Basics questions

## Computer science

### Data structures


#### What is the purpose of a list (array in some programming languages) data structure? Name some methods of it!
    List can store multiple items in a single variable. Lists are also useful data structures because they are iterable and mutable.
    Methods:
        - list.count(item) --> counts an item in a list
        - list.append(item) --> add a single item the the end of the list
        - list.remove(item) --> remove item from the list
        - list.sorted()
        - list.index(x)--> get the smallest index of the item
        - len(list) --> return the length of a list (number of items in the list)

#### What is the difference between a list/array and a set?
    In list you can refer with index. In set you can not (and the index is metter)
    List is a collection which is ordered and changeable and allows duplicate members
    Set is a collection which is unordered and unindexed. No duplicate members

#### What is the purpose and methods of a dictionary/map data structure?
    Consists of a collection of key-value pairs. Each key-value pair maps the key to its associated value. 
    Dictionary items are unordered, mutable, and indexed
    Dictionary items are presented in key:value pairs, and can be referred to buy using the key name.
    Methods:
        dict() --> creates a dictionary in Python.
        dict.get(key)  --> return value based on key or None if it doesn't exist
        update() --> muck like append in lists. Adds items to the dictionary once. It can change already existing value too
        dict.keys() --> returns the keys of the dictionary.
        dict.values() --> returns the values of the dictionary
        dict.items() return both the keys and values of the dictionary.


### Algorithms


#### Fibonacci sequences. Write a method (or pseudo code), that generates the Fibonacci sequences.
    fibonacci  = [0, 1]
    n = int(input("How far do you want"))
    count = 0
    index1 = 0
    index2 = index1 + 1
    while count < n:
        fibonacci.append(fibonacci[index1] + fibonacci[index2])
        index1 += 1
        count += 1
    print(fibonacci)

        or

    for element in range(n):
        fibonacci.append(fibonacci[element - 1] + fibonacci[element])
    print(fibonacci)

#### How do you find a max value in a list/array if you can’t use any built-in functions?
    list_of_numbers = [...]
    max_value = list_of_numbers[0]
    for elements in list_of_numbers:
        if element > max_value
        max_value = element

        or

    With bubblesort and than tha last element in the list is the maximum value:

    N = len(array)
    i = 0
    j = 0
    while j < N - i -1:
        if array[j] > array[j+1]: 
            array[j], array[j+1] = array[j+1], array[j] 
        j += 1
        if j >= N - i - 1:
            j =0 
            i += 1
    print(array[-1])

#### How do you find the average of values in a list/array if you can’t use any built-in functions?
    Sum all the elements than divide with the lenght of the list.
    lista = [...]
    sum(lista) / len(lista)

    or

    lista = [...]
    sum = 0
    for element in lista:
        sum += elemelent
    return sum / len(lista)

#### What do we call an *in-place* sort?
    Sorting list without assigning its sorted outcome to any other variable.
    list.sort() --> because i modifies the lins in-place

#### Explain an algorithm which sorts a list!
    Bubblesort: The algorithm iterates through the list, the number of times of the list's length. each time it chaecks adjacent elements and if the next element is lower, it swaps them. This way it sorts the list into ascending order.

    N = len(array)
    i = 0
    j = 0
    while j < N - i -1:
        if array[j] > array[j+1]: 
            array[j], array[j+1] = array[j+1], array[j] 
        j += 1
        if j >= N - i - 1:
            j =0 
            i += 1
    print(array)


### Programming paradigms - procedural


#### What is the call stack?
    It's a data structure, that stores information about the active subroutines of the program.

#### What is “Stack overflow”?
    It's an error which occurs when a program attempts to use more space than available on the call stack. It's often the result of faulty programming and/or infinite loops.

#### What are the main parts of a function?
    def 'function name' ('the argument'): --> name (parameters)
            'the algorithm' or 'the function body that describing the routine.'
            return 'the return value'


### Programming languages - Python  


#### How do you use a dictionary in Python?
    Dictionaries contain key-value paris. They are unordered, mutable and indexed
    dict = {key:value}
    Referencing keys value in dictionary: dict['key'] --> It gives back the value 
    Referencing key in dictionary: dict['key'].key() --> It gives back the key

#### What does it mean that an object is immutable in Python?
    The object's state can't be modified after declaring it.
    These are of in-built types such as: int, floeat, bool, string, unicode, tuple.

#### What is conditional expression in Python?
    Conditional expressions return different values based on the result of boolean expression spcified by the programmer (based on the condition being true or false). The result of boolian expression is either True or False.

#### What are different types of arguments in Python?
    Default argumetns: agrument has no value specified by default and requires another variable inside the program to get itself a value.
        def sum(a=2, b=5):
    Keyword arguments: has value by default, can only be sepified after the default arguments and never before them.
        def print_name(name1, name2)
        print_name('Ákos','Tegez')
    Variable length keyword arguments: The amount of arguments is not static, but hte value of the arguments is static.
        def locations(name, adress):
        locations('ákos','Béla','Márk' = 'Budaepst', 'Máté' = 'Tatabánya', 'Róland' = 'Szolnok')
    Command-line arguments: The arguments value is declared when stating the program in a command-line.
    
#### What is variable shadowing? (context: variable scope)
    A variable declared within a certain scope which has the same name as a variable declared in an outer scope. This outer variable is said to be shadowed by the inner variable, while the inner identifier is said to mask the outer indertifier. This can lead to confusion, as it may be unclear which variable subsequent uses of the sahdowed variable name refer to.

#### What can happen if you try to delete/drop/add an item from a List, while you are iterating over it in Python?
    With add (append): The iteration continues without an issue, albeit with different ammount of elements.
    With delete/drop: The program breaks with an index error.

#### What is the "golden rule" of variable scoping in Python (context: LEGB)? What is the lifetime of variables?
    Avoiding global variables use.
    The golden rule means that variables should only be accessible where they are use.

    In python the LEGB rule is used to decide the order in which the namespaces are to be searched for scope resolution.
    LEGB stand for:
        1. Local: Defined inside the function
        2. Enclosed: Defined inside enclosing functions (nested funcions concept)
        3. Global: Defined at the uppermost level
        4. Built-in: Reserved names in Python built-in modules

#### If you need to access the iterator variable after a for loop, how would you do it in Python?
    Just assign it to another variable inside the foor loop and the new variable can be used afterwards outside the for loop.

#### What type of elements can a list contain in Python?
    Any data type can be listed in python. Such as: Boolean, string, float, integer, lists, dict, tuple or sets

#### What is slice operator in Python and how to use?
    slicing can be done with the silce() function or with list slicint. These doesnt change the list but creates a new object, but return s a part (slice) of the object.
    list[start:end:step] --> ceartes a new list from the elements between start and end (the end index is not included)

#### What arithmetic operators (+,*,-,/) can be used on lists in Python? What do they do?
    + adds to the value of the variable in the list element or joins two lists together or adds a string into a list character by character or by itself
    * multiplies the value in the list element or multiplies the number of list elements themselvers or multiplies the ammount of list elements
    - substracts from the list elements value
    / divides the list elements value

#### What is the purpose of the in and not in membership operators in Python?
    IN operators check if the value is inside a list/set/dictionary.
    NOT operators is a negation statement, and it checks if the value is NOT equal to the control value
    NOT IN: Reserve of the in oparator
#### What does the + operator mean when used with strings in Python?
    It is used to add characters or other strings at the end of strings or to join mutliple string together
#### Explain f strings in Python?
    f strings are strings that contain the value of a variable in themself and this making them dynamic
    f'string {variable} string'

#### Name 4 iterable types in Python!
    String, list, tuple, dictionary

#### What is the difference between list/set/dictionary comprehension and a generator expression in Python?
    List/set/dictionary comprehensions create the entire collection at once, while generators can evaluate elements on demand.
    List/set/dictionary can be reffered to by themselves. Generator expressions can only be reffered to in loops. Generator functions contain one or more yield statements instead of a return statement.

#### Does the order of the function definitions matter in Python? Why?
    Yes, it matters if you want to use one function inside another. Then the inner function must be defined before the outer definition.

#### What does unpacking mean in Python?
    Unpacking is a way where arguments can be given to a function from a list/set/dictionary. Unpacking is done by the * or the ** operator.

#### What happens when you try to assign the result of a function which has no return statement to a variable in Python?
    The value will be None and that will be assigned to the variable and its type will become NoneType.


## Software engineering


### Debugging


#### What techniques can you use while debugging a program in Python?
    Use the built in debugger from the IDE. Read between the code and try to figure out the proglem.
    or
    Print out the variables and check where it goes wrong.

#### What does step over, step into and step out mean while using the debugger?
    Step over: steps over the next line or loop in the code (skip a certain function)
    Step into: steps into definitions or loops and checks the functions line by line
    Step out: does the opposite that step into.

#### How can you start to debug a program from a certain line using the debugger?
    Place a break points in the IDE at the line where you want to start debugging at. The breakponts where the the built in debugger tool stop the running code.

### Version control

#### What are the advantages of using a version control system?
    You can record and follow every change throughout the project.
    Multiply people can work on the same code at the same time.
    If comething goes wrong, you can always go back to a previous version.

#### What is the difference between the working directory, the staging area and the repository in git?
    Working directory: The current, active directory that you modify on you computer.
    Staging area: contains the files that are added from the working directory.
    (Local git) repositry: storage of commited changes, which can be restored or merged later if needed (and than pushed to github)

#### What are remote repositories in git?
    These are online storages of the git, repositories that are not on the computer you are working on.
    It can be used to share code with colleagues by git push/pull command and to manage multiple branches and merges between the versions.

#### Why does a merge conflict occur?
    A conflict arises when two separate branches have made edits to the same line in a file or when a file has been deleted in one branch but edited in the other.

#### Through what series of commands could you put a new file into a remote repository connected to your existing local repository?
    git clone or init .... --> cloning a repository
    touch filename --> creating a new file
    git add filename or . --> add file to staging
    git commit -m "commit massage" --> creat a commit with an appropritate massage and add it to the local repository
    git push --> push the canges/commits to the remote repository

#### What does it mean atomic commits and descriptive commit messages?
    Atomic commits: When you commit every logical block that you wrote
    Descriptive commit massage: when the commit massages are meaningful, concrise and easy to read.

#### What’s the difference between git and GitHub?
    Git is a distributed version control tool that can manage a development project's source code history, while GitHub is a cloud bades platform built around the Git tool. It is a website for monitoring git projects, commits, and branches.


## Software design


### Clean code


#### What does clean code mean?
    The code is clean if it can be understood easily, from understandability comes readability, cangeability, extensibility and maintainability. There is no duplications, no dead code, meaningful names, proper indentation, functional structure and no magic numbers in it.

#### What steps do we usually do during a clean code refactoring?
    1. Rename badly named variables and funcions (name magical number)
    2. Fix badly formatted code
    3. Clear repetitive code
    4. Refactor long methods
    5. Fix wrond comment usage
    6. Delete dead codes


### Error handling


#### What is exception handling?
    Exceptions are use to handle possible errors occurring during the program execution. Exceptions can anticipate the error type (it it is given) and when the error occurs it will execute the coded lines inside the exceptions instead of crashing the program.

#### What are the basics of exception handling in Python?
    We use try-except block.
    It the try block runs to failure, it jumps to the except block rather than crasing. The except block contains the logic that deals with the exception gracefully.

#### In which case should we catch an exception? Why?
    Any time a specific error can be excepted it is wise to use exceptions. For example: when user input is used and the input type is important or when we are liking for files which my not exist or when we need to translate object but it is not clear if it can be done.

#### What can/should we do with an exception in the ‘except’ block?
    Print and understandable error massage (such as ValueError). and tell the program how to continue executing our code (or not)

#### What does the else and finally statement do in a try-except block in Python?
    Else is called when nothing went wrong and the except block doesn't catch an exception.
    Finally block: code is always executed, whether the program executer properly or it raised an exception.


## Software Development Methodologies


#### What is the main goal of a retrospective meeting?
    The goal is to discuss among the team members how the work went during the last spring, what was good, what was bad, and what steps each member can take to improve the personal and team work.


## Programming environment


### Unix


#### What is UNIX and what is Linux?
    UNIX is a family of multitasking multiuse computer operating system from the 70's that meant to be easier to handle for programmers than conventional operating system. It has a modular design and command line interface (CLI)

    LINUX is a family of open source Unix-like operating system based on the Linux kernel.
    Linux is free (open source) and currently maintained and updated by the Linux community, but UNIX is licensed. Unix-like systems are very similar to UNIX, even though they are not certified to be UNIX system.
    Linux also has a GUI (Graphical User Interface)

#### What do we call the shell in Linux?
    A Shell is a command interpreter in Linux used mainly in the Linux Terminal. It provides a computer user an interface to the UNIX/GNU Linus system so that the user can run different command or utilities/tools with some input data (then executed by the operating system)

#### What does root means in a Linux environment?
    Root either means Root Directory, or in the case of privileges, it means administrator, or complete privilege with access to all commands in the OS.

#### How do you access your personal files in Linux?
    Through the file browser of by the treminal with the "cd" command

#### How can you install an application in Linux?
    You can use the software center or you can use commands in the terminal as well:
    sudo apt-get install <application name>
    brew install <application name> (macOS)
#### What is package management in Linux, what are repositories?
    Package management keeps track of the users' software packages. It tells the user whenever there's a new version of an installed software is available.
    The repository storage location where new softwares get installed and existing softwares get updated.

#### How do you navigate in the filesystem with the command line?
    pwd: Print workind directory
    ls: List items
    cd: Change direstory

#### What does the following commands do: mkdir, rm, cat, cp, touch?
    mkdir: Create new folder (directory)
    rm: Remove file or folder (directory)
    cat: Concatenate files and print to standard output
    cp: Copy file or folder (directory)
    touch: Create new file

#### How can you look up what does a command do in Linux if you have no internet connection?
    man <command name>
    <command name> --help

#### What does the following commands do: head, tail, more, less?
    head: Print the first 10 lines to standard output
    tail: Print the last 10 lines to standard output
    more: View one screenful of text at a time
    less: similat to more, but faster and you can navigate through the file. Better for large files

#### How do you download a file from internet using the terminal?
    wget <URL>
