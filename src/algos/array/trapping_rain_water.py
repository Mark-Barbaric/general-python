def trap_rain_water(heights : list[int])->int:
    ans = 0
    
    for i in range(1, len(heights)-1):
        maxL, maxR = 0,0
        
        for l in range(i, -1, -1):
            maxL = max(maxL, heights[l])
        
        for r in range(i, len(heights)):
            maxR = max(maxR, heights[r])
        
        ans += min(maxL, maxR) - heights[i]
    
    
    return ans

def trap_rain_water_dp(heights : list[int])->int:
    ans = 0
    leftMax = [0 for _ in range(len(heights))]
    rightMax = [0 for _ in range(len(heights))]
    
    leftMax[0] = heights[0]
    rightMax[-1] = heights[-1]
    
    for i in range(1, len(heights)):
        leftMax[i] = max(heights[i], leftMax[i - 1])
    
    for i in range(len(heights) - 2, 0, -1):
        rightMax[i] = max(heights[i], rightMax[i+1])
        
    for i in range(1, len(heights) - 1):
        ans += min(leftMax[i], rightMax[i]) - heights[i]
        
    return ans


def trap_rain_water_stack(heights : list[int])->int:
    ...