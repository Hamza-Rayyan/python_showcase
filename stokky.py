class Solution:
    def maxProfit(self,prices):
        left = 0 #Buy
        right = 1 #Sell
        max_profit = 0
        while right < len(prices):
            currentProfit = prices[right] - prices[left] #our current Profit
            if prices[left] < prices[right]:
                max_profit =max(currentProfit,max_profit)
            else:
                left = right
            right += 1
        return max_profit

obj = Solution()
input_str = input("Enter a list of numbers separated by commas: ")
input_list = input_str.split(',')
my_list = [int(item.strip()) for item in input_list]
print("List entered:", my_list)

 
print(obj.maxProfit(my_list))


