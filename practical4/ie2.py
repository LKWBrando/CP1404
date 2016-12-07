usernames = ['jimbo', 'giltson98', 'derekf', 'WhatSup', 'NicolEye',
             'swei45','BaseInterpreterInterface', 'BaseStdIn', 'Command',
             'ExecState', 'InteractiveConsole', 'InterpreterInterface', 'StartServer', 'bob']

userInput = str(input("Please enter your username"))
while userInput not in usernames:
    print("Access Denied")
    userInput = str(input("Please enter your username"))
print("Access Granted")
