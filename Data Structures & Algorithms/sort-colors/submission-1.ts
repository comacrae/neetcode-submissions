class Solution {
    /**
     * @param {number[]} nums
     * @return {void} Do not return anything, modify nums in-place instead.
     */
    sortColors(nums: number[]): void {
        const counts = [0,0,0];
        for(const n of nums){
            counts[n] +=1;
        }
        let idx = 0;
        for(let val = 0; val < counts.length; val++){
            for(let freq = 0; freq < counts[val]; freq++){
                nums[idx] = val;
                idx +=1;
            }
        }

    }
}
