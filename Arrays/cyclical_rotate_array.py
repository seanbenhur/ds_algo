


def rotate(arr):
    n = len(arr)

    last_elem = arr[-1]

    for i in range(n-1,0,-1):
        arr[i] = arr[i-1]
    arr[0] = last_elem 

    return arr 

if __name__ == '__main__':
    n = int(input())
    arr = [int(input()) for _ in range(n)]
    print(arr)
    arr = rotate(arr)
    print(arr)


