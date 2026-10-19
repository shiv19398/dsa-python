def threeSum(nums, target):
    results = []

    nums.sort()

    n = len(nums)

    for i in range(n):
        if i !=0 and nums[i] == nums[i-1]:
            continue

        left = i + 1
        right = n -1

        while left < right:
            current_sum = nums[i] + nums[left] + nums[right]

            if current_sum < target:
                left += 1

            elif current_sum > target:
                right -= 1

            else:
                results.append([nums[i], nums[left], nums[right]])

                left = left + 1
                right = right - 1

                while left < right and nums[left] == nums[left-1]:
                    left += 1
                while right > left and nums[right] == nums[right+1]:
                    right -= 1

    return results


threeSum([-1, 0, 1, 2, -1, -4], 0)
print(f"Three sum results: {threeSum([-1, 0, 1, 2, -1, -4], 0)}")