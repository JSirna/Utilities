def find_max(nums):
    max_so_far = float("-inf")
    temp = max_so_far
    if (nums):
        for num in nums:
            if (temp < num):
                temp = num
        print(temp)
        return temp
    else:
        return max_so_far