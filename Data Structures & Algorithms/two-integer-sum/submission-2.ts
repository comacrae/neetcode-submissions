class Solution {
    /**
     * @param {number[]} nums
     * @param {number} target
     * @return {number[]}
     */
    twoSum(nums: number[], target: number): number[] {
       //hashmap solution
       //init map
       const m = new Map<number,number>();
       // for each value in nums
       for(const [idx,val] of nums.entries()){
        //if target - nums[val] is in map, return that idx and curr idx
        const diff = target - val;
        if(m.has(diff))
            return [m.get(diff), idx]
        else
            // else put curr idx using curr val as key
            m.set(val,idx);
       }

    }
}
