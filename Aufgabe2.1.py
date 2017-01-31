import time
start_time = time.time()


dictionary = dict()
with open("Linktext.txt", encoding="utf-8") as readfile:
    for i in readfile:
        if i in dictionary:
            dictionary[i] += 1
        else:
            dictionary[i] = 1
with open("Linkstatistik.txt","w",encoding="utf-8") as writefile:
    for i in sorted(dictionary):
        writefile.write(str(dictionary[i]) + "\t" + i)

        print("Running time: %d:%d" % (((time.time() - start_time) / 60), ((time.time() - start_time) % 60)))