class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # each row must contain the digits 1-9 without duplicates 
        # each col must contain the digits 1-9 without duplicates 
        # each of the nine 3x3 sub-boxes of the grid must contain digits 1-9 without 
        # ... duplicates. 

        # [[1, 2, 3, 4, 5], 
        #  [1, 2, 3, 4, 5], 
        #  [1, 2, 3, 4, 5]]

        num_of_rows = len(board)
        num_of_cols = len(board[0])

        # each row (no repeats)
        for row in board: 
            seen = set() 
            for item in row:
                # if int(item) > 9 or int(item) < 1:
                #     return False
                if item == ".":
                    continue
                if item not in seen:
                    seen.add(item)
                else:
                    print("returning false for row")
                    return False 

            
        # each column (no repeats)
        col = 0 
        while col < num_of_cols:
            seen = set() 
            for row in range(num_of_rows):
                item = board[row][col]
                # if int(item) > 9 or int(item) < 1:
                #     return False 
                if item == ".":
                    continue 
                if item not in seen:
                    seen.add(item)
                else:
                    print("returning false for col")
                    return False 
            col += 1 
        
        # each square 
        col = 0 
        row = 0 

    
        while col < 9: 
            while row < 9: 
                seen_in_square = set() 
                for r in range(row, row + 3):
                    for c in range(col, col + 3):
                        item = board[r][c]
                        if item == ".":
                            continue
                        if item not in seen_in_square:
                            seen_in_square.add(item)
                        else:
                            return False 
                row += 3 
            col += 3 
            row = 0 

        



        


        return True 


        # each box (no repeats)



        

