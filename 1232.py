class Solution:
    def checkStraightLine(self, coordinates: List[List[int]]) -> bool:

        coef0 = coordinates[0]
        coef1 = coordinates[1]

        if coef0[0] - coef1[0] != 0:
            a = (coef0[1] - coef1[1]) / (coef0[0] - coef1[0])
            b = coef0[1] - a * coef0[0]

            for coord in coordinates:
                if coord[0] * a + b == coord[1]:
                    continue
                else:
                    return False
            
        else:
            for coord in coordinates:
                if coef0[0] != coord[0]:
                    return False
        
        return True