from random import randint

def GenerateArray(l = 100, begin = 0, end = 1000):

    arr = []

    for i in range(l):
        arr.append(randint(begin, end))

    arr.sort()

    return arr


def AdvSearch(arr, num):

    l = len(arr)
    avg = int((l - 1) / 2)

    if arr[l - 1] < num:
        print(f"'{num}' is more than arr[{l - 1}].")
    elif arr[0] > num:
        print(f"'{num}' is less than arr[0].")
    else:
        while True:
            if arr[avg] < num:
                if arr[avg + 1] > num:
                    print(f"'{num}' is between arr[{avg}] and arr[{avg + 1}].")
                    break
                avg = int((avg + l - 1) / 2)
            elif arr[avg] > num:
                if arr[avg - 1] < num:
                    print(f"'{num}' is between arr[{avg - 1}] and arr[{avg}].")
                    break
                avg = int(avg / 2)
            else:
                print(f"'{num}' is equal arr[{avg}].")
                break

