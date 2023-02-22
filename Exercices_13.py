
liste_voyelle = ['a','e','i','o','u']
def nbr_voy_et_conson(tab, n = 0):
    a = -1 if tab[n] in liste_voyelle else 1
    if n == len(tab)-1:
        return a
    else:
        return a+ nbr_voy_et_conson(tab, n +1)
 
def compt(tab):
    nbre = nbr_voy_et_conson(tab)
    if nbre>0:
        return "ici, les consonnes depassent les voyelles de ", nbre
    elif nbre<0:
        return " ici, les voyelles depassent les consonnes de ",abs(nbre)
    else:
        return "ici, il y a egalité"
 
les_mots = []
print("entrer les mots ")
for i in range(3):
    print("mot ",(i+1))
    
    a=input()
    les_mots.append(a)
for i in les_mots:
    print (compt(i), i)
