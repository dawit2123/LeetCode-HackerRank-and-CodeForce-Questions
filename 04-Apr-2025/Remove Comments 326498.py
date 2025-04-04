# Problem: Remove Comments - https://leetcode.com/problems/remove-comments/

class Solution:
    def removeComments(self, source):
        def get_who_first(line, commenting): 
            atype, btype, ctype = line.find('//'), line.find('/*'), line.find('*/')
            if atype != -1 and ctype != -1 and commenting:
                if commenting and ctype > atype: 
                    return False
                else: return ctype > atype
            elif atype != -1 and btype != -1:
                return btype > atype
            return atype != -1

        commenting, outputs, remained = False, [], ''
        for line in source:
            output = []
            while True: 
                if line.find('//') != -1 and get_who_first(line, commenting):
                    line = line[:line.find('//')]
                    if len(line) > 0: output.append(line)
                
                if not commenting and line.find('/*') != -1:
                    remained, line, commenting = line[:line.find('/*')], line[line.find('/*')+2:], True

                if commenting and line.find('*/') != -1:
                    line = line[line.find('*/')+2:]
                    line, remained, commenting =remained + line, '', False
                    if line.find('//')!=-1 or line.find('/*')!=-1 or line.find('*/')!=-1: continue
                    if len(line) > 0: output.append(line)
                break

            if len(output) > 0: outputs.append(''.join(output)) 
            elif not commenting and len(line) > 0: outputs.append(line) 
        return outputs