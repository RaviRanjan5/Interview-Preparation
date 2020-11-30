""" This is a Insertion Sort Program in Python """


def Insertion(A):
    for i in range(1, len(A)):
        j = i - 1
        min_element = A[i]
        while A[j] > min_element and j >= 0:
            A[j + 1] = A[j]
            j = j - 1
        A[j + 1] = min_element

    return


A = [5, 2, 1, 3, 7]
print(A)
Insertion(A)
print(A)