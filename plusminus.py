def plusMinus(arr):
    pos, neg, zero = 0,0,0
    for num in arr:
        if num > 0:
            pos += 1
        elif num < 0:
            neg += 1
        else:
            zero += 1
    print(pos / len(arr))
    print(neg / len(arr))
    print(zero / len(arr))
