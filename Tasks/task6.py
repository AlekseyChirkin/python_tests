# Дан файл Tasks/txt/pwd.txt с логинами и паролями. Найдите топ 10 самых популярных паролей

fileName = "txt/pwd.txt"
passwords = []

with open(fileName, encoding="utf8") as file:
    lines = file.readlines()

for pair in lines:
    pair = pair.split(";")
    passwords.append(pair[1].removesuffix("\n"))

print("Топ-10 самых частых паролей:")

for i in range(1, 11):
    mostFreq = 0
    mostFreqPassword = ''

    for pwd in passwords:
        freq = passwords.count(pwd)
        if mostFreq < freq:
            mostFreq = freq
            mostFreqPassword = pwd

    print(f"{i}. {mostFreqPassword} - он используется {mostFreq} раз")
    passwords = list(filter(mostFreqPassword.__ne__, passwords))
