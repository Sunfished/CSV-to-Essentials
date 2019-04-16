import csv



######
startNum = 650
######

#adds a new line to pokedex.txt based on the variables needed
def addVar(name,l,ind,col,default):
    word = name + default
    if l[ind][col]:
        word = name + l[ind][col]
    return word

#makes all words undercase and removes spaces
def scrub(word):
    return word.lower().replace(" ","")

#uppercase and removes all characters other than letters and numbers
def internalize(word):
    newword = ""
    for i in word:
        if i.isalpha() or i.isdigit():
            newword+=i
    return newword.upper().replace(" ","")

#returns the column from list l that string c appears
def getCol(l,col):
    for i in range(len(l)):
        if scrub(l[i]) == scrub(col):
            return i

#creates the stat strings based on the list and HP column
def createStats(myList,hpCol):
    s = ""
    for i in range(hpCol,hpCol+6):
        if myList[i] != "" and myList[i].isdigit():
            s += myList[i]
        else:
            s += "1"
        s+=","
    return s[:-1]

#Open Files
baseText = open("pokemonBASE.txt",'r',encoding='utf-8-sig')
baseText = baseText.readlines()
with open('pokemonNEW.csv','rt',encoding="UTF8") as f:
    reader = csv.reader(f)
    fakemonList = list(reader)


newList = []
ind = 1

print("Found the following Titles:")
print(fakemonList[0])

#Get Column Information
nameCol = getCol(fakemonList[0],"name")
type1Col = getCol(fakemonList[0],"type1")
type2Col = getCol(fakemonList[0],"type2")
hpCol = getCol(fakemonList[0],"hp")
genderCol = getCol(fakemonList[0],"genderrate")
growthCol = getCol(fakemonList[0],"growthrate")
expCol = getCol(fakemonList[0],"exp")
effortCol = getCol(fakemonList[0],"ehp")
catchCol = getCol(fakemonList[0],"catch")
happyCol = getCol(fakemonList[0],"happy")
ability1Col = getCol(fakemonList[0],"ability1")
ability2Col = getCol(fakemonList[0],"ability2")
abilityHCol = getCol(fakemonList[0],"abilityh")
egg1Col = getCol(fakemonList[0],"egggroup1")
egg2Col = getCol(fakemonList[0],"egggroup2")
hatchCol = getCol(fakemonList[0],"hatch")
heightCol = getCol(fakemonList[0],"height")
weightCol = getCol(fakemonList[0],"weight")
colorCol = getCol(fakemonList[0],"color")
shapeCol = getCol(fakemonList[0],"shape")
classCol = getCol(fakemonList[0],"class")
habitatCol = getCol(fakemonList[0],"habitat")
pokedexCol = getCol(fakemonList[0],"pokedex")
evolutionCol = getCol(fakemonList[0],"evolution")
evotypeCol = getCol(fakemonList[0],"evotype")
evodataCol = getCol(fakemonList[0],"evodata")

#Create Addendum
while(fakemonList[ind][nameCol]):
    newList.append("#-------------------------------")
    newList.append("[" + str(startNum) + "]")
    
    newList.append("Name="+fakemonList[ind][nameCol])
    newList.append("InternalName="+internalize(fakemonList[ind][nameCol]))
    
    newList.append(addVar("Type1=",fakemonList,ind,type1Col,"NORMAL"))
    if fakemonList[ind][type2Col]:
        newList.append("Type2="+internalize(fakemonList[ind][type2Col]))

    #Stats
    newList.append("BaseStats="+createStats(fakemonList[ind],hpCol))

    newList.append(addVar("GenderRate=",fakemonList,ind,genderCol,"FemaleOneEighth"))
    newList.append(addVar("GrowthRate=",fakemonList,ind,growthCol,"Medium"))
    newList.append(addVar("BaseEXP=",fakemonList,ind,expCol,"1"))

    #Effort Points
    newList.append("EffortPoints="+createStats(fakemonList[ind],effortCol))
        
    newList.append(addVar("Rareness=",fakemonList,ind,catchCol,"1"))
    newList.append(addVar("Happiness=",fakemonList,ind,happyCol,"70"))

    #Abilities
    ability = ""
    if fakemonList[ind][ability1Col]:
        ability += internalize(fakemonList[ind][ability1Col])
    else:
        ability += "KLUTZ"
    if fakemonList[ind][ability2Col]:
        ability += "," + internalize(fakemonList[ind][ability2Col])
    newList.append("Abilities=" + ability)
    if fakemonList[ind][abilityHCol]:
        newList.append("HiddenAbility=" + internalize(fakemonList[ind][abilityHCol]))

    #Moves
    newList.append("Moves=1,TACKLE")
    newList.append("EggMoves=CHARM")

    #Egg Groups
    egg = ""
    if fakemonList[ind][egg1Col]:
        egg += fakemonList[ind][egg1Col]
        if fakemonList[ind][egg2Col]:
            egg += "," + fakemonList[ind][egg2Col]
    else:
        egg += "Undiscovered"
    newList.append("Compatibility=" + egg)

    #Hatch Rate
    if fakemonList[ind][hatchCol]:
        newList.append("StepsToHatch=" + fakemonList[ind][hatchCol])
    else:
        newList.append("StepsToHatch=" + "5355")

    newList.append(addVar("Height=",fakemonList,ind,heightCol,"0.1"))
    newList.append(addVar("Weight=",fakemonList,ind,weightCol,"0.1"))
    newList.append(addVar("Color=",fakemonList,ind,colorCol,"White"))
    newList.append(addVar("Shape=",fakemonList,ind,shapeCol,"1"))
    newList.append(addVar("Habitat=",fakemonList,ind,habitatCol,"Rare"))

    #Regional Numbers

    newList.append(addVar("Kind=",fakemonList,ind,classCol,"???"))
    newList.append(addVar("Pokedex=",fakemonList,ind,pokedexCol,"???"))

    #Evolution Handler
    evos = fakemonList[ind][evolutionCol].split(",")
    types = fakemonList[ind][evotypeCol].split(",")
    data = fakemonList[ind][evodataCol].split(",")

    if fakemonList[ind][evolutionCol] and len(evos) == len(types) and len(evos) == len(data):
        evoString = ""
        for i in range(len(evos)):
            evoString += internalize(fakemonList[ind][evolutionCol]) + ","
            evoString += fakemonList[ind][evotypeCol] + ","
            evoString += internalize(fakemonList[ind][evodataCol]) + ","
        newList.append("Evolutions=" + evoString[:-1])
    
    #Iterate Upwards
    ind+=1
    startNum+=1



#write
newText = open("pokemon.txt","w+")

for i in range(len(baseText)):
    newText.write(baseText[i])

for i in range(len(newList)):
    newText.write("\n" + newList[i])

newText.close()
print("Press Enter to exit")
input()
exit()
