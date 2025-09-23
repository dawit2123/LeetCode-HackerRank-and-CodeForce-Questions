class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        version1_values= version1.split(".")
        version2_values= version2.split('.')
        i=0
        j=0
        while i<len(version1_values) or j<len(version2_values):
            if i<len(version1_values) and j<len(version2_values):
                if int(version1_values[i])>int(version2_values[j]):
                    return 1
                elif int(version1_values[i])<int(version2_values[j]):
                    return -1
            else:
                if i<len(version1_values) and int(version1_values[i])!=0:
                    return 1
                elif j<len(version2_values) and int(version2_values[j])!=0:
                    return -1
            i+=1
            j+=1
        return 0