## each row is ascending
## so row[-1] of previous is < row[0] of next row

## 

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        left = 0
        right = len(matrix) - 1 ## last element in matrix

        while (left <= right):
            mid = (left + right) // 2   ## make it equal most middle element of matrix -> O(log(n*m))

            if matrix[mid][-1] < target:  ### number is in a higher up row
                # make right equal mid 
                #right = matrix[mid + 1][-1] #### am i making sure that a mid + 1 exists
                left = mid + 1
                

            elif matrix[mid][0] > target: ## number is in a lower row 
                right = mid - 1
                #left = matrix[mid - 1][0]

            else: ## target is inside the current row mid is at!
                if target in matrix[mid]:
                    return True
                else:
                    return False

        return False

### ex 1:
## left = 0 index (1), right = 11 index (40), mid = 11 // 2 = 5, 11 > 10

        