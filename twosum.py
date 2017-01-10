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
        out_list = []
        my_dict = {}
        print nums
        print range(len(nums))
        target = int(target)
        #print len(nums)
        for i in range(len(nums)):
            print "?"
            my_dict[nums[i]] = i
            print "i: %s" % i
            print "my_dict %s" % my_dict
            print "my_dict[nums[i]] %s" % my_dict[nums[i]]
            print "!"
        print my_dict
        i = 0
        for i in range(len(nums)):
            #print "............"
            print "i: %s" % i
            print "nums[%s]: %s" % (i, nums[i])
            print "my_dict[%s]: %s" % (i, my_dict[nums[i]])
            dictionary_key = target - nums[i]
            print "dictionary_key %s" % dictionary_key
            if ((dictionary_key in my_dict) and (dictionary_key != nums[i])):
                    print "i is %s" % i
                    #print my_dict[dictionary_key]
                    #out_list = [my_dict[i],my_dict[dictionary_key]]
                    #print out_list
                    #return i
                    out_list.append(i)
        #print "end"
        return out_list

#arr = [230,863,916,585,981,404,316,785,88,12,70,435,384,778,887,755,740,337,86,92,325,422,815,650,920,125,277,336,221,847,168,23,677,61,400,136,874,363,394,199,863,997,794,587,124,321,212,957,764,173,314,422,927,783,930,282,306,506,44,926,691,568,68,730,933,737,531,180,414,751,28,546,60,371,493,370,527,387,43,541,13,457,328,227,652,365,430,803,59,858,538,427,583,368,375,173,809,896,370,789]
#target = 542
arr = [3,2,4]
target = 6
#arr = [0,4,3,0]
#target = 0
#arr = [2,1,9,4,4,56,90,3]
#target = 8

#arr = input()
#print arr.type()
#target = int(input())
#print target
#print target.type()

return_list = Solution().twoSum(arr, target)
print return_list
#print return_list