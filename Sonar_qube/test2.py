from collections import Counter
def ArrayChallenge(arr):
    n = len(arr)
    data = Counter(arr)
    get_mode = dict(data)

    mode = [k for k, v in get_mode.items() if v == max(list(data.values()))]
    if len(mode) == n:
        return -1
    else:
        return mode[0]

arr = [5,5,5,2,1,1,1,1,1]
res = ArrayChallenge(arr)

print(res)
