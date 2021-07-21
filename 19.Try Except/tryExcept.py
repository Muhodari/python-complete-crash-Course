try:
    x = int(input("Input an integer: "))
    print(x)
except ValueError:
    print("something went wrong")

finally:
    print("try Except finished")
