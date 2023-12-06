def alphanumeric(password):
    return password.isalnum()

string = input()

print(alphanumeric(string))


#alternative
alphanum = lambda psw: psw.isalnum()

print(alphanum(string))
