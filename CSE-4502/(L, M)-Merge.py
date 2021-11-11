import random


# assume l = m in the (l,m) merge sort
# we also assume that l % len(lst) == 0
def LMM(l, lst):
    # merges two sorted lists to a sort list
    def merge(a, b):
        temp = []
        i = 0
        j = 0
        while i < len(a) and j < len(b):
            if a[i] > b[j]:
                temp.append(b[j])
                j += 1
            else:
                temp.append(a[i])
                i += 1
        temp += a[i::] + b[j::]
        return temp

    """
    Recursively merging the lists
    lst is a lst of lists 
    example:
    [[1, 3, 7], [2, 6, 9], [0, 4,  11], [5, 8, 10]] 
    - > [[1, 2, 3, 6, 7, 9], [0, 4, 5, 8, 10, 11]]
        - > [[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]]
             return [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
    output: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]

    """

    def helper(x):
        # we are done if true
        if len(x) == 1:
            return x[0]

        # temp will become our next lst in the recursion
        # this merges 2 lists at a time from lst and puts it into temp
        temp = []
        for i in range(0, len(x), 2):
            if i + 1 >= len(x):
                temp.append(x[i])
                break
            temp.append(merge(x[i], x[i + 1]))

        return helper(temp)

    # creates l lists of size l in y
    y = []
    for i in range(0, len(lst), l):
        y.append([lst[j] for j in range(i, i + l)])

    # Shuffling the elements of y
    # this grabs y[0][b], y[1][b],..., y[-1][b] and merges it into z[b]
    z = [[] for i in range(l)]
    i = 0
    j = 0
    while i < len(y):
        if not z[i]:
            z[i].append(y[j][i])
        else:
            z[i] = merge(z[i], [y[j][i]])

        j += 1
        if j > l - 1:
            j = 0
            i += 1

    # we are returning a sorted list after recursively merging
    return helper(z)


def isSorted(x):
    temp = True
    for i in range(1, len(x) - 1, 2):
        if i >= len(x) - 2:
            temp = True
            break
        temp = x[i] < x[i + 1]
    return temp


if __name__ == "__main__":
    size = 10000
    lst = [i for i in range(size)]
    random.shuffle(lst)

    result = LMM(int(len(lst) ** 0.5), lst)

    print(isSorted(result))
