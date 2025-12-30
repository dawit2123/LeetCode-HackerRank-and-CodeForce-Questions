class Solution:
    def numMagicSquaresInside(self, grid: List[List[int]]) -> int:
        R, C = len(grid), len(grid[0])
        if R < 3 or C < 3:
            return 0
        pattern_1 = [[8, 1, 6], [3, 5, 7], [4, 9, 2]]
        
        valid_squares = []
        def rotate(sq):
            return [[sq[2][0], sq[1][0], sq[0][0]],
                    [sq[2][1], sq[1][1], sq[0][1]],
                    [sq[2][2], sq[1][2], sq[0][2]]]
        
        # Generate all 4 rotations
        curr = pattern_1
        for _ in range(4):
            valid_squares.append(curr)
            curr = rotate(curr)
            
        # Generate reflections (transpose) and their rotations
        curr = [[pattern_1[j][i] for j in range(3)] for i in range(3)] # Transpose
        for _ in range(4):
            valid_squares.append(curr)
            curr = rotate(curr)

        # Optimization: Flatten them to tuples for easier comparison/hashing
        # Each magic square becomes a tuple of 9 numbers
        valid_patterns = set()
        for sq in valid_squares:
            flat = tuple(num for row in sq for num in row)
            valid_patterns.add(flat)

        count = 0
        for r in range(R - 2):
            for c in range(C - 2):
                #    If grid[r+1][c+1] is not 5, skip immediately.
                if grid[r+1][c+1] != 5:
                    continue               
                # Extract the 3x3 subgrid as a flattened tuple
                subgrid = (
                    grid[r][c],   grid[r][c+1],   grid[r][c+2],
                    grid[r+1][c], grid[r+1][c+1], grid[r+1][c+2],
                    grid[r+2][c], grid[r+2][c+1], grid[r+2][c+2]
                )
                
                # O(1) Lookup
                if subgrid in valid_patterns:
                    count += 1
                    
        return count