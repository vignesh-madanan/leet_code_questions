def numIdenticalPairs(self, nums: List[int]) -> int:
    
    res_counter = 0
    for i in range(len(nums)):
        for j in range(len(nums)):
            if i<j and nums[i]==nums[j]:
                res_counter +=1
                
            
    return res_counter