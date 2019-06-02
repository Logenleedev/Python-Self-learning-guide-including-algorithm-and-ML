def maxProfit(prices):
  arrayLen = len(prices)
  profits = []
  for x in range(arrayLen - 1):
    i = x + 1
    while i < arrayLen:
      profit = prices[i] - prices[x]
      profits.append(profit)
      i += 1
  maxProfit = max(profits)
  if maxProfit > 0:
    return maxProfit
  else:
    return 0
