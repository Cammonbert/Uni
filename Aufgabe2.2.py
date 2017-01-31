import time
start_time = time.time()


dictRepetition = dict()
dictText = dict()
with open("Linkstatistik.txt", encoding="utf-8") as readfile:
    for i in readfile:
        tuple = i.rstrip().split("\t")
        if len(tuple) > 2:
            dictRepetition[tuple[1]] = dictRepetition.get(tuple[1], 0) + int(tuple[0])
            dictText[tuple[1]] = tuple[2]
with open("Over200.txt", "w", encoding="utf-8") as writefile:
    for i in sorted(dictRepetition):
        if dictRepetition[i] >= 200:
            writefile.write(str(dictRepetition[i]) + "\t" + i + "\t" + dictText[i] + "\n")


print("Running time: %d:%d" % (((time.time() - start_time)/60), ((time.time() - start_time)%60)))