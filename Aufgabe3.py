import sys


def outputfile_open():
    try:
        if len(sys.argv) > 3:
            fh = open(sys.argv[3], "w")
        else:
            fh = sys.stdout
        return fh
    except IOError:
        print("Error: could not open output file for writing!")

# Starts here
searchwords = dict()
dictText = dict()

linkstatistikfilename = "Linkstatistik.txt"
# wenn mehr als ein argument gegeben wurd speichere das erste als readfilename ab
if len(sys.argv) > 1:
    linkstatistikfilename = sys.argv[1]

# sind es mehr als 2 öffnet er das 2. als searchwordfile
if len(sys.argv) > 2:
    with open(sys.argv[2], encoding="utf-8") as swfile:
        for i in swfile:
            searchwords[i.rstrip()] = 0

# Wenn noch nichts im dictionary steht, öffnen und eingaben einlesen bis " " kommt
if len(searchwords) == 0:
    eingabe = ""
    while eingabe != " ":
        eingabe = input("Enter search string: ")
        if eingabe != " ":
            searchwords[eingabe] = 0

# öffnet readfile, speichert alle zeilen gesplittet und vergleicht sie mit den eingabeworten, speichert nur häufigstes
with open(linkstatistikfilename, encoding="utf-8") as readfile:
    for i in readfile:
        liste = i.rstrip().split("\t")
        if len(tuple) > 2:
            if liste[2] in searchwords:
                if int(liste[0]) > searchwords[liste[2]]:
                    searchwords[liste[2]] = int(liste[0])
                    dictText[liste[2]] = liste[1]

# erstellt einen output
with outputfile_open() as outfile:
    for i in searchwords:
        if i in dictText:
            outfile.write(str(dictText[i]) + "\n")
