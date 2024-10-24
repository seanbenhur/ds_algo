class Solution:
    def trap(self, height: List[int]) -> int:
        ans=0
        n=len(height)
        left,right=0,n-1
        ans=0
        l_max,r_max=0,0
        while left<=right:
            if r_max<=l_max:
                ans+=max(0,r_max-height[right])
                r_max=max(r_max,height[right])
                right-=1
            else:
                ans+=max(0,l_max-height[left])
                l_max=max(l_max,height[left])
                left+=1
        return ans
        