def stampa_matrice(matrice):
    for riga in matrice:
        print(" ".join(str(x) for x in riga))

# ESERCIZIO 1
# Scrivere una funzione leggi_esegui(n), che dato un intero n, 
# legge una matrice n×n in input e restituisce la somma di tutti gli elementi.

def leggi_esegui(n):
    matrice = []
    for i in range(n):
        riga = []
        for j in range(n):
            elemento = int(input(f"Inserisci l'elemento [{i}][{j}] della matrice: "))
            riga.append(elemento)
        matrice.append(riga)

    somma = 0
    for i in range(n):
        for j in range(n):
            somma += matrice[i][j]

    return somma

def leggi_esegui_1(n):
    matrice = []
    for i in range(n):
        riga = input(f"Inserisci la riga {i} della matrice (elementi separati da spazio): ")
        riga = riga.split() #[lista di stringhe!!!!]
        if len(riga) != n:
            print(f"Errore: la riga {i} deve contenere esattamente {n} elementi.")
            return None
        riga = [int(x) for x in riga]
        matrice.append(riga)

    somma = 0
    for i in range(n):
        for j in range(n):
            somma += matrice[i][j]
    return somma

# ESERCIZIO 2
# Scrivere una funzione somma_righe(M) che dato una matrice M
# restituisce un vettore con la somma di ogni riga.
# Se la matrice M è la seguente:
# M = [[1, 2, 3],
#      [4, 5, 6],
#      [7, 8, 9]]
# La funzione deve restituire il seguente vettore:
# [6, 15, 24]

def somma_righe(M):
    somma = []
    for riga in M:
        somma.append(sum(riga))
    return somma


#ESERCIZIO 3
# Scrivere una funzione trasposta(M) che data una matrice
# M restituisce la matrice trasposta di M.
# Se la matrice M è la seguente:
# M = [[1, 2, 3],
#      [4, 5, 6],
#      [7, 8, 9]]
# La funzione deve restituire la seguente matrice:
# [[1, 4, 7],
#  [2, 5, 8],
#  [3, 6, 9]]

def trasposta(M):
    trasposta = []
    for i in range(len(M[0])):
        riga = []
        for j in range(len(M)):
            riga.append(M[j][i])
        trasposta.append(riga)
    return trasposta

# ESERCIZIO 4
# Scrivere una funzione prodotto_matrici(A, B) che date due matrici A e B
# ne restituisce il prodotto A×B..
#
# Regola: l'elemento C[i][j] del risultato è la somma dei prodotti
# degli elementi della riga i di A per gli elementi della colonna j di B:
#   C[i][j] = A[i][0]*B[0][j] + A[i][1]*B[1][j] + ... + A[i][k]*B[k][j]
#
# Esempio:
# A = [[1, 2],        B = [[5, 6],
#      [3, 4]]             [7, 8]]
#
# C[0][0] = 1*5 + 2*7 = 19   C[0][1] = 1*6 + 2*8 = 22
# C[1][0] = 3*5 + 4*7 = 43   C[1][1] = 3*6 + 4*8 = 50
#
# Output: 
# [[19, 22], 
#  [43, 50]]
 
def prodotto_matrici(A, B):
    righe_A = len(A)
    colonne_A = len(A[0])
    righe_B = len(B)
    colonne_B = len(B[0])
 
    if colonne_A != righe_B:
        print("Errore: dimensioni incompatibili per il prodotto.")
        return 0
 
    # Inizializza la matrice risultato con tutti zeri
    C = []
    for i in range(righe_A):
        riga = []
        for j in range(colonne_B):
            riga.append(0)
        C.append(riga)
 
    # Calcola ogni elemento C[i][j]
    for i in range(righe_A):
        for j in range(colonne_B):
            for k in range(colonne_A):        # colonne_A == righe_B
                C[i][j] += A[i][k] * B[k][j]


#ESERCIZIO 1 APPELLO 31/03/23
# Si scriva una funzione contenuto(V,W) che dato un vettore V ed un vettore W
# restituisce True se tutti gli elementi di V sono presenti in W, False altrimenti.
# Esempio:
# V = [-2.1, 15.4, 2.1, -7.5] e 
# W = [-7.5, 6.3, -111.7, 2.1, 46.2, -22.5, 15.4, -7.7, -10.7, 9.9]
# La funzione restituisce true.

def contenuto(V, W):
    for elemento in V:
        if elemento not in W:
            return False
    return True

# ESERCIZIO 2 APPELLO 31/03/23
# Data una matrice quadrata M di interi di dimensione n x n con n dispari, 
# si scrivano i seguenti metodi:

# 1. prod, che riceve M ed una posizione di cella (i,j) e 
# restituisce il prodotto degli elementi di M che si trovano nella
# riga i e nella colonna j di M.

# 2. check, che riceve M ed un indice di riga 'i' e restituisce true se 
# il vettore riga i-simo contiene tutti elementi distinti; altrimenti restituisce false.

# 3. leftTriangle, che riceve M, e restituisce un vettore contenente gli elementi situati 
# nel triangolo aventi come base la prima colonna e come vertice opposto alla base 
# l'elemento centrale di M.

# 4. main che legge da input una matrice di interi di dimensione n x n (con n dispari), invoca i metodi definiti ai punti
# 1, 2 e 3 e ne stampa il risultato.

# Esempio per 2 e 3
#  3   66   13   22    7 
#  8    0   24    2   16 
#  4   21    9   14   23 
# [17] [5] [25] [8] [11] <--- Riga i=3
#  6   20   12   18    5 

# -----------------------------------------------------------------------------------------
# Esempio per 3:
# #3#  66   13   22    7 
# #8#  #0#  24    2   16 
# #4#  #21# #9#  14   23   <--- 9 è l'elemento centrale
# #17# #5#  25    8   11 
# #6#  20   12   18    5 

def prod(M, i, j):
    n = len(M)
    prodotto = 1
    for k in range(n):
        prodotto = prodotto * M[i][k]
    for k in range(n):
        if k != i :
            prodotto = prodotto * M[k][j]
    return prodotto

def check(M, i):
    riga = M[i]
    for j in range(len(riga)):
        for k in range(j + 1, len(riga)):
            if riga[j] == riga[k]:
                return False  # Trovato un duplicato
    return True  # Nessun duplicato trovato


def leftTriangle(M):
    n = len(M)
    centro = n // 2
    risultato = []

    # Parte 1: dalla prima riga fino al centro (incluso)
    for i in range(centro + 1):
        for j in range(i + 1):
            risultato.append(M[i][j])

    # Parte 2: dal centro+1 fino all’ultima riga
    k = centro - 1
    for i in range(centro + 1, n):
        for j in range(k + 1):
            risultato.append(M[i][j])
        k -= 1  # diminuisco ogni volta

    return risultato

def leftTriangle(M):
    n = len(M)              # n è il numero di righe (e colonne)
    risultato = []
    for j in range(n):
            for i in range(j,n-j):
                risultato.append(M[i][j])

    return risultato

#main che richiama il tutto
def main():
    n = int(input("Inserisci la dimensione n della matrice (n dispari): "))
    if n % 2 == 0:
        print("Errore: n deve essere dispari.")
        return

    M = []
    for i in range(n):
        riga = input(f"Inserisci la riga {i} della matrice (elementi separati da spazio): ")
        riga = riga.split()
        if len(riga) != n:
            print(f"Errore: la riga {i} deve contenere esattamente {n} elementi.")
            return
        riga = [int(x) for x in riga]
        M.append(riga)

    # Esempio di utilizzo dei metodi
    i, j = 1, 1  # Posizione di cella per il prodotto
    print(f"Prodotto degli elementi nella riga {i} e colonna {j}: {prod(M, i, j)}")
    
    i_check = 2  # Indice di riga per il check
    print(f"Riga {i_check} contiene tutti elementi distinti? {check(M, i_check)}")
    
    print(f"Elementi nel triangolo sinistro: {leftTriangle(M)}")

if __name__ == "__main__":
    main()