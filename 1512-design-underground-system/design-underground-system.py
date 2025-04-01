class UndergroundSystem:

    def __init__(self):
        self.user = defaultdict(tuple)
        self.stat = defaultdict(list)

    def checkIn(self, id: int, stationName: str, t: int) -> None:
        self.user[id] = (stationName,t)

    def checkOut(self, id: int, stationName: str, t: int) -> None:
        chkin = self.user[id]
        self.stat['_'.join([chkin[0],stationName])].append(t-chkin[1])

    def getAverageTime(self, startStation: str, endStation: str) -> float:
        arr = self.stat['_'.join([startStation,endStation])]
        return sum(arr)/len(arr)