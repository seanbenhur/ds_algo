
nums = [1, 7, 3, 5, 6]

def find_equivalent(nums):
    total = sum(nums)
    leftsum = 0
    for index, value in enumerate(nums):
        rightsum = total - leftsum - value
        leftsum += value
        if rightsum == leftsum:
            return index 
        
    return -1
            
ind = find_equivalent(nums)
print(ind)