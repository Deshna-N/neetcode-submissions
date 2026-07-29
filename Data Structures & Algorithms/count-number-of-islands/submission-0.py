## island must have connected 1's (atleast 2) up, down, left or right
## ANDD has zeros up down left and right of all the 1's

## base cases if in visited already, if == 0, less than minimums on graph or greater than  maxes on graph
class Solution:
    def dfs(self, grid, r, c, visited):
        row = len(grid)
        col = len(grid[0])
        
        

        if ((min(r, c) < 0) or (r, c) in visited or (r >= row) or (c >= col) or (grid[r][c] == "0")):
            return  ## cant be in island
        else:
            visited.add((r, c))
            self.dfs(grid, r + 1, c, visited)
            self.dfs(grid, r - 1, c, visited)
            self.dfs(grid, r, c + 1, visited)
            self.dfs(grid, r, c - 1, visited)


    def numIslands(self, grid: List[List[str]]) -> int:
        row = len(grid)
        col = len(grid[0])
        visited = set()
        count = 0

        for r in range(0, row):
            for c in range(0, col):
                if (grid[r][c] == "1") and ((r,c) not in visited):
                    count += 1
                    self.dfs(grid, r, c, visited)
        return count


            


        

        



## ex 1 walk through:
# first at 0, we gotta continue and can't go down so only right
        


        