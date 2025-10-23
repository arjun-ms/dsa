class Solution:
    def stockBuySell(self, arr, n):
        buy = 0
        sell = 1
        max_profit = 0

        while(sell<n):
            if arr[sell] > arr[buy]:
                curr_profit = arr[sell] - arr[buy]
                max_profit = max(max_profit,curr_profit)
            else:
                buy = sell     # reset the buy pointer
        
            sell += 1
        return max_profit
