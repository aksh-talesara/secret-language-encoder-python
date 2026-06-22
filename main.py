import code as codelang

print("Hello this is secret language chat")
codein = input("Press \"C\" to code and \"DC\" to decode: ")
inpp= input("Enter the sentence or word you want to code/decode: ")
cinpp= inpp.split()
if codein.lower()=="c":                          # code
    for ni in range(len(cinpp)):
        if len(cinpp[ni])>=3:
            res = (cinpp[ni][1:] + cinpp[ni][0])
            cinpp[ni] = codelang.final(res)
        elif len(cinpp[ni])<3:
            cinpp[ni]= codelang.coder(cinpp[ni])
            #print(cinpp[ni])
    yo = " ".join(cinpp)
    print(yo)  

     
elif codein.lower()=="dc":                      #decode
    for i in range(len(cinpp)):
        if len(cinpp[i])>=3:
            cinpp[i] =cinpp[i][3:-3]
            cinpp[i]= (cinpp[i][-1:]+cinpp[i][:-1])
        elif len(cinpp[i])<3:
            cinpp[i]= codelang.coder(cinpp[i])
    yo = " ".join(cinpp)
    #yo = " ".join(codelang.coder(cinpp))
    print(yo)
else:
    pass

