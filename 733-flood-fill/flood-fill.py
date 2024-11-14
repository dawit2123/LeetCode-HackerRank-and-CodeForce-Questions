class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        cur=image[sr][sc]
        def dfs(sr, sc, visit, cur):
            if min(sr, sc)<0 or sr==len(image) or sc==len(image[0]) or (sr, sc) in visit or cur!=image[sr][sc]:
                return
            visit.add((sr, sc))
            cur=image[sr][sc]
            image[sr][sc]=color
            dfs(sr+1, sc, visit, cur)
            dfs(sr-1, sc, visit, cur)
            dfs(sr, sc+1, visit, cur)
            dfs(sr, sc-1, visit, cur)
            visit.remove((sr, sc))
        dfs(sr, sc, set(), cur)
        return image