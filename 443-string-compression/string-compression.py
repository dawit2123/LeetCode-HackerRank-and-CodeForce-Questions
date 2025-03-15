class Solution:  
    def compress(self, chars: List[str]) -> int:  
        n = len(chars)  
        idx = 0  
        i = 0  
        
        while i < n:  
            current_char = chars[i]  
            count = 0  
            
            while i < n and chars[i] == current_char:  
                count += 1  
                i += 1  
            
            if count == 1:  
                chars[idx] = current_char  
                idx += 1  
            else:  
                chars[idx] = current_char  
                idx += 1  
                for digit in str(count):  
                    chars[idx] = digit  
                    idx += 1  

        chars[:] = chars[:idx]  
        return idx  