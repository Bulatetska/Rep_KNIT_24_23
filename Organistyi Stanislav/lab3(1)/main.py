spysok = list(range(5))
i = 0
while(i < len(spysok)):
   if (spysok[i] % 2 == 0):
      spysok.remove(spysok[i])
      i+=1
print(spysok)