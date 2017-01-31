'''

[[link | text]]

* look for first first [[ in line
* look for | marker for text beginning
* look for ]]

**. Drop if newlines in link
**. If newline in text add space see wiki
**. Drop if nested [[Text1[[Text2]]Text3]], in this case take only internal one
**. Drop if anchors - that means link begins with #, because it is not possible to clarify page url
**. Drop if links to internal subpage - that means link begins with /, because it is not possible to clarify page url

***. Parse text until ]] or [[ or end of file
***. If text is empty => text = link

TODO:
now just ignoring

**. Magic links? {{}}
**. Repetitive |

Alternative approach:
Use this regex string for detection
 [\[][\[]([^\|\n]*)(\|([^\]]+))*[\]][\]]
need to be extended for corner cases
Possible execution speed advantage?

'''

import time
start_time = time.time()

with open("Linktext.txt", "w", encoding="utf-8") as writefile:
    with open("wikilinks_en.txt", encoding="utf-8") as readfile:
        foundLinkBeg = False
        hasText = False
        linkText = ""
        textText = ""
        prevChar = ""

        for line in readfile:
            for ch in line:
                if ch == "\n":
                    break

                if prevChar == "[" and ch == "[":
                    foundLinkBeg = True
                    hasText = False
                    linkText = ""
                    textText = ""
                    continue
                if prevChar == "]":
                    if ch == "]":
                        if foundLinkBeg is True:
                            if hasText is True and textText != "":
                                writefile.write(linkText + "\t" + textText + "\n")
                            else:
                                writefile.write(linkText + "\t" + linkText + "\n")
                        foundLinkBeg = False
                        hasText = False
                    else:
                        if hasText is True:
                            textText += "]"
                        else:
                            linkText += "]"
                    continue

                prevChar = ch

                if ch == "]":
                    continue

                if foundLinkBeg is True:
                    if ch == "|":
                        hasText = True
                        continue
                    if hasText is True:
                        textText += ch
                        continue
                    if linkText == "":
                        if ch == "#" or ch == "/":
                            foundLinkBeg = False
                            hasText = False
                    linkText += ch

            if hasText is False:
                foundLinkBeg = False
                linkText = ""
                textText = ""
                prevChar = ""
            else:
                textText += " "
                prevChar = " "

print("Running time: %d:%d" % (((time.time() - start_time)/60), ((time.time() - start_time)%60)))
