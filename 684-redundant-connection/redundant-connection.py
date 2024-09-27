class JoinFind:
    def __init__(self,n):
        self.par={}
        self.rank={}
        for i in range(1, n+1):
            self.par[i]=i
            self.rank[i]=0
    def find(self, n):
        p=self.par[n]
        while p!=self.par[p]:
            self.par[p]=self.par[self.par[p]]
            p=self.par[p]
        return p
    def join(self,p1,p2):
        p1,p2=self.find(p1), self.find(p2)
        if p1==p2:
            return False
        if self.rank[p2]>self.rank[p1]:
            self.par[p1]=p2
            self.rank[p2]+=1
        elif self.rank[p2]<self.rank[p1]:
            self.par[p2]=p1
            self.rank[p1]+=1
        else:
            self.par[p2]=p1
            self.rank[p1]+=1
        return True
class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        res=[]
        remove_node=JoinFind(len(edges))
        for edge in edges:
            p1=edge[0]
            p2=edge[1]
            if not remove_node.join(p1,p2):
                res=[p1,p2]
        return res