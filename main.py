import code as codelang

print("Hello this is secret language chat")
codein = input("Press \"C\" to code and \"DC\" to decode: ")
inpp= input("Enter the sentence or word you want to code/decode: ")
cinpp= inpp.split()

if codein.lower()=="c":                          # code
    for i in range(len(cinpp)):
        if len(cinpp[i])>3:
            cinpp[i]= codelang.final(cinpp[i])    
    yo = " ".join(codelang.coder(cinpp))
    print(yo)


elif codein.lower()=="dc":                      #decode
    for i in range(len(cinpp)):
        if len(cinpp[i])>3:
            cinpp[i] =cinpp[i][3:-3]
    yo = " ".join(codelang.coder(cinpp))
    print(yo)

