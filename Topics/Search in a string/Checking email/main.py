def check_email(string):
    try:
        a, b = string.split("@")
    except ValueError:
        print(False)
        quit()

    if ' ' in string:
        print(False)
        quit()

    elif '@' not in string or '@.' in string:
        print(False)
        quit()

    elif "." not in b:
        print(False)
        quit()

    print(True)
    quit()
