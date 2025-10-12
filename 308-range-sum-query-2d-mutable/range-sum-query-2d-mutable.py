class BIT:
    def __init__(self, n):
        self.n=n
        self.values=[0]*(self.n+1)
    @staticmethod
    def lowerbit(x):
        return x&-x
    # update
    def update(self, x, delta):
        while x<=self.n:
            self.values[x]+=delta
            x+=BIT.lowerbit(x)
    # query
    def query(self, x):
        s=0
        while x>0:
            s+=(self.values[x])
            x-=BIT.lowerbit(x)
        return s
class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        self.trees=[]
        n=len(matrix[0])
        for row in matrix:
            tree=BIT(n)
            for j in range(n):
                tree.update(j+1, row[j])
            self.trees.append(tree)


    def update(self, row: int, col: int, val: int) -> None:
        tree= self.trees[row]
        prev= tree.query(col+1)-tree.query(col)
        tree.update(col+1, val-prev)

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        result=sum([tree.query(col2+1)-tree.query(col1) for tree in self.trees[row1:row2+1]])
        return result

# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# obj.update(row,col,val)
# param_2 = obj.sumRegion(row1,col1,row2,col2)