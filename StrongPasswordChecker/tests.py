from passwordValidator import passwordValidator
from controller import controller


class tests:

    def __init__(self):
        pasValidator = passwordValidator()
        passController = controller()

        print("\nVerify Password length:\n")

        print("Has good length ana?",pasValidator.checkPasswordLength("ana"))
        print("Has good length anaAreMere?",pasValidator.checkPasswordLength("anaAreMere"))
        print("Has good length anaAreMereMorcoviSiPortocale?",pasValidator.checkPasswordLength("anaAreMereMorcoviSiPortocale"))

        print("\nVerify Lowercase:\n")

        print("Contains lowercase Ana?",pasValidator.checkLowercaseLetter("Ana"))
        print("Contains lowercase ANA?",pasValidator.checkLowercaseLetter("ANA"))

        print("\nVerify Uppercase:\n")

        print("Contains uppercase Ana?",pasValidator.checkUppercaseLetter("Ana"))
        print("Contains uppcase ana?",pasValidator.checkUppercaseLetter("ana"))

        print("\nVerify Digit:\n")

        print("Contains digit Ana1?",pasValidator.checkUppercaseLetter("Ana1"))
        print("Contains digit ana?",pasValidator.checkUppercaseLetter("ana"))

        print("\nVerify Password\n")

        print("Check password GoodPassword1:",pasValidator.validatePassword("GoodPassword1"))
        print("Check password wrongpassword:",pasValidator.validatePassword("wrongpassword"))
        print("Check password GooodPassword1:",pasValidator.validatePassword("GooodPassword1"))

        print("\nVerify Duplicates\n")

        print("Index duplicates for aaanaaaremereee: ",pasValidator.checkDuplicates("aaanaaaremereee"))
        print("Index duplicates for aaaaaaaaaaaa: ",pasValidator.checkDuplicates("aaaaaaaaaaaa"))

        print("\nVerify Insert\n")

        print("From: ana to:",passController.insertLetters(0,"ana"))

        print("\nVerify Delete\n")

        print("From: aaaaaaaaaaaaaaaaaaaaaaaaa to:",passController.deleteLetters(0,"aaaaaaaaaaaaaaaaaaaaaaaaa"))


        print("\nVerify strong password:\n")

        print("Minimum for AnaaaareMereeeeeeeeeeee: ",passController.strongPassword("AnaaaareMereeeeeeeeeeee"))
        print("Minimum for aaaaaaaaaaaa: ",passController.strongPassword("aaaaaaaaaaaa"))
        print("Minimum for abcdefgabcdefgabcdefgabcdefg: ",passController.strongPassword("abcdefgabcdefgabcdefgabcdefg"))
        print("Minimum for a: ",passController.strongPassword("a"))
        print("Minimum for 1: ",passController.strongPassword("1"))
        print("Minimum for D: ",passController.strongPassword("D"))
        print("Minimum for Strong1: ",passController.strongPassword("Strong1"))