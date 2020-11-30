""" This is a Selection Sort Program in Python """


def Selection(A):
    for i in range(len(A)):
        min_index = i
        for j in range(i + 1, len(A)):
            if A[j] < A[min_index]:
                min_index = j
        A[i], A[min_index] = A[min_index], A[i]

    return


A = [5, 2, 1, 3, 7]
print(A)
Selection(A)
print(A)