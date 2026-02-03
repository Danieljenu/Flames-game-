    b=input("Enter your name ")
    g=input("Enter your partner name")
    el1=[]
    el2=[]
    for e1 in b:
        el1.append(e1)
    for e2 in g:
        el2.append(e2)
    print(el1,el2)
    #for removing comman thing in the listi
    for f in el1[:]:          # iterate over a COPY
        if f in el2:
            el1.remove(f)
            el2.remove(f)
    oflame=len(el1)+len(el2)
    n=0
    def jok():
        global flame
        while True:
            if len(l)<flame:
                flame=-len(l)
            else:
                l.pop(flame-1)
                n=flame
                flame=oflame
    l=['F','L','A','M','E','S']
    flame=oflame
    while len(l)>=2:
        if n==0:
            jok()
        else:
            flame=-n
            jok()
