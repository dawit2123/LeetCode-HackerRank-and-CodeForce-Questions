class Solution:
    def imageSmoother(self, img: List[List[int]]) -> List[List[int]]:
        ROWS, COLS= len(img), len(img[0])
        result_img= [[0]*len(img[0]) for _ in range(len(img))]
        for row in range(ROWS):
            for col in range(COLS):
                img_sum, img_count= 0, 0
                for i in range(row-1, row+2):
                    for j in range(col-1, col+2):
                        if i>=0 and i<ROWS and j>=0 and j<COLS:
                            img_sum+=img[i][j]
                            img_count+=1
                result_img[row][col]=(img_sum//img_count)
        return result_img