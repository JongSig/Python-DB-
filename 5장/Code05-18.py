inFp = None
inStr = ""

inFp = open("D:/코드/파이썬DB/5장/TXT/data1.txt", "r", encoding="utf-8")

i = 1
while(True):
    inStr = inFp.readline()
    if inStr == "":
        break
    print("%d %s %s" %(i,":", inStr), end = "")
    i = i + 1

inFp.close()
