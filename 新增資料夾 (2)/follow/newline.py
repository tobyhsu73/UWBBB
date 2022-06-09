fp1 = open("lidardata3.txt", "r", encoding="utf8")
s1 = fp1.read(100)
while(s1):
    s2 = s1.replace("}", "}\n")
    with open("lidardata4.txt", "a", encoding="utf8") as fp2:
        fp2.write(s2)
        print(s2,end='')
    s1 = fp1.read(100)
fp1.close()
print('OK')