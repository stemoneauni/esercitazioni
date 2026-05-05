##### ESERCIZIO SULLE LISTE #####

# Si scriva una funzione Python avente come nome presente that 
# riceve in ingresso due liste a e b, e restituisce una lista
# contenente ogni elemento di a che compare col quadruplo del 
# suo valore in b.
# Si faccia in modo che la lista risultante contenga numeri distinti.

# Esempio:
# Se a = [2.1, 15.4, 2.1, -2.5, 28.9, 15.3, 665.0, 3.0] e 
# b = [8.4, -111.7, 61.6, -10.0, -7.7, -10.7, 12.0] 
# allora la funzione presente restituirà la seguente lista 
# [2.1, 15.4, -2.5, 3.0] 
# perchè il quadruplo di 2.1 (ossia 8.4) è presente in b; 
# il quadruplo di 15.4 (ossia 61.6) è presente in b; 
# il quadruplo di -2.5 (ossia -10.0) compare in b; 
# il quadruplo di 3.0 (ossia 12.0) compare in b.

def presente(a,b):
    ris = []
    for x in a:
        if x not in ris and 4*x in b:
            ris.append(x)
    return ris


# Si scriva una funzione Python avente come nome combinazioni_valide 
# che riceve in ingresso tre liste a, b e c contenenti numeri interi, 
# e restituisce una lista contenente tutti gli elementi 
# x di a per cui esistono almeno un elemento
# y in b e un elemento z in c tali che x = y + z.
#
# Si faccia in modo che la lista risultante contenga numeri distinti
# e mantenga l’ordine di prima occorrenza degli elementi in a.
#
# Esempio:
# Se a = [5, 10, 7, 3, 15, 10, 8] 
#    b = [2, 4, 6, 9]
#    c = [1, 3, 5, 9]
# allora la funzione combinazioni_valide restituirà la seguente lista
# [5, 10, 7, 3, 15]
#
# perchè:
# 5 = 2 + 3
# 10 = 9 + 1
# 7 = 2 + 5 o 7 = 4 + 3
# 3 = 2 + 1
# 15 = 9 + 6
#
# 8 non va incluso perché non esistono y in b e z in c tali che y + z = 8

def combinazioni_valide(a, b, c):
    risultato = []

    for x in a:
        trovato = False

        # controllo se esiste almeno una coppia (y, z)
        for y in b:
            for z in c:
                if x == y + z:
                    trovato = True
                    break
            if trovato:
                break

        # aggiungo x solo se:
        # 1. ho trovato una combinazione valida
        # 2. non è già presente nel risultato (niente duplicati)
        if trovato and x not in risultato:
            risultato.append(x)

    return risultato


a = [5, 10, 7, 3, 15, 10, 8] 
b = [2, 4, 6, 9]
c = [1, 3, 5, 9]
print(combinazioni_valide(a, b, c))

####### MATRICI #######

# ESERCIZIO 1
# Si scriva la funzione colonneSimmetriche 
# che riceve una matrice quadrata M e stampa su video 
# gli indici delle colonne di M che risultino simmetriche. 
# Per maggiore chiarezza si veda l'esempio.

def colonneSimmetriche(M):
    n = len(M)
    for i in range(n):
        simmetrica = True
        for j in range(n // 2):
        # Verifico la simmetria
            if M[j][i] != M[n - j - 1][i]:
                simmetrica = False
                break
        # Stampo l'indice della colonna simmetrica
        if simmetrica:
            print(i)

# ESERCIZIO 2
# Si scriva la funzione creaVettore che riceve una 
# matrice quadrata M e restituisce un array 
# (avente dimensione pari al lato di M) che contiene, 
# in posizione i, il minimo tra la somma degli elementi
#  posti sulla riga i di M e la somma degli elementi 
# posti sulla colonna i di M.
def creaVettore(M):
    n = len(M)
    v = []
    for i in range(n):
        sommaRiga = 0
        sommaColonna = 0
        # Calcolo la somma della riga e della colonna i-esima
        for j in range(n):
            sommaRiga += M[i][j]
            sommaColonna += M[j][i]
        # Calcolo il minimo tra le somme e lo assegno a v[i]
        if sommaRiga <= sommaColonna:
            v.append(sommaRiga)
        else:
            v.append(sommaColonna)
    return v

# ESERCIZIO 3
# Si scriva la funzione elaboraMatrice che 
# riceve una matrice di interi M, e restituisce 
# una matrice A ottenuta da M eliminando
# la prima colonna e l’ultima riga
def elaboraMatrice(M):
    nuova_matrice = []
    for i in range(len(M) - 1): # esclude l'ultima riga
        nuova_riga = []
        for j in range(1, len(M[i])): # esclude la prima colonna
            nuova_riga.append(M[i][j])
            nuova_matrice.append(nuova_riga)
    return nuova_matrice


def main():
    n = int(input("Inserisci la dimensione della matrice quadrata: "))
    M = []
    for i in range(n):
        riga = []
        for j in range(n):
            valore = int(input("Inserisci l'elemento: "))
            riga.append(valore)
            M.append(riga)
    colonneSimmetriche(M)
    vettore = creaVettore(M, n)
    print("Vettore creato:", vettore)
    nuova_matrice = elaboraMatrice(M)
    print("Matrice elaborata (senza prima colonna e ultima riga):")
    for riga in nuova_matrice:
        print(riga)

main()