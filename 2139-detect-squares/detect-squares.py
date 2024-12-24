class DetectSquares:

    def __init__(self):
        self.coordinates_count=defaultdict(int)
        self.coordinates=[]

    def add(self, point: List[int]) -> None:
        self.coordinates_count[tuple(point)]+=1
        self.coordinates.append(point)

    def count(self, point: List[int]) -> int:
        res=0
        px, py= point
        for coordinate in self.coordinates:
            x,y= coordinate
            if (abs(px-x)!=abs(py-y)) or x==px or y==py:
                continue
            res+= self.coordinates_count[(x, py)]*self.coordinates_count[(px, y)]
        return res


# Your DetectSquares object will be instantiated and called as such:
# obj = DetectSquares()
# obj.add(point)
# param_2 = obj.count(point)