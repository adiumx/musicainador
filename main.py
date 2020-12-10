import re
def escalas(raiz, ton):
    datos = ["C","C#","D","D#","E","F","F#","G","G#","A","A#","B"]
    ndatos = [1,2,3,4,5,6,7,8,9,10,11,12]
    nl = []
    n = datos.index(raiz)
    datos1 = []

    for i in range(len (ton)):
        pass
        if ton[i]=='T':
            pass
            nl.append(2)
        else:
            pass
            nl.append(1)
        
    for i in range(len (ton)):
        pass
        if n>=12:
            pass
            n=n % 12

        datos1.append(datos[n])
        n=n+nl[i]
        
    return datos1
    
    
def acordes(raiz, tipo):
    """
    docstring
    """
    pass
    M=["T", "T", "st" ,"T", "T", "T" ,"st" ]#escala mayor
    datos = ["C","C#","D","D#","E","F","F#","G","G#","A","A#","B"]
    ndatos = [1,2,3,4,5,6,7,8,9,10,11,12]
    datosc = []
    el = " "
    num = 0
    n = datos.index(raiz)
    acorde = []
    for i in range(len (datos)):
        pass
        if n>=12:
            pass
            n=n % 12
        datosc.append(datos[n])
        n+=1
    escala=escalas(raiz, M)
    print(tipo)
    for i in range(len(tipo)):
        pass
        regex = r"\d+"
        test_str = "".join(tipo[i])
        
        matches = re.finditer(regex, test_str, re.MULTILINE)

        for matchNum, match in enumerate(matches, start=1):
            
            print ("".format(matchNum = matchNum, start = match.start(), end = match.end(), match = match.group()))
            
            for groupNum in range(0, len(match.groups())):
                groupNum = groupNum + 1
                
                print ("".format(groupNum = groupNum, start = match.start(groupNum), end = match.end(groupNum), group = match.group(groupNum)))
        print(test_str[match.start():match.end()])
        regex1 = r"\D+"

        matches = re.finditer(regex1, test_str, re.MULTILINE)

        for matchNum, match in enumerate(matches, start=1):
            
            print ("".format(matchNum = matchNum, start = match.start(), end = match.end(), match = match.group()))
            
            for groupNum in range(0, len(match.groups())):
                groupNum = groupNum + 1
                
                print ("".format(groupNum = groupNum, start = match.start(groupNum), end = match.end(groupNum), group = match.group(groupNum)))
            print(test_str[match.start():match.end()])
    return acorde
    
M=["T", "T", "st" ,"T", "T", "T" ,"st" ]#escala mayor
m=["T", "st", "T", "T", "st", "T", "T"]#escala menor
quinta=["0","4"]
mayor=["0","2","4"]
menor=["0","2b","4"]
aumentado=["0","2","4#"]
disminuido=["0","2b","4b"]
cuartasuspendida=["0","3","4"]
segundasuspendida=["0","1","4"]
septima=["0","2","4","6b"]
septimamayor=["0","2","4","6"]
sexta=["0","2","4","5"]
sextamenor=["0","2b","4","5"]
septimamenor=["0","2b","4","6b"]
septimamenorquintabemol=["0","2b","4b","6b"]
septimadisminuido=["0","2b","4b","5"]
novenaanadida=["0","2","4","1"]
menorseptimamayor=["0","2b","4","6"]
septimamayorquintaaumentada=["0","2","4#","6"]
septimaquintaaumentada=["0","2","4#","6b"]
septimaquintadisminuida=["0","2","4b","6b"]
septimamayornovena=["0","2","4","6","8"]
septimanovena=["0","2","4","6b","8"]
septimamenornovena=["0","2b","4","6b","8"]
septimanovenaaumentada=["0","2","4","6b","8#"]
septimanovenamenor=["0","2","4","6b","8b"]
sextanovena=["0","2","4","5","8"]
septimamayornovenaoncena=["0","2","4","6","8","10"]
#pentatonica menor se elimina la segunda y la sexta nota de la escala menor
raiz = "C"
escala=escalas(raiz, M)
print(escala)
acorde=acordes(raiz, menor)
print(acorde)