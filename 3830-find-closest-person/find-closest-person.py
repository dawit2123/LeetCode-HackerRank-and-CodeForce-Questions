class Solution:
    def findClosest(self, x: int, y: int, z: int) -> int:
        x_moves=abs(z-x)
        y_moves=abs(y-z)
        if x_moves<y_moves:
            return 1
        elif y_moves<x_moves:
            return 2
        else:
            return 0