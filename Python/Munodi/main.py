#  Munodi Çözümü - Ömer Arda Kaya - 18.04.2023
#  Problem linki: https://github.com/squillero/computer-sciences/tree/master/Python/exams/munodi

SEQUENCE = "seq.dat"


def main():
    try:
        sequencefile = open(SEQUENCE, "r")
    except OSError as problem:
        print("Error while opening file. Error:", problem)
        return -1
    order = 0
    for linestr in sequencefile:
        order += 1
        line = linestr.split(" ")
        illegal = False
        for pos in range(0, len(line)):
            after = pos + 1
            if after == len(line):
                break
            curnum = int(line[pos])
            nextnum = int(line[pos + 1])
            if curnum % 2 == 0:
                if curnum / 2 != nextnum:
                    illegal = True
                    break
            else:
                if curnum * 3 + 1 != nextnum:
                    illegal = True
                    break
        if illegal:
            print("Sequence", order, "is NOT a Munodi sequence")
        else:
            print("Sequence", order, "is a Munodi sequence (length", str(len(line)) + ")")


if __name__ == '__main__':
    main()
