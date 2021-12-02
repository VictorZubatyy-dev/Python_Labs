global_var = "I'm global"


def enclosing():
    print("enclosing")
    enclosing_var = "a"
    # print(global_var)
    global_var = "hello World"

    def inner():
        print("inner")
        i = 22
        nonlocal enclosing_var
        enclosing_var = 7
        print(i)
        print(enclosing_var)
        global global_var
        print(global_var)

    print(global_var)

    inner()
    print(global_var)
    print(enclosing_var)
    # print(i) # causes an error

    # loop and if statements don't count as blocks in Python
    # -> declarations inside are visible outside
    for runner_var in range(0,5):
        b = runner_var


    print(b)

enclosing()


