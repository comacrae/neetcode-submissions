class Solution {
    /**
     * @param {number[]} nums
     * @param {number} k
     * @return {boolean}
     * set = [2,3]
     * k = 3
     * 0    1   2   3
     * 1    2   3   1
     * L            R
     */
    containsNearbyDuplicate(nums: number[], k: number): boolean {
        // init the window
        const window = new Set<number>();
        //init the left pointer
        let L = 0;
        // add first value to the set
        window.add(nums[L]);
        
        //in a loop do the following
        for(let R = L + 1; R < nums.length; R++){
            // start R = L + 1
            // if the size of the window < K
            if(R - L > k){
                // trim the L value by removing nums[L] from set
                window.delete(nums[L])
                // increment L
                L+=1;
            }
            if(window.has(nums[R]))
                return true;   
            // if nums[R] in set, a dupe is found, so return True
            else
            // else add nums[R] to the set
                window.add(nums[R]);
        // if this point is reached, the entire array has been traversed so return False
        }
        return false;
    }
}
