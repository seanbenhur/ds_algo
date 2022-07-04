nums = [-2,1,-3,4,-1,2,1,-5,4]


def max_subarray_with_indices(nums):
    local_max = global_max = nums[0]
    left_index = right_index = 0

    for i in range(len(nums)):
        curr = nums[i]
        if curr > curr+local_max:
            left_index = i
            local_max = curr 
        else:
            local_max = local_max + curr
        if local_max > global_max:
            global_max = local_max
            right_index = i 
    return {"Global Max": global_max, "Left Index": left_index, "Right Index" :right_index}

ans = max_subarray_with_indices(nums)
print(ans)



