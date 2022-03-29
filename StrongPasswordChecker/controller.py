from string import ascii_letters
from passwordValidator import passwordValidator
import random

class controller:

    def __init__(self):
        self.__validator = passwordValidator()

    '''
        Function that checks if the password contains the requirements, and if is not, will be updated
        :param minimum = integer, total number of steps done so far
        :param string = string, given password to be updated
        :returns the final number of steps done along with updated password
    '''
    def checkAndInsert(self, minimum, string):

        if not self.__validator.checkUppercaseLetter(string):
            string += random.choice(ascii_letters).upper()
            minimum += 1

        if not self.__validator.checkLowercaseLetter(string):
            string += random.choice(ascii_letters).lower()
            minimum += 1

        if not self.__validator.checkDigit(string):
            string += str(random.randint(1, 9))
            minimum += 1

        return minimum, string


    '''
        Function that takes the password, checks if it meets the requirements of at least each one upper, lower, digit 
        letter and after that still inserts random ascii letters until achieves the minimum number of letters
        :param minimum = integer, total number of steps done so far
        :param string = string, given password to be updated
        :returns the final number of steps done along with updated password
    '''
    def insertLetters(self, minimum, string):

        newMinimum, newString = self.checkAndInsert(minimum, string)

        while len(newString) < 6:
            newString += random.choice(ascii_letters)
            newMinimum += 1

        minimum = newMinimum
        string = newString

        return minimum, string


    '''
        Function that takes a longer password, copies first 17 letters from that password, after that checks if it meets the 
        requirements of at least each one upper, lower, digit letter and if there is below 3 updates after check copies the 
        last digits from password until 20th one to minimize the actions of insert/delete/replace
        :param minimum = integer, total number of steps done so far
        :param string = string, given password to be updated
        :returns the final number of steps done along with updated password
    '''
    def deleteLetters(self, minimum, string):

        newString = ""
        for letterIndex in range(0,17):
            newString += string[letterIndex]

        newMinimum, newString = self.checkAndInsert(minimum, newString)

        while len(newString) < 20:
            newString += string[len(newString)]

        minimum = newMinimum + len(string) - 20
        string = newString

        return minimum, string


    '''
        Function that takes the list of indexes for duplicates from given password and replace every password index found 
        with a random ascii letter
        :param minimum = integer, total number of steps done so far
        :param string = string, given password to be updated
        :returns the final number of steps done along with updated password
    '''
    def makeNewStringWithoutDuplicates(self, minimum, string):

        newString = ""
        duplicateList = self.__validator.checkDuplicates(string)
        duplicateList.append(-1)
        # print(duplicateList)
        curentDuplicateIndex = 0

        for index in range(len(string)):

            if index == duplicateList[curentDuplicateIndex]:
                newString += random.choice(ascii_letters)
                minimum += 1
                curentDuplicateIndex += 1
            else:
                newString += string[index]

        return minimum, newString


    '''
        Main function that takes every step and checks in this order:
        - password length, and updates it if needed
        - checks and updates for minimum one upper, lower and digit letter
        - replace one of letters from every group of 3
        :param string = string, given password to be updated
        :returns the final number of steps done for updating to a strong password
    '''
    def strongPassword(self, string):

        minimum = 0
        passwordLength = len(string)

        if not self.__validator.checkPasswordLength(string):
            if passwordLength < 6:
                minimum, string = self.insertLetters(minimum, string)
                # print("1", string)
            else:
                minimum, string = self.deleteLetters(minimum, string)
                # print("2", string, "len:", len(string))


        if len(string) < 20:
            minimum, string = self.checkAndInsert(minimum, string)

        if len(self.__validator.checkDuplicates(string)) > 0:
            minimum, string = self.makeNewStringWithoutDuplicates(minimum, string)
            # print("3", string)


        # print("string: ", string, "", self.__validator.validatePassword(string))

        return minimum


    '''
        Function call for controller
    '''
    def runAlgorithm(self, string):
        return self.strongPassword(string)