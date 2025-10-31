package HackWithZairza-Hacktoberfest2025.DSA.DP.Best time to buy and sell stock;

public class BestTimeToBuyAndSellStock_Baibhab13 {
    public static int maxProfit(int[] prices) {
        int buy=prices[0];
        int profit=0;
        for(int i=1;i<prices.length;i++) {
            if(prices[i]<buy) {
                buy=prices[i];
            } else if(prices[i]-buy>profit) {
                profit=prices[i]-buy;
            }
        }
        return profit;
    }

    public static void main() {
        int prices[] = {7,1,5,3,6,4};
        System.out.println("The maximum profit is " + maxProfit(prices));
    }
}
