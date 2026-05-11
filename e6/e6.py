# APPELLO DEL 19 FEBBRAIO 2026

# ESERCIZIO 1
# Si scriva una funzione Python avente nome almenoK
# che riceve in ingresso due liste L1 e l2, ed un intero k,
# e restituisce una lista contenente ognli elemento di L1
# che compare almeno k volte in L2.
# Si faccia in modo che la lista risultate contenga
# numeri distinti.

# Esempio:
# Se L1 = [2.1, 15.4, 2.1, -2.5, 28.9, 15.3, 665.0, 3.0] e
# L2 = [2.1, 2.1, 2.1, 15.4, -111.7, 2.1] e k = 3
# allora la funzione almenoK restituirà la seguente lista
# [2.1] perchè solo il numnero 2.1 compare almeno 3 volte 
# (4 per la precisione) in L2.

def almenoK(L1,L2,k):
    ris = []
    for i in range(len(L1)):
        count = 0
        for j in range(len(L2)):
            if L1[i] == L2[j]:
                count += 1
        if count >= k and L1[i] not in ris:
            ris.append(L1[i])
    return ris

print(almenoK([2.1, 15.4, 2.1, -2.5, 28.9, 15.3, 665.0, 3.0], [2.1, 2.1, 2.1, 15.4, -111.7, 2.1], 3))

# ESERCIZIO 2.1
# Data una matrice quadrata M di interi di dimensione
# nxn con n dispari, si scriva la seguente funzione Python:
# corners, che riceve M ed una posizione di cella (i,j) e 
# restituisce la somma tra l'elemento in posizione (i,j)
# e la somma dei quattro elementi situati agli angoli della matrice.

def corners(M, i, j):
    n = len(M)
    elemento_i_j = M[i][j]
    corner_sinistro_sopra = M[0][0]
    corner_destro_sopra = M[0][n-1]
    corner_sinistro_basso = M[n-1][0]
    corner_destro_basso = M[n-1][n-1]

    return elemento_i_j + corner_sinistro_sopra + corner_destro_sopra + corner_sinistro_basso + corner_destro_basso

# ESERCIZIO 2.2
# Data una matrice quadrata M di interi di dimensione
# nxn con n dispari, si scriva la seguente funzione Python:
# rowVScenter, che riceve M ed un indice di riga i. Restituisce
# True se il numero degli elementi dispari contenuti nella riga i
# è minore del numero di elementi pari contenuti nella colonna 
# centrale della matrice, False altrimenti.

def rowVScenter(M, i):
    n = len(M)
    n_dispari = 0
    for j in range(n):
        if M[i][j] % 2 != 0:
            n_dispari += 1
    
    n_pari = 0
    centro = n // 2
    for k in range(n):
        if M[k][centro] % 2 == 0:
            n_pari += 1

    return n_dispari < n_pari

# ESERCIZIO 2.3
# Data una matrice quadrata M di interi di dimensione
# nxn con n dispari, si scriva la seguente funzione Python:
# diagonals, che riceve M e restituisce la diagonale (tra principale e secondaria)
# la cui somma degli elementi è maassima.

def diagonals(M):
    n = len(M)
    diagonale_principale = []
    somma_p = 0
    for i in range(n):
        diagonale_principale.append(M[i][i])
        somma_p += M[i][i]
    
    diagonale_secondaria = []
    somma_s = 0
    for j in range(n):
        diagonale_secondaria.append(M[j][n-1-j])
        somma_s += M[j][n-1-j]
    
    if somma_p >= somma_s:
        return diagonale_principale
    else:
        return diagonale_secondaria


def main():
    n = int(input("Inserisci la dimensione della matrice quadrata: "))
    M = []
    for i in range(n):
        riga = []
        for j in range(n):
            valore = int(input("Inserisci l'elemento: "))
            riga.append(valore)
        M.append(riga)
    
    print(corners(M, 3, 1))
    print(rowVScenter(M, 1))
    print(diagonals(M))

"""
M = [
    [3, 86, 13, 22, 7],
    [15, 0, 24, 2, 16],
    [4, 21, 9, 14, 23],
    [17, 5, 25, 8, 11],
    [6, 20, 12, 18, 5]
]

print(corners(M, 3, 1))
print(rowVScenter(M, 1))
print(diagonals(M))
"""
