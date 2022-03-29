from controller import controller
from tests import tests

class Console:

    def __strong(self):
        password = input("Write a password: ")
        con = controller()
        solution = con.runAlgorithm(password)

        if solution == 0:
            print("MINIMUM:",solution,"\nThis is a strong password")
        else:
            print("MINIMUM number of changes for a stronger password is: ", solution)

    def __tests(self):
        pasTests = tests()

    def run(self):
        while True:
            print("\n\nPress 1 for normal MINIMUM number of steps to a stronger password\nor 2 for tests "
                  "validation\nexit closes the program\n\n")
            print(">>")
            cmd = input()
            if cmd == "1":
                self.__strong()
            elif cmd == "2":
                self.__tests()
            elif cmd == "exit":
                return
            else:
                continue
