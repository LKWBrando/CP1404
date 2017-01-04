from practical7.programminglanguage import ProgrammingLanguage

ruby = ProgrammingLanguage("Ruby", "Dynamic", True, 1995)
python = ProgrammingLanguage("Python", "Dynamic", True, 1991)
vb = ProgrammingLanguage("Visual Basic", "Static", False, 1991)

print(ruby)
print(python)
print(vb)

list = [ruby, python, vb]

print("The dynamically typed languages are:")
for i in list:
    if i.is_dynamic() == True:
        print(i.language)

