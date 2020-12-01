def bubble_sort(A, n):
    for i in range(n):
        swapped = False
        for j in range(n - i - 1):
            if A[j] > A[j + 1]:
                A[j], A[j + 1] = A[j + 1], A[j]
                swapped = True

        if swapped == False:
            break

    print(A)


l = [10, 1, 7, 13, 2]
size = len(l)
bubble_sort(l, size)
