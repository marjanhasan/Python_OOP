nums = [10, 20, 30, 40, 50]
nums.append(60)
print(nums)  # [10, 20, 30, 40, 50, 60]
nums.insert(2, 70)
print(nums)  # [10, 20, 70, 30, 40, 50, 60]
if 30 in nums:
    nums.remove(30)
print(nums)  # [10, 20, 70, 40, 50, 60]
last = nums.pop()
print(nums, last)
