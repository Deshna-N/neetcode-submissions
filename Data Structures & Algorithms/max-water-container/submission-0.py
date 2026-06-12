### between the two bars, take the length of shortest of two and then the width between
# then calculate area and that will give max amount of water
# Need the two tallest poles that are the furthest in order to get biggest length and biggest width
#might need to have a for loop running for each bar, and then a while left < right inside??
### thus iterating for each bar...
### point, not sure where to calcjulate final area/length at moment
## just realized that since can't sort heights cause they want O(n), that puts me in dilemma,
## i just checked that they labeled this as a greedy alg, should i use that? Maybe watch
##the video on that i kinda forgot how it works, two pointer method starting to fall apart rn
class Solution:
    def maxArea(self, heights: List[int]) -> int:
        left = 0
        right = len(heights) - 1
        area = 0
        final_area = 0
        width = 0
        curr_length = 0


        while left < right:
            ## compare the smaller number between left and right, and that is the used length
            curr_length = min(heights[left] , heights[right])

            ## calc width between the two 
            width = right - left
            area = width * curr_length

            if area > final_area:
                final_area = area
            
            ### different if staements???
            if heights[left] < heights[right]:
                left += 1
            elif heights[left] > heights[right]:
                right -= 1
            else: ## theyre equal
                right -= 1
        return final_area
            


          
### ex 1:
## while left < right, left is at pos 1 (h 1) and right is at pos 8 (h 6)
### curr_length = 1, width is 7
## area is 7, bigger than final_area, so final_area = 7
### left moves up to second bar 

##i = 2, left is at pos 2 (h 7) and right is at pos 8 (h 6)
### curr_length = 6, width 6
## area is 36, bigger than final_area, so final_area = 36




        