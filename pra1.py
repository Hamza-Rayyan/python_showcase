class Solution(object):
    def __init__(self, prices ):
        small_ele = min(self.prices)
        maxim_ele = max(self.prices)
        for i in self.prices:
            if i <= small_ele:
                sum = maxim_ele - small_ele
                max_profit = sum
                print(max_profit)
                
                
jan = Solution[7,1,5,3,6,4]

        