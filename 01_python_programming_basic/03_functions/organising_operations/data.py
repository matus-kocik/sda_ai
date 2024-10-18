this_text = "Hello World"

""" def log_into_terminal():
    print(this_text)

log_into_terminal() """


def log_into_terminal():
    local_text = "Ahoj svet"
    print(local_text)


# log_into_terminal()


def another_function():
    log_into_terminal()
    print(this_text)


# another_function()

third_function = log_into_terminal

# third_function()


def log_into_terminal():
    local_text = "Ahoj svet"
    print(this_text)
    print(local_text)

    def fourth_function():
        print(f"This is four function....")

    fourth_function()


# log_into_terminal()


def another_function():
    log_into_terminal("Its from another function()")


def log_into_terminal(to_log, second_to_log=None):
    print(to_log)
    if second_to_log is not None:
        print(second_to_log)


# log_into_terminal("Ahoj", "Hello")


def greetings(name=""):
    print(f"Ahoj {name}")


greetings("Matus")
