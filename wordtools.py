
import sys


def cleanword(str):
    alphanumeric = ""

    for character in str:
        if character.isalnum():
            alphanumeric += character
    retorno = alphanumeric.strip()
    return retorno

def has_dashdash(str):
    flag1 = False
    flag2 = False

    for character in str:
        if character == '-':
            if not flag1:
                flag1 = True
            else:
                flag2 = True
        else:
            flag1 = False

    return flag2


def extract_words(str):
    lista = str.split()
    listaNova = []
    for string in lista:
        alphanumeric = ""
        for character in string:
            if character.isalnum():
                alphanumeric += character
            else:
                alphanumeric += ' '
        listatemp = alphanumeric.split()
        for str in listatemp:
            listaNova.append(str.lower())

    return listaNova


def wordcount (str, list):
    count = 0
    for string in list:
        if string == str:
            count = count + 1
    return count

def wordset (list):
    listaNova = []
    for string in list:
        if not string in listaNova:
            listaNova.append(string)
    listaNova.sort()
    return listaNova

def longestword(list):
    numero = 0
    for str in list:
        if numero < len(str):
            numero = len(str)
    return numero


def test(passou):
    linha = sys._getframe(1).f_lineno
    if passou:
        msg = "linha {0} funciona".format(linha)
    else:
        msg = "erro na linha {0}".format(linha)
    print(msg)


def testes():
    test(cleanword("what?") == "what")
    test(cleanword("'now!'") == "now")
    test(cleanword("?+='w-o-r-d!,@$()'") == "word")
    test(has_dashdash("distance--but"))
    test(not has_dashdash("several"))
    test(has_dashdash("spoke--"))
    test(has_dashdash("distance--but"))
    test(not has_dashdash("-yo-yo-"))
    test(extract_words("Now is the time! 'Now', is the time?Yes, now.") ==
    ['now', 'is', 'the', 'time', 'now', 'is', 'the', 'time', 'yes', 'now'])
    test(extract_words("she tried to curtsey as she spoke--fancy") ==
    ['she', 'tried', 'to', 'curtsey', 'as', 'she', 'spoke', 'fancy']
    )
    test(wordcount("now",
                   ["now", "is", "time", "is", "now", "is", "is"]) == 2)
    test(wordcount("is",
                   ["now", "is", "time", "is", "now", "the", "is"]) == 3)
    test(wordcount("time",
                   ["now", "is", "time", "is", "now", "is", "is"]) == 1)
    test(wordcount("frog",
                   ["now", "is", "time", "is", "now", "is", "is"]) == 0)
    test(wordset(["now", "is", "time", "is", "now", "is",
                  "is"]) ==
         ["is", "now", "time"])
    test(wordset(["I", "a", "a", "is", "a", "is", "I", "am"])
         ==
         ["I", "a", "am", "is"])
    test(wordset(["or", "a", "am", "is", "are", "be", "but",
                  "am"]) ==
         ["a", "am", "are", "be", "but", "is", "or"])
    test(longestword(["a", "apple", "pear", "grape"]) == 5)
    test(longestword(["a", "am", "I", "be"]) == 2)
    test(longestword(["this", "supercalifragilisticexpialidocious"]) == 34)
    test(longestword([]) == 0)


testes()

