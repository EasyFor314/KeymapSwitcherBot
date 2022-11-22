en_ru = {"q":"й", "w":"ц", "e":"у", "r":"к", "t":"е", "y":"н",
         "u":"г", "i":"ш", "o":"щ", "p":"з", "[":"х", "]":"ъ",
         "a":"ф", "s":"ы", "d":"в", "f":"а", "g":"п", "h":"р",
         "j":"о", "k":"л", "l":"д", ";":"ж", "'":"э", "z":"я",
         "x":"ч", "c":"с", "v":"м", "b":"и", "n":"т", "m":"ь",
         ",":"б", ".":"ю", "?":",", "/":".", "&":"?"}
ru_en = {"й":"q", "ц":"w", "у":"e", "к":"r", "е":"t", "н":"y",
         "г":"u", "ш":"i", "щ":"o", "з":"p", "ф":"a", "ы":"s",
         "в":"d", "а":"f", "п":"g", "р":"h", "о":"j", "л":"k",
         "д":"l", "ж":";", "'":"э", "я":"z", "ч":"x", "с":"c", 
         "м":"v", "и":"b", "т":"n", "ь":"m", "б":",", "ю":".", ",":"?", ".":"/"}

# af, ar, bg, bn, ca, cs, cy, da, de, el, en, es, et, fa,
# fi, fr, gu, he, hi, hr, hu, id, it, ja, kn, ko, lt, lv,
# mk, ml, mr, ne, nl, no, pa, pl, pt, ro, ru, sk, sl, so,
# sq, sv, sw, ta, te, th, tl, tr, uk, ur, vi, zh-cn, zh-tw

switcherMode = "off"
import langid

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
    """Установить мод"""
    global switcherMode
    switcherMode = str(mode)
    pass

def detect_mode(message: str):
    """ Определить мод по вводимому тексту"""
    #print(message)
    langid.set_languages(['ru', 'en'])  # ISO 639-1 codes
    detect_name_language, score = langid.classify(message)
    #print(detect_name_language)  # en
    #print("Определили язык " + detect_name_language)
    if detect_name_language == "ru":
        setMode("russian")
    elif detect_name_language == "en":
        setMode("english")
    else:
        setMode("off")

def getMode ():
    """Получить текущий мод мод"""
    return switcherMode
