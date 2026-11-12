class Solution {
    /**
     * @param {number[]} prices
     * @return {number}
     */
    maxProfit(prices: number[]): number {
        //track min seen so far and subtract from curr price to get running max
        let minSoFar = prices[0];
        let maxProfit = 0;
        for(const price of prices){
            const profit = price - minSoFar;
            if(profit > maxProfit)
                maxProfit = profit;
            if(price < minSoFar)
                minSoFar = price;
        }
        return maxProfit;
    }
}
