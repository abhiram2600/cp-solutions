def findnumber(s):
    mi = min(s)
    k = s.find(mi)
    fir = s[:k]
    las = s[k:]
    ss = las + fir
    return ss
for _ in range(int(input())):
    n = int(input())
    s = input()
    k=findnumber(s)
    for i in range(k,len(ss)):
        if ss[i]==s[i]:
            pass
        else:
            if ascii(ss[i])>ascii(s[i]):

                =findnumber(k,s)
    print(ss)
    print(k + 1)
