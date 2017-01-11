class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """

        # Initialization
        i = 0
        j = 0
        out_list = []
        my_dict = {}

        # Create hash table where keys are arr and values are index
        # To handle collisions, create a list for each value
        for i in range(len(nums)):
            # Handle collision here
            if nums[i] in my_dict:
                my_dict[nums[i]].append(i)
            else:
                new_list = []
                my_dict[nums[i]] = new_list
                my_dict[nums[i]].append(i)

        # Go through to see if target - value in array is a key that exists
        # There are couple of things to consider here...
        # 1. Handle collision cases
        # 2. Handle if key exists, the key value also cannot equal the value at the same index in array
        for j in range(len(nums)):
            dictionary_key = target - nums[j]
            # 1. The second AND conditional statement is to account when two matching keys and collision occurs
            if len(my_dict[nums[j]]) > 1 and (nums[j] * 2 == target):
                out_list = my_dict[nums[j]]
                return out_list
            # This covers case 2.
            elif ((dictionary_key in my_dict) and (dictionary_key != nums[j])):
                out_list.append(j)
        return out_list

# Test cases
"""
arr = [230,863,916,585,981,404,316,785,88,12,70,435,384,778,887,755,740,337,86,92,325,422,815,650,920,125,277,336,221,847,168,23,677,61,400,136,874,363,394,199,863,997,794,587,124,321,212,957,764,173,314,422,927,783,930,282,306,506,44,926,691,568,68,730,933,737,531,180,414,751,28,546,60,371,493,370,527,387,43,541,13,457,328,227,652,365,430,803,59,858,538,427,583,368,375,173,809,896,370,789]
target = 542
#arr = [3,2,4]
#target = 6
#arr = [0,4,3,0]
#target = 0
#arr = [2,1,9,4,4,56,90,3]
#target = 8
"""

return_list = Solution().twoSum(arr, target)
print return_list