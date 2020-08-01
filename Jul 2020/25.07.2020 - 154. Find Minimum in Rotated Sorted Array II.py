class Solution:
    def findMin(self, nums: List[int]) -> int:
        l,r = 0,len(nums)-1
        while l < r:
            mid = l + (r-l)//2
            if nums[mid] > nums[r]: # in this case answer must be to right of mid
                l = mid+1
            elif nums[mid] < nums[r]: # in this case answer must be either mid or left of mid
                r = mid
            else: # if nums[mid] == nums[r] then we are not sure so exclude right endpoint and continue because of this step we are not cutting list in half so O(N) worst time
                r-=1
        return nums[l]

#Space, Time = O(1), O(logN)-O(N) (avg-worstcasr)

