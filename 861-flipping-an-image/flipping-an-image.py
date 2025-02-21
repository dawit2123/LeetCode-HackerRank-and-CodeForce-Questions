class Solution:
    def flipAndInvertImage(self, image: List[List[int]]) -> List[List[int]]:
        result=[]
        for i in range(len(image)):
            flipped_image=image[i][::-1]
            for j in range(len(flipped_image)):
                flipped_image[j]= 0 if flipped_image[j]==1 else 1
            result.append(flipped_image)
        return result
