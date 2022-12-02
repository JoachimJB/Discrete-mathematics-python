#Oppgaver kapittel 4

def oppg_4_1_8():
    for a in range(1,10):
        for b in range(1,10):
            for c in range(1,10):
                if(b % a != 0 and c % a != 0 and b*c % a == 0):
                    print(a, b, c)    
                    
def oppg_4_1_37():
    m = 2
    for a in range(1,10):
        for b in range(1,10):
            for c in range(1,10):
                if((a*c-b*c) != 0 and (a*c-b*c) % m == 0 and (a-b) % m != 0):
                    print("m: ", m, "a: ", a, "b: ",b, "c: ",c)
    
def rest_kvot(a, b):
    rest = a % b
    Kvotient = a // b
    print ("a og b gir: kvotient:",Kvotient,"og rest:",rest)

#oppg_4_1_8()
#oppg_4_1_37()
rest_kvot(1529, 14038)
