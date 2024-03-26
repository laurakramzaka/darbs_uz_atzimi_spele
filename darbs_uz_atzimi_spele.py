from random import randint
TGREEN =  '\033[32m'
ENDC = '\033[m'
TRED = '\033[31m'

pareizas_atbildes = 0
spele_noteikumi = False

def atminet_vardu(dziesmas_teksts, pareizais_vards):
    global pareizas_atbildes
    global spele_noteikumi
    print("\t")
    print("\t")
    if not spele_noteikumi:
            print("Sveicināts dziesmu rindiņas viena trūkstošā vārda spēlē! Tev vajadzēs ievadīt savu minējumu atkarība no dziesmas teksta! Kopa ir 8 jautājumi. \n")
            spele_noteikumi = True
        
    vardi = dziesmas_teksts.split()
    for i, vards in enumerate(vardi):
        if '_' in vards:
            print(" ".join(vardi[:i]) + " ____ " + " ".join(vardi[i+1:]))
            minejums = input("Ievadiet savu minējumu: ")
            print("\t")
            if minejums.lower() == pareizais_vards.lower():
                print(TGREEN + "Pareizi!😎", ENDC)
                pareizas_atbildes += 1
                print("\t")
            else:
                print(TRED + "Nepareizi👎", ENDC + "Pareizā atbilde ir:", pareizais_vards)
                print("\t")

dziesmas_teksts_1 = "Un es skrienu, skrienu vēl, man vēl ________"
pareizais_vards_1 = "jāpaspēj"

dziesmas_teksts_2 = "Liku ____ zem akmeņa"
pareizais_vards_2 = "bēdu"     

dziesmas_teksts_3 = "_________, kam tu mīti purviņā?"
pareizais_vards_3 = "Dzērvenīt"  

dziesmas_teksts_4 = "Kur tu teci, kur tu teci, _______ mans?"
pareizais_vards_4 = "gailīti"   

dziesmas_teksts_5 = "_______ iekrita tevī"
pareizais_vards_5 = "Debesis"   

dziesmas_teksts_6 = "Ieklausies Ģenoveva.Es gribu būt tavs nelabais. Nelabais ____ labais"
pareizais_vards_6 = "labu"   

dziesmas_teksts_7 = "Saule _____ sēdināja"
pareizais_vards_7 = "latvi"   

dziesmas_teksts_8 = "Sāp naktī ________ sirds"
pareizais_vards_8 = "salauzta"   



atminet_vardu(dziesmas_teksts_1, pareizais_vards_1)
atminet_vardu(dziesmas_teksts_2, pareizais_vards_2)
atminet_vardu(dziesmas_teksts_3, pareizais_vards_3)
atminet_vardu(dziesmas_teksts_4, pareizais_vards_4)
atminet_vardu(dziesmas_teksts_5, pareizais_vards_5)
atminet_vardu(dziesmas_teksts_6, pareizais_vards_6)
atminet_vardu(dziesmas_teksts_7, pareizais_vards_7)
atminet_vardu(dziesmas_teksts_8, pareizais_vards_8)

print("Kopā pareizas atbildes:", pareizas_atbildes)


