def hello():
    return "Hello World"

# Ensure input() doesn't break automated tests
if __name__ == "__main__":
    print("Hello World")
    name = input("Enter your name: ")
    print(name)

    num = 34
    if num > 12:
        print("number is good")
    else:
        print("number is bad")

    print(hello())
