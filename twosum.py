class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        #print nums
        #print target
        #print "----"
        i = 0
        my_dict = {}
        target = int(target)
        #print len(nums)
        for i in range(len(nums)):
            my_dict[nums[i]] = i
        #print my_dict
        i = 0
        for i in range(len(nums)):
            #print "............"
            #print "i: %s" % i
            #print "nums[%s]: %s" % (i, nums[i])
            #print "my_dict[%s]: %s" % (i, my_dict[nums[i]])
            dictionary_key = target - i
            print dictionary_key
            if my_dict.get(dictionary_key, default=None):
                print "i is %s" % i
                #print my_dict[dictionary_key]
                out_list = [my_dict[i],my_dict[dictionary_key]]
                print out_list
            else:
                out_list = [0]
        #print "end"
        return out_list

arr = [2,1,9,4,4,56,90,3]
target = 8
#arr = input()
#print arr.type()
#target = int(input())
#print target
#print target.type()

return_list = Solution().twoSum(arr, target)
print return_list
#print return_list