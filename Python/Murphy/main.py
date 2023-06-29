#  Murphy Çözümü - Ömer Arda Kaya - 29.06.2023
#  Problem linki: https://github.com/squillero/computer-sciences/tree/master/Python/exams/_imported/murphy


def main():
    try:
        murphyfile = open("Murphy_reads.txt", "r")
    except OSError:
        print("Murphy reads not found.")
        return -1
    try:
        argumentsfile = open("arguments.txt", "r")
    except OSError:
        print("Arguments not found.")
        return -2
    arguments = []  # Argümanları bir listeye alalım (dosya pointer resetlenmeme olayını unutma)
    for crude in argumentsfile:
        argument = crude.strip()
        arguments.append(argument)
    title = None  # Her maxim title ile başlayıp belirsiz miktarda statement ile devam ediyor. Title öncesi boşluk var
    found = False
    for crude in murphyfile:
        line = crude.strip()
        if line != "" and not found:  # Satır boşluk ise title'ı resetlemek lazım
            if not title:  # Title resetlenmiş ise yeni title şu anki satır
                title = line
            for argument in arguments:  # Bütün argümanları satırın içinde tek tek arıyoruz
                if argument in line.lower():  # Aradığımız argüman büyük harfli olabilir; bütün satırı küçültüyoruz
                    if len(line) > 50:  # Satır 50 harften uzunsa 50 harf printleyip üç nokta ekliyoruz (Hoca istemiş)
                        print(title, "-", line[0:50] + "...")
                    else:
                        print(title, "-", line)
                    found = True  # Bir maximde argüman bulunduysa o maximi tekrar printlemiyoruz
                    break  # O maximi atlamak için tekrar boş satır olana kadar her satırı found ile atlıyoruz
        elif line == "":
            title = None
            found = False


if __name__ == '__main__':
    main()
