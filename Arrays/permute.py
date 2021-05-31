def permute(nums):
    n = len(nums)
        
    if n==1:
        return [nums]
        
    if n==2:
        return [[nums[0],nums[1]],[nums[1],nums[0]]]
        
    res = []
    for i in range(n):
        temp = permute(nums[0:i]+nums[i+1:])
        res += [[nums[i]] + x for x in temp]
            
    return res
        

if __name__ == "__main":
    n = int(input())
    for _ in range(n):
        nums = list(map(int, input().strip()))
        print(permute(nums))
        