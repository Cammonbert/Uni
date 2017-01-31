from nltk.tag import StanfordNERTagger
from nltk.tokenize import word_tokenize
import sys


jar = 'C:/Users/Peter/stanford-ner-2016-10-31/stanford-ner.jar'
model = 'C:/Users/Peter/stanford-ner-2016-10-31/classifiers/english.all.3class.distsim.crf.ser.gz'
st = StanfordNERTagger(model, jar)


# erstellt funktion die Ausgabe umleitet, falls mehr als 3 argumente übergeben wurden, ansonsten standartoutput
# falls das ausgabeargument nicht geöffnet werden kann: Error
def outputfile_open():
    try:
        if len(sys.argv) > 3:
            fh = open(sys.argv[3], "w")
        else:
            fh = sys.stdout
        return fh
    except IOError:
        print("Error: could not open output file for writing!")


# öffnet als standard Linkstatistik. erstellt searchword und dictText
linkstatistikfilename = "Linkstatistik.txt"
searchwords = dict()
dictText = dict()


# wenn mehr als ein argument gegeben wurd speichere das erste als readfilename ab
# ich bekomm meine statistik datei
if len(sys.argv) > 1:
    linkstatistikfilename = sys.argv[1]

# sind es mehr als 2 öffnet er das 2. als searchwordfile
# ich bekomm meine suchwort datei
if len(sys.argv) > 2:
    with open(sys.argv[2], encoding="utf-8") as swfile:
        for i in swfile:
            searchwords[i.rstrip()] = 0

# frägt so lange searchwords ab bis einem langweilig wird und " " eingegeben wird
# ich bekomm ein dictionary aus searchwords mit wert 0
if len(searchwords) == 0:
    eingabe = ""
    while eingabe != " ":
        eingabe = input("Enter search string: ")
        if eingabe != " ":
            searchwords[eingabe] = 0

# öffnet readfile und speichert jede zeile gesplittet. vergleicht werte mit den searchword werten, speichert höchsten
# ich setze die werte meines searchword dictionaries auf die höchsten in der statistik gefundenen
''' das ganze mache ich aber nur wenn etwas anderes als "O" durch stanfordNER ausgegeben wird'''
with open(linkstatistikfilename, encoding="utf-8") as readfile:
    for i in readfile:
        liste = i.rstrip().split("\t")
        if len(liste) > 2:
            if liste[2] in searchwords:
                if int(liste[0]) > searchwords[liste[2]]:
                    searchwords[liste[2]] = int(liste[0])
                    dictText[liste[2]] = liste[1]

# erstellt einen output
with outputfile_open() as outfile:
    for i in searchwords:
        if i in dictText:
            outfile.write(str(dictText[i]) + "\n")


def interactive():
    satz = ""
        sentence = word_tokenize(sentence)
        print(st.tag(sentence))
        tags = st.tag(sentence)
        for tup in tags:
            if tup[1] == "O":
                satz += str((tup[0] + " "))
        print(satz)
        satz = ""
        sentence = input("Enter sentence, or Leer for quit.")


def noninteractive(datei):
    reg = r"(\d+)([\t])(.+)([\t])(.+)"        #regex erstellen
    list2 = list()                                  #liste erstellen
    #Aufgabe4_noninteractive.txt leeren
    writefile = open("Aufgabe4_noninteractive.txt", "w")
    writefile.truncate()
    writefile.close()

    writefile = open("Aufgabe4_noninteractive.txt", "w")    #öffne writefile
    eingabedatei = open(datei, "r")                         #öffne eingabedatei
    for thing in eingabedatei.readlines():                  #für jede line in eingabedatei
        satz = word_tokenize(thing)                         #line tokenizen
        tags = st.tag(satz)                                 #tags liste erstellen
        writefile.write("\n\n" + str(thing))                #tags liste in datei schreiben
        for tup in tags:                                    #für jedes tupel in der liste tags
            if tup[1] == "O":                               #wenn value O ist
                writefile.write(str((tup[0] + " ")))        #schreibe key
            else:                                           #ansonsten
                with open("Over200.txt", encoding="utf-8") as readfile:         #öffne Over200.txt
                    for line in readfile:                                       #für jede line darin
                        list1 = re.findall(reg, line)                           #regexe finden
                        for item in list1:                                      #für jedes item in liste aus regexen
                            if tup[0] == item[4]:                               #wenn key = eingabetext
                                list2.append((item[2], int(item[0])))           #liste 2 erstellen mit anzahl und wikiartikel
                if list2:                                                       #wenn etwas in liste2 steht
                    #ersten(und damit höchsten) key mit artikelname in writefile schreiben
                    writefile.write(str("[[" + (sorted(list2, key=lambda x: x[1], reverse=True)[0][0] + "|" + tup[0] + "]] ")))
                    list2.clear()                                               #liste2 leeren
                else:                                                           #sonst
                    writefile.write(str((tup[0] + " ")))                        #key einfach schreiben

