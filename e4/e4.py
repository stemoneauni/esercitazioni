# APPELLO DEL 05/07/22
#ESERCIZIO 1
# Si scriva un metodo avente nome multipli che riceve in ingresso
# un vettore (di elementi positivi) V1, e restituisce un
# vettore contenente ogni elemento distinto di V1 tale per
# cui nessun suo multiplo (diverso da se stesso) è presente in V1.
#(N.B. il vettore risultante contiene numeri distinti.)
#Esempio:
#Se V1=[ 2.1, 15.4, 2.1, 7.7] allora l'output sarà [ 2.1, 15.4] 
# perché 2.1 e 15.4 non hanno loro multipli in V1, 
# mentre 15.4 è multiplo di 7.7. 
# N.B. L’elemento 2.1 è presente una sola volta.


def multipli(V1):
    risultato = []
    
    for x in V1:
        if x not in risultato: # considero ogni numero una sola volta nel risultato
            ha_multiplo = False
            
            for y in V1:
                if x != y:
                    # controllo se y è multiplo di x
                    if y % x == 0:
                        ha_multiplo = True
            
            if not ha_multiplo:
                risultato.append(x)
    
    return risultato

V1 = [2.1, 15.4, 2.1, 7.7]
print(multipli(V1))  # Output: [2.1, 15.4]

#ESERCIZIO 2.1
# Data una matrice M di interi di dimensione 
# n x m, si scriva:
# sommaPari, che riceve M e restituisce la somma 
# degli elementi di M che si trovano nelle righe di indice pari 
# (N.B. la prima riga ha indice 0).

def sommaPari(M):
    somma = 0
    for i in range(len(M)):
        if i % 2 == 0: #siamo in una riga pari
            for elemento in M[i]: #sommo tutti gli elementi
                somma += elemento
    return somma

#ESERCIZIO 2.2
# Data una matrice M di interi di dimensione
# n x m, si scriva:
# controlla, che riceve M ed una posizione di cella (i,j) 
# e restituisce true se la somma degli elementi di M che si
# trovano nella colonna j 
# è pari al minimo valore contenuto nella riga i di M; 
# altrimenti restituisce false.

def controlla(M, i, j):
    somma = 0
    for k in range(len(M)):
        somma += M[k][j] #sommo tutti gli elementi della colonna j

    minimo = M[i][0]
    for x in range(1, len(M[i])):
        if M[i][x] < minimo:
            minimo = M[i][x] #trovo il minimo della riga i
    return somma == minimo



#ESERCIZIO 2.3
# Data una matrice M di interi di dimensione 
# n x m, si scriva:
# projection, che riceve M ed un intero k, 
# e restituisce la matrice M’ ottenuta da M eliminando sia le prime k
# colonne che le ultime k colonne di M (si veda l’esempio in figura).

def projection(M, k):
    M1 = [] 
    
    if len(M) == 0:
        return M1
        
    numero_colonne = len(M[0])
    for riga in M:
        # Calcoliamo l'indice in cui dobbiamo fermare il "taglio"
        fine = numero_colonne - k
        nuova_riga = riga[k : fine]
        # Aggiungiamo la riga appena tagliata alla nostra nuova matrice
        M1.append(nuova_riga)
        
    return M1

M = [ [3, 66, 13, 22, -1], [15, 0, 24, 2, -1], [4, 21, 9, 14, -2], [17, -5, 25, 8, -1] ]

print(projection(M, 2))
print(controlla(M, 3, 4))


# APPELLO DEL 03/02/23
#ESERCIZIO 1
# Si scriva un metodo doppio che riceve in ingresso un vettore v,
# e restituisce true se e solo se ogni elemento x di v 
# (tranne l’elemento in ultima posizione) è seguito da un elemento y=2*x.
# Esempio:
# Se v=[ 2.1, 4.2, 8.4, 16.8], allora il metodo doppio restituirà true.
# Qualora invece v=[ 2.1, 4.2, 5.4, 10.8], il metodo
# doppio restituirà false in quanto il valore 4.2 
# non è seguito dall’elemento 8.4 in v.

def doppio(v):
    for i in range(len(v) - 1):
        if v[i]*2 != v[i+1]:
            return False
    return True

#ESERCIZIO 2.1
# Data una matrice quadrata M di caratteri di 
# dimensione n x n con n pari, si scriva:
# sim, che riceve M e restituisce true se e solo se ogni 
# carattere contenuto nella cella avente posizione (i,j) è uguale 
# all’elemento in posizione (j,i) 
# (N.B: la prima riga ha i=0, la prima colonna ha j=0).

def sim(M):
    n = len(M)
    for i in range(n):
        for j in range(i+1, n): # controlla solo metà superiore (j > i)
            if M[i][j] != M[j][i]:
                return False
    return True

# ESERCIZIO 2.2
# Data una matrice quadrata M di caratteri di
# dimensione n x n con n pari, si scriva:
# check, che riceve M e restituisce true se e solo se 
# esistono almeno due vettori riga della matrice M uguali
# (stessi valori nelle stesse posizioni).

def check(M):
    n = len(M)
    for i in range(n - 1): #prendo la prima riga
        riga1 = M[i]
        for j in range(i + 1, n):#confronto le righe successive
            riga2 = M[j]
            if riga2 == riga1:
                return True
    return False

# ESERCIZIO 2.3
# Data una matrice quadrata M di caratteri di
# dimensione n x n con n pari, si scriva:
# tre, che riceve M, e restituisce un vettore contenente 
# gli elementi situati nel triangolo i cui cateti corrispondono
# al primo vettore riga ed al primo vettore colonna, 
# e la cui ipotenusa corrisponde alla diagonale secondaria (si
# veda l’esempio in figura, in cui il triangolo è evidenziato in grigio).

def tre(M):
    n = len(M)
    risultato = []
    for i in range(n):
        for j in range(n - i): #j va da 0 a n-i-1 per rimanere nel triangolo
            risultato.append(M[i][j])    
    return risultato