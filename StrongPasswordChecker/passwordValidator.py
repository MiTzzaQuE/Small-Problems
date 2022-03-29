

class passwordValidator:

    def __init__(self):
        return

    '''
        Function that takes one string and checks if password length is between 6 and 20
        :param = string - String given with password to be checked
        :return = True if it meets the requirments
        return False otherwise
    '''
    def checkPasswordLength(self, string):
        return 6 <= len(string) <= 20


    ''' 
        Function that takes one string and checks if it has at least one lowercase
        :param = string - String given with password to be checked
        :return = True if it meets the requirments
        return False otherwise
    '''
    def checkLowercaseLetter(self, string):
        for letter in string:
            if letter.islower():
                return True
        return False


    ''' 
        Function that takes one string and checks if it has at least one uppercase
        :param = string - String given with password to be checked
        :return = True if it meets the requirments
        return False otherwise
    '''
    def checkUppercaseLetter(self, string):
        for letter in string:
            if letter.isupper():
                return True
        return False


    ''' 
        Function that takes one string and checks if it has at least one digit
        :param = string - String given with password to be checked
        :return = True if it meets the requirments
        return False otherwise
    '''
    def checkDigit(self, string):
        for letter in string:
            if letter.isdigit():
                return True
        return False


    ''' 
        Function that takes one string and checks if it does not contain more than 3 duplicates in a row
        :param = string - String given with password to be checked
        :return = List which contains indexes of first element from a 3 duplicate row
    '''
    def checkDuplicates(self, string):
        stringLength = len(string)
        indexs = []
        currentIndex = 0

        while currentIndex < (stringLength - 2):

            if string[currentIndex] == string[currentIndex + 1] == string[currentIndex + 2]:
                lastDuplicateIndex = currentIndex + 2

                while lastDuplicateIndex < len(string) and string[lastDuplicateIndex] == string[currentIndex]:
                    lastDuplicateIndex += 1

                for element in range(lastDuplicateIndex-currentIndex):
                    if element % 3 == 0:
                        indexs.append(currentIndex + element)
                currentIndex = lastDuplicateIndex - 1

            currentIndex += 1

        return indexs


    ''' 
        Function that takes one string and checks if it meets all the requirments
        :param = string - String given with password to be checked
        :return = True if it meets the requirments
        return False otherwise
    '''
    def validatePassword(self, string):
        if self.checkPasswordLength(string) == self.checkDigit(string) == self.checkUppercaseLetter(string) == self.checkLowercaseLetter(string) == True\
                and len(self.checkDuplicates(string)) == 0:
            return True
        return False