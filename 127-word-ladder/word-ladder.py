class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList:
            return 0
        
        ptw= defaultdict(list)
        for word in wordList:
            for j in range(len(word)):
                pattern= word[:j]+"*"+word[j+1:]
                ptw[pattern].append(word)
        # initalising the res, visit and queue variable
        res=1
        queue=deque([beginWord])
        visit= set()
        visit.add(beginWord)
        # starting from the queue 
        while queue:
            for _ in range(len(queue)):
                word= queue.popleft()
                if word==endWord:
                    return res
                for j in range(len(word)):
                    pattern= word[:j]+"*"+word[j+1:]
                    for w in ptw[pattern]:
                        if w not in visit:
                            visit.add(w)
                            queue.append(w)
            res+=1
        return 0
        
