en_ru = {"q":"й", "w":"ц", "e":"у", "r":"к", "t":"е", "y":"н",
         "u":"г", "i":"ш", "o":"щ", "p":"з", "[":"х", "]":"ъ",
         "a":"ф", "s":"ы", "d":"в", "f":"а", "g":"п", "h":"р",
         "j":"о", "k":"л", "l":"д", "'":"ж", '"':"э", "z":"я",
         "x":"ч", "c":"с", "v":"м", "b":"и", "n":"т", "m":"ь",
         ",":"б", ".":"ю", "?":",", "/":".", "&":"?"}
ru_en = {"й":"q", "ц":"w", "у":"e", "к":"r", "е":"t", "н":"y",
         "г":"u", "ш":"i", "щ":"o", "з":"p", "ф":"a", "ы":"s",
         "в":"d", "а":"f", "п":"g", "р":"h", "о":"j", "л":"k",
         "д":"l", "я":"z", "ч":"x", "с":"c", "м":"v", "и":"b",
         "т":"n", "ь":"m", "б":",", "ю":",", ",":"?"}

switcherMode = "off"

def englishToRussian (inputString):
    inputList = list(inputString)
    resultList = list()
    for elem in inputList:
        if elem.isupper() and en_ru.get(elem.lower()) != None:
            resultList.append(en_ru.get(elem.lower()).upper())
        elif en_ru.get(elem) != None:
            resultList.append(en_ru.get(elem))
        else:
            resultList.append(elem)
    result = "".join(resultList)
    return result

def russianToEnglish (inputString):
    inputList = list(inputString)
    resultList = list()
    for elem in inputList:
        if elem.isupper() and ru_en.get(elem.lower()) != None:
            resultList.append(ru_en.get(elem.lower()).upper())
        elif ru_en.get(elem) != None:
            resultList.append(ru_en.get(elem))
        else:
            resultList.append(elem)
    result = "".join(resultList)
    return result

def setMode (mode):
    global switcherMode
    if mode == "english" or mode == "russian":
        switcherMode = str(mode)
    pass

def getMode ():
    return switcherMode
