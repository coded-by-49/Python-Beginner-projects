def test(board,Ai,opp):
    score = 0
    for col in range(-7,0):
        current_column = [board[col := col+7] for i in range(6)]
        # i could add a condition that checks if nothing is inside the column , then it automatically skips and moves on to the next iteration !!!!!!!!!!!!!!!!!!!!!!!!!1
        slice_start,slice_stop = 0,4
        for i in range(3):
            current_window  = current_column[slice_start:slice_stop]
            if current_window.count(Ai) == 3 and current_window.count(opp) == 0:
                score += 150
                print(f"this is an increment of 150 from the col {col%7} and the index {slice_start} ---> {slice_stop-1}\n")
            elif current_window.count(Ai) == 2 and current_window.count(opp) == 0:
                score += 75
                print(f"this is an increment of 75 from the col {col%7} and the index {slice_start} ---> {slice_stop-1}\n")
            elif current_window.count(Ai) == 1 and current_window.count(opp) == 0:
                score += 10
                print(f"this is an increment of 10 from the col {col%7} and the index {slice_start} ---> {slice_stop-1}\n")
            elif current_window.count(Ai) == 0 and current_window.count(opp) == 3:
                score -= 150
                print(f"this is a decrement  of -150 from the col {col%7} and the index {slice_start} ---> {slice_stop-1}\n")
            elif current_window.count(Ai) == 0 and current_window.count(opp) == 2:
                score -= 75
                print(f"this is a decrement  of -75 from the col {col%7} and the index {slice_start} ---> {slice_stop-1}\n")
            elif current_window.count(Ai) == 0 and current_window.count(opp) == 1:
                score -= 10 
                print(f"this is a decrement  of -10 from the col {col%7} and the index {slice_start} ---> {slice_stop-1}\n")
            slice_start, slice_stop = slice_start+1,slice_stop+1

    # row check
    row_start,row_stop = 0,7
    for row in range(6):
        current_row = board[row_start:row_stop]
        slice_start,slice_stop = 0,4
        for i in range(4):
            current_window  = current_row[slice_start:slice_stop]
            if current_window.count(Ai) == 3 and current_window.count(opp) == 0:
                score += 150
                print(f"this is an increment of 150 from the row : {row} and the index {slice_start} ---> {slice_stop-1}\n")
            elif current_window.count(Ai) == 2 and current_window.count(opp) == 0:
                score += 75
                print(f"this is an increment of 75 from the row {row} and the index {slice_start} ---> {slice_stop-1}\n")
            elif current_window.count(Ai) == 1 and current_window.count(opp) == 0:
                score += 10
                print(f"this is an increment of 10 from the row {row} and the index {slice_start} ---> {slice_stop-1}\n")
            elif current_window.count(Ai) == 0 and current_window.count(opp) == 3:
                score -= 150
                print(f"this is a decrement  of -150 from the row {row} and the index {slice_start} ---> {slice_stop-1}\n")
            elif current_window.count(Ai) == 0 and current_window.count(opp) == 2:
                score -= 75
                print(f"this is a decrement  of -75 from the row {row} and the index {slice_start} ---> {slice_stop-1}\n")
            elif current_window.count(Ai) == 0 and current_window.count(opp) == 1:
                score -= 10 
                print(f"this is a decrement  of -10 from the row {row} and the index {slice_start} ---> {slice_stop-1}\n")
            slice_start, slice_stop = slice_start+1,slice_stop+1
        row_start += 7
        row_stop += 7

    # right diagonal check 
    RD_outsiders = [4,5,6,12,13,20,35,36,37,28,29,21]
    RD_start_num = [0,1,2,3,7,14]
    
    for i in RD_start_num:
        current_diagonal = [board[i]]
        while i+8 not in RD_outsiders and i+8 <= 41:
            i += 8
            current_diagonal.append(board[i])  
        slice_start,slice_stop = 0,4
        while slice_stop<=len(current_diagonal):
            current_window  = current_diagonal[slice_start:slice_stop]
            if current_window.count(Ai) == 3 and current_window.count(opp) == 0:
                score += 150
                print(f"this is an increment of 150 from the RD : {i} and the index {slice_start} ---> {slice_stop-1}\n")
            elif current_window.count(Ai) == 2 and current_window.count(opp) == 0:
                score += 75
                print(f"this is an increment of 75 from the RD {i} and the index {slice_start} ---> {slice_stop-1}\n")
            elif current_window.count(Ai) == 1 and current_window.count(opp) == 0:
                score += 10
                print(f"this is an increment of 10 from the RD {i} and the index {slice_start} ---> {slice_stop-1}\n")
            elif current_window.count(Ai) == 0 and current_window.count(opp) == 3:
                score -= 150
                print(f"this is a decrement  of -150 from the RD {i} and the index {slice_start} ---> {slice_stop-1}\n")
            elif current_window.count(Ai) == 0 and current_window.count(opp) == 2:
                score -= 75
                print(f"this is a decrement  of -75 from the RD {i} and the index {slice_start} ---> {slice_stop-1}\n")
            elif current_window.count(Ai) == 0 and current_window.count(opp) == 1:
                score -= 10 
                print(f"this is a decrement  of -10 from the RD {i} and the index {slice_start} ---> {slice_stop-1}\n")
            slice_start, slice_stop = slice_start+1,slice_stop+1

    # left diagonal check
    LD_outsiders = [0, 1, 2, 7, 8, 14, 27, 33, 34, 39, 40, 41]
    LD_start_num = [3,4,5,6,13,20]
    
    for i in LD_start_num:
        current_diagonal = [board[i]]
        while i+6 not in LD_outsiders and i+6 < 41:
            i += 6
            current_diagonal.append(board[i])  
        slice_start,slice_stop = 0,4
        while slice_stop<=len(current_diagonal):
            current_window  = current_diagonal[slice_start:slice_stop]
            if current_window.count(Ai) == 3 and current_window.count(opp) == 0:
                score += 150
                print(f"this is an increment of 150 from the LD : {i} and the index {slice_start} ---> {slice_stop-1}\n")
            elif current_window.count(Ai) == 2 and current_window.count(opp) == 0:
                score += 75
                print(f"this is an increment of 75 from the LD : {i} and the index {slice_start} ---> {slice_stop-1}\n")
            elif current_window.count(Ai) == 1 and current_window.count(opp) == 0:
                score += 10
                print(f"this is an increment of 10 from the LD : {i} and the index {slice_start} ---> {slice_stop-1}\n")
            elif current_window.count(Ai) == 0 and current_window.count(opp) == 3:
                score -= 150
                print(f"this is a decrement  of -150 from the LD : {i} and the index {slice_start} ---> {slice_stop-1}\n")
            elif current_window.count(Ai) == 0 and current_window.count(opp) == 2:
                score -= 75
                print(f"this is a decrement  of -75 from the LD : {i} and the index {slice_start} ---> {slice_stop-1}\n")
            elif current_window.count(Ai) == 0 and current_window.count(opp) == 1:
                score -= 10 
                print(f"this is a decrement  of -10 from the LD : {i} and the index {slice_start} ---> {slice_stop-1}\n")
            slice_start, slice_stop = slice_start+1,slice_stop+1
            
    return score

board_neg_1110 = [
    # C0   C1   C2   C3   C4   C5   C6
    " ", " ", " ", " ", " ", " ", "x",  # Row 0
    " ", " ", " ", " ", " ", " ", "x",  # Row 1
    "x", " ", " ", " ", " ", " ", " ",  # Row 2
    "o", " ", " ", " ", " ", " ", " ",  # Row 3
    "o", "o", " ", " ", " ", " ", " ",  # Row 4
    "o", "o", "o", " ", " ", " ", " "   # Row 5
]

print(test(board_neg_1110,"x","o"))