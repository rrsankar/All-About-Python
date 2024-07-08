def bubble_sort(sequence):

    indexing_length = len(sequence) - 1

    sorted = False

    while not sorted:

        sorted = True

        for i in range(0, indexing_length):

            if sequence[i] > sequence[i+1]:

                sorted = False

                sequence[i], sequence[i+1] = sequence[i+1], sequence[i]

    return sequence


print(bubble_sort([12, 1, 11, 3, 13, 5, 6]))