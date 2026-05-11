# ESERCIZIO 2
# Data una matrice quadrata M di interi, 
# di dimensione nxn con n dispari, si scrivano
# le seguenti funzioni:
# product, che riceve M ed una posizione di cella (i,j),
# e restituisce il prodotto degli elementi che si trovano
# nella riga i e nella colonna j di M.

def product(M, i, j):
    prodotto = 1
    for k in range(len(M)):
        if k!= j: #consideriamo l'elemento in comune una sola volta
            prodotto *= M[i][k]
        prodotto *= M[k][j]
    return prodotto

# ESERCIZIO 2.2
# Si scriva una funzione verifica che, data una matrice M, 
# ed una posizione di cella (i,j), 
# restituisce true se la somma degli elementi di M
# che si trovano nella riga i è minore del massimo 
# valore contenuto nella colonna j,
# altrimenti restituisce false.

def verifica(M, i, j):
    n = len(M)
    somma = 0
    for k in range(n):
        somma += M[i][k]

    massimo = M[0][j]
    for k in range(1, n):
        if M[k][j] > massimo:
            massimo = M[k][j]
    return somma < massimo

#ESERCIZIO 2.3
# Si scriva una funzione che, data una matrice M,
# restituisce una lista contenete gli elementi 
# situati nel triangolo aventi come base la prima riga
# e come vertice opposto alla base l'elemento centrale
# di M (si veda l'esempio sottostante, in cui il triangolo è
# evidenziato in grigio).

def sopra(M):
    n = len(M)
    ris = []
    centro = n // 2
    for i in range(centro + 1):
        for j in range(i, n - i):
            ris.append(M[i][j])
    return ris

M = [
    [3, 86, 13, 22, 7],
    [15, 0, 24, 2, 16],
    [4, 21, 9, 14, 23],
    [17, 5, 25, 8, 11],
    [6, 20, 12, 18, 5]
]
print(product(M, 3, 1))
print(verifica(M, 3, 1))
print(sopra(M))