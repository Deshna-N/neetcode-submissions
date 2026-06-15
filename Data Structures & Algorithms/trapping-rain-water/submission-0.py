## set width of 1 for all bars
## two pointer approach again! 
## thinking of area once again so area = width * height 
### but wanna calculate total area of already made bars!
### how much water at each position , add them all up
### water inside is found by finding tallest at right side, and left side, then find min of those 2
## prefix array: ->
## height = [0,2,0,3,1,0,1,3,2,1]
## pre_ar = [0,2,2,3,3,3,3,3,3,3] -> curr_max = 0
## suf_ar = [1,2,3,3,3,3,3,3,3,3]


class Solution:
    def pre(self, height: List[int]) -> []:
        pre_arr = []
        curr_max = 0
        for i in range(len(height)):
            if height[i] >= curr_max:
                pre_arr.append(height[i])
                curr_max = height[i]
            else:
                pre_arr.append(curr_max)
        return pre_arr

    def suf(self, height: List[int]) -> []:
        suf_arr = []
        curr_max = 0
        height = list(reversed(height))
        for i in range(len(height)):
            if height[i] >= curr_max:
                suf_arr.append(height[i])
                curr_max = height[i]
            else:
                suf_arr.append(curr_max)
        suf_arr.reverse()
        return suf_arr

    def trap(self, height: List[int]) -> int:
        pre_array = self.pre(height)
        suf_array = self.suf(height)
        ### loop through each position
        total_water = 0
        for i in range(len(height)):
            max_left = pre_array[i]
            max_right = suf_array[i]
            area_water = min(max_left, max_right) - height[i]
            total_water = total_water + area_water
        return total_water






## ex: left at 0 (h 0), right at 9 (h 1)
## 
        