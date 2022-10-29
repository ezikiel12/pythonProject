# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
run = 1
while run == 1:
    userSelect =input('Add, Subtract, Multiply, or Divide?')
    print('you selected to ' + userSelect)

    var1 = int(input ('Enter first number:'))
    var2 = int(input('Enter the 2nd number:'))

    def subtract():
        print (var1-var2)

    def multiply():
        print(var1*var2)

    def divide():
        print(var1/var2)
        print('Remainder:', var1%var2)

    def add():
        print(var1+var2)

    match userSelect:
        case 'add':
            add()
        case 'subtract':
            subtract()
        case 'divide':
            divide()
        case 'multiply':
            multiply()

    keepGoing = input("Do another? y/n")
    if keepGoing == 'y':
        run = 1
    else:
        run = 0

