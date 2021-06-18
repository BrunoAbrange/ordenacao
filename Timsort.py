"""Timsort é um algoritmo de ordenação hibrido desenvolvido por Tim Peters, utiliza o merge sort e o 
insertion sort. Utiliza o que cada um deles faz de melhor, para ter uma boa performace em diversos tipos 
de dados. Primeiro passo ele realiza a divisão dos dados em grupos menores, pois o Insertion sort funciona 
melhor com ordenação de pequenos grupos, após a ordenação desses pequenos grupos utiliza-se o Merge sort 
para ordenação combinando os grupos."""

MIN_MERGE = 32

def calcMinRun(n):
	r = 0
	while n >= MIN_MERGE:
		r |= n & 1
		n >>= 1
	return n + r

def insertionSort(valores, esq, dir):
	for i in range(esq + 1, dir + 1):
		j = i
		while j > esq and valores[j] < valores[j - 1]:
			valores[j], valores[j - 1] = valores[j - 1], valores[j]
			j -= 1

def merge(valores, l, m, r):

	len1, len2 = m - l + 1, r - m
	esq, dir = [], []
	for i in range(0, len1):
		esq.append(valores[l + i])
	for i in range(0, len2):
		dir.append(valores[m + 1 + i])

	i, j, k = 0, 0, l

	while i < len1 and j < len2:
		if esq[i] <= dir[j]:
			valores[k] = esq[i]
			i += 1
		else:
			valores[k] = dir[j]
			j += 1
		k += 1

	while i < len1:
		valores[k] = esq[i]
		k += 1
		i += 1
	while j < len2:
		valores[k] = dir[j]
		k += 1
		j += 1

def timSort(valores):
	tamLista = len(valores)
	minRun = calcMinRun(tamLista)

	for inicio in range(0, tamLista, minRun):
		fim = min(inicio + minRun - 1, tamLista - 1)
		insertionSort(valores, inicio, fim)

	tamBloco = minRun
	while tamBloco < tamLista:
		
		for esq in range(0, tamLista, 2 * tamBloco):

			meio = min(tamLista - 1, esq + tamBloco - 1)
			dir = min((esq + 2 * tamBloco - 1), (tamLista - 1))

			if meio < dir:
				merge(valores, esq, meio, dir)
		tamBloco = 2 * tamBloco

if __name__ == "__main__":

	valores = [-211, 7, 155, -14, 0, 135, 0, 7, -71, -4, -211, 7, 155, -14, 0, 135, 0, 7, -71, -4, -134, 5, 8, -14, 12,111, 23, 45, 11, 23, 31 , 400, 20, 7, 15, -14, 0, 15, 0, 7, -7, -4, -13, 5, 8, -14, 12,111, 23, 45, 32 , -134, 5, 8, -14, 12,111, 23, 45, 11, 23, 31 , 400, 20, 7, 15, -14, 0, 15, 0, 7, -7, -4, -13, 5, 8, -14, 12,111, 23, 45, 32]

	print(valores)
	timSort(valores)
	print(valores)
