kazakh_cyrillic = input("Введите казахский текст на кириллице: ")

kazakh_latin = ""
kazakh_cyrillic_to_latin = {
    "А": "A",
    "Ә": "Á",
    "Б": "B",
    "В": "V",
    "Г": "G",
    "Ғ": "Ǵ",
    "Д": "D",
    "Е": "E",
    "Ё": "E",
    "Ж": "J",
    "З": "Z",
    "И": "I",
    "Й": "I",
    "К": "K",
    "Қ": "Q",
    "Л": "L",
    "М": "M",
    "Н": "N",
    "Ң": "Ń",
    "О": "O",
    "Ө": "Ó",
    "П": "P",
    "Р": "R",
    "С": "S",
    "Т": "T",
    "У": "Ý",
    "Ұ": "U",
    "Ү": "Ú",
    "Ф": "F",
    "Х": "X",
    "Һ": "H",
    "Ц": "C",
    "Ч": "Ch",
    "Ш": "Sh",
    "Щ": "Sh",
    "Ъ": "",
    "Ы": "Y",
    "І": "I",
    "Ь": "",
    "Э": "E",
    "Ю": "Iý",
    "Я": "Ia"
}

for char in kazakh_cyrillic:
    if char.upper() in kazakh_cyrillic_to_latin:
        kazakh_latin += kazakh_cyrillic_to_latin[char.upper()]
    else:
        kazakh_latin += char

print("Казахский текст на латинице: " + kazakh_latin)