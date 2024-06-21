def smaller(arr):
    def merge_sort_enum(enum):
        half = len(enum) // 2
        if half:
            left, right = merge_sort_enum(enum[:half]), merge_sort_enum(enum[half:])
            for i in range(len(enum))[::-1]:
                if not right or left and left[-1][1] > right[-1][1]:
                    count[left[-1][0]] += len(right)
                    enum[i] = left.pop()
                else:
                    enum[i] = right.pop()
        return enum
    
    count = [0] * len(arr)
    merge_sort_enum(list(enumerate(arr)))
    return count
