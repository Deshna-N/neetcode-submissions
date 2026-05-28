# thinking about a hash table so possibly a dict for checking duplicates
# row = {}, col = {}, box = {} -> key is position/index, val is numerical number
# so iterating over the row, add to row set, if anything repeated retur false
# iterate over col, same if repeat return false
# box is row // 3 and col // 3 ??
# to store multiple vals for each key -> value MUST BE A SET
# ex: row = {0, {1, 2, 3, 4, 5}}


#for r in row:
##if r not in row:
##row.append(r)
##now values are sets, so will add to the row[r]

# box = key->(r//3, c//3), value ->()



class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row = {}
        col = {}
        box = {}

        for r in range(len(board)):  #from 0 to 8, going index to index
            if r not in row:
                row[r] = set()
        ##now row was 9 different keys in it : row = {0: (), 1: (), 2: () ...}
            for c in range(len(board)):
                if c not in col:
                    col[c] = set()

                if board[r][c] == ".":
                    continue
                #rows
                if board[r][c] in row[r]:
                    return False
                row[r].add(board[r][c])
                #cols
                if board[r][c] in col[c]:
                    return False
                col[c].add(board[r][c])
                ##BOX:
                box_key = (r//3 , c//3)
                if box_key not in box:
                    box[box_key] = set()
                if board[r][c] in box[box_key]:
                    return False
                box[box_key].add(board[r][c])
        return True        

                






                

        