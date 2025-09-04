class Solution:
    def findClosest(self, x: int, y: int, z: int) -> int:
        x_moves=abs(z-x)
        y_moves=abs(y-z)
        return 0 if x_moves==y_moves else 2-(x_moves<y_moves)