
def main():

    #intro
    print('Camel case converter ')
    # Getting a sentence from user, set all to lower case
    sent  = input("Enter the sentence you want to convert \n").lower().strip()
    # Split the sentence into words
    words = sent.split(' ')

    # Create an array  and Capitalize all words
    sentArray = Capitalize(words)

    # for Lab 1 the first word should be lowercase

    camelcase = ''.join(Lab1Edit(sentArray))
    print(camelcase)



def Capitalize(words):
    capWords = []
    # loop each word and capitalize it
    for eashWord in words:
        # Converting each word first letter to upper and appending it with remaining letters
        final_words = eashWord[0].upper() + eashWord[1:].strip()
        # Put all words into array
        capWords.append(final_words)

    return capWords


def Lab1Edit (sentArray):
    #Change the first word to a lowercase
    change = sentArray[0].lower()
    sentArray[0]= change
    #After the edit send back
    return sentArray


if __name__ == '__main__':
        main()
