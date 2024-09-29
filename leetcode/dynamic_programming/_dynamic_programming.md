## 1. House Robber (**Interview Question**)

### You are a professional robber planning to rob houses along a street. Each house has a certain amount of money stashed, but adjacent houses have security systems that will automatically contact the police if two adjacent houses are robbed on the same night. Write a function `max_money_robbed(nums)` to determine the maximum amount of money you can rob tonight without alerting the police.

**Input:**  
An integer array, `nums`, where each element represents the amount of money in a house.

**Output:**  
An integer representing the maximum amount of money you can rob without triggering the alarms.

**Example 1:**

- Input: `nums = [1, 2, 3, 1]`
- Output: `4`
- Explanation: Rob house 1 (money = 1) and house 3 (money = 3). The total amount robbed is `1 + 3 = 4`.

**Example 2:**

- Input: `nums = [2, 7, 9, 3, 1]`
- Output: `12`
- Explanation: Rob house 1 (money = 2), house 3 (money = 9), and house 5 (money = 1). The total amount robbed is `2 + 9 + 1 = 12`.

**Constraints:**

- `1 <= nums.length <= 100`
- `0 <= nums[i] <= 400`

-----------------------------------------------------------------------------------------



## 2. Best Time to Buy and Sell Stock (**Interview Question**)

### You are given an array `prices` where `prices[i]` represents the price of a given stock on the `i`th day. Your goal is to maximize profit by choosing a single day to buy the stock and another day in the future to sell it. Write a function `max_profit()` that returns the maximum profit from the transaction. If no profit can be made, return `0`.

**Input:**  
An array, `prices`, representing the price of a stock on different days.

**Output:**  
An integer representing the maximum profit achievable from a buy-sell transaction. If no profit can be made, return `0`.

**Example 1:**

- Input: `prices = [7, 1, 5, 3, 6, 4]`
- Output: `5`
- Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = `6 - 1 = 5`.

**Example 2:**

- Input: `prices = [7, 6, 4, 3, 1]`
- Output: `0`
- Explanation: No transactions can be done to make a profit, so return `0`.

**Constraints:**

- `1 <= prices.length <= 105`
- `0 <= prices[i] <= 104`

-----------------------------------------------------------------------------------------



## 3. Climbing Stairs (**Interview Question**)

### You are climbing a staircase that requires `n` steps to reach the top. Each time, you can climb either 1 step or 2 steps. Write a function `climb_stairs()` that returns the number of distinct ways you can climb to the top.

**Input:**  
An integer, `n`, representing the total number of steps to the top.

**Output:**  
An integer representing the number of distinct ways to climb to the top.

**Example 1:**

- Input: `n = 2`
- Output: `2`
- Explanation: There are two ways to climb to the top:
  1. 1 step + 1 step
  2. 2 steps

**Example 2:**

- Input: `n = 3`
- Output: `3`
- Explanation: There are three ways to climb to the top:
  1. 1 step + 1 step + 1 step
  2. 1 step + 2 steps
  3. 2 steps + 1 step

**Constraints:**

- `1 <= n <= 45`

-----------------------------------------------------------------------------------------
