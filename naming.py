while True:

    sentence = input("file name?: ")
    case = input("lower/upper/title --> L/U/T ?")


    def lower(name: str):
        return name.replace(" ", "-").lower()
    def upper(name: str):
        return name.replace(" ", "-").upper()
    def title(name: str):
        return name.replace(" ", "-").title()

    if case == "L":
        print(lower(sentence))
    elif case == "U":
        print(upper(sentence))
    else:
        print(title(sentence))

    response = input("Quit y/n?: ")

    if response == "y":
        break

