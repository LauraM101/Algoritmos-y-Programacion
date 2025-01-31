foráneos = ['k','w','x','y']
palabras = ['vaquero','whiskey','gorra','mexico','rally']

def remover_palabras(foráneos,palabras):
    for c in foráneos:
        for p in palabras:
            if c in p:
             palabras.remove(p)

    return palabras

print(remover_palabras(palabras))


cocacola = [80,100,93,99,101,102,95,110,109,120,125,130]
cont= 0
rallies=[]
def contador(cocacola):
    for i in range(len(cocacola)):
        if i ==0:
            cont +=1
        elif cocacola[i] > cocacola [i -1]: #[i-1] es para revisar el valor anterior
            cont +=1
        else:
            rallies.append(cont)
            cont= 0
    return (max(rallies))

print(contador(cocacola))
