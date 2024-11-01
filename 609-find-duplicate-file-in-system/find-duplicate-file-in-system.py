class Solution:
    def findDuplicate(self, paths: List[str]) -> List[List[str]]:
        duplicate_list=defaultdict(list)
        for path in paths:
            dir, *files= path.split()
            for file in files:
                text, val= file.split("(")
                duplicate_list[val[0:len(val)-1]].append(dir+"/"+text)
        res=[file_list for file_list in duplicate_list.values() if len(file_list)>1]
        return res