/**
 * Author: DearAsutosh
 * Problem: Best Time to Buy and Sell Stock II (LeetCode #122)
 * Description: Find the maximum profit you can achieve by buying and selling
 *              multiple times. You can buy and sell on the same day.
 */
public class BestTimeToBuyAndSellStockII_DearAsutosh {
    // we have to return maximum profit from prices array
    public static int maxProfit(int[] prices) {
        int profit = 0;
        for (int i = 1; i < prices.length; i++) {
            // If price is higher than previous day, sell today
            if (prices[i] > prices[i - 1]) {
                profit += prices[i] - prices[i - 1]; // accumulate profit
            }
        }
        return profit;
    }
    public static void main(String[] args) {
        int[] prices = { 7, 1, 5, 3, 6, 4 };
        System.out.println("Maximum Profit: " + maxProfit(prices));
    }
}
