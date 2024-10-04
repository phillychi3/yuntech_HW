data = [(5, 2), (8, 1), (1, 2, 3)]


def merge(left, right, compare):
    rr = []
    i, j = 0, 0
    while i < len(left) and j < len(right):
        if compare(left[i], right[j]):
            rr.append(left[i])
            i += 1
        else:
            rr.append(right[j])
            j += 1
    while i < len(left):
        rr.append(left[i])
        i += 1
    while j < len(right):
        rr.append(right[j])
        j += 1
    return rr


def merge_sort(L, compare=lambda x, y: x < y):
    """Assumes L is a list, compare defines an ordering
      on elements of L
    Returns a new sorted list with the same elements as L"""
    if len(L) < 2:
        return L[:]
    else:
        middle = len(L) // 2
        left = merge_sort(L[:middle], compare)
        right = merge_sort(L[middle:], compare)
        return merge(left, right, compare)


print(merge_sort(data))
