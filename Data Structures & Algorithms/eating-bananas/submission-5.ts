class Solution {
    /**
     * @param {number[]} piles
     * @param {number} h
     * @return {number}
     */
    
    minEatingSpeed(piles: number[], h: number): number {
        //init minK from max(piles)
        let minK = -1;
        let pilesMax =-1;
        for(const pile of piles){
            if(pile > pilesMax)
                pilesMax = pile;
        }
        minK = pilesMax;

        // set ptrs to start, end
        let st = 1;
        let end = pilesMax;

        // while st <= end
        while(st <= end){
            //get mid
            let rate = Math.floor((st + end) / 2);
            // run koko eating loop
            let totalHours = 0;
            for(const pile of piles){
                let hoursToEatPile = Math.ceil(pile / rate);
                totalHours += hoursToEatPile;
            }

            // if too many hours, then try a larger k
            if(totalHours > h){
                st = rate + 1;
            }else{
                minK= rate;
                end = rate - 1;
            }
            // if no bananas left, update minK and try a smaller k
        }
            
        //return minK
        return minK;
    }
}
