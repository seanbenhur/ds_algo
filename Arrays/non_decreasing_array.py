


from copy import deepcopy

def non_decrease(nums):
    #make a copy of  the arrays 
    a,b = deepcopy(nums),deepcopy(nums)

    if len(nums)>2:
        #traverse
        for i in range(len(nums)):
            if a[i]>a[i+1]:
                del a[i]
                del b[i+1]
                return ((a==sorted(a) or (b==sorted(b))))

            else:
                return True
    else:
        return True


if __name__ == "__main__":
    nums = list(map(int, input().split()))
    print(non_decrease(nums))
            

