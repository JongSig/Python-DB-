inFp = None
inStr = ""

inFp = open("D:/코드/파이썬DB/5장/TXT/data1.txt", "r", encoding="utf-8")

inStr = inFp.readline()
print(inStr, end = "")

inStr = inFp.readline()
print(inStr, end = "")
inStr = inFp.readline()
print(inStr, end = "")

inFp.close()
