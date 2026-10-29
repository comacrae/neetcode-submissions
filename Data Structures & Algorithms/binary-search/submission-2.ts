class Solution {
    /**
     * @param {number[]} nums
     * @param {number} target
     * @return {number}
     */
    search(nums: number[], target: number): number {
        // edge case: if nums is emtpy, return 
        if (nums.length === 0)
            return -1
        
        // set left and right pointers
        let l = 0;
        let r = nums.length - 1;
        // while left pointer is less than right pointer
        while (l <= r){
            //get the mid 
            let mid = Math.floor((l + r) / 2);
            if(nums[mid] == target)
                //if value at mid equals target, return mid
                return mid;
            else if (nums[mid] < target)
                //if value at mid is less than target, set l to mid + 1
                l = mid + 1;
            else
                r = mid - 1;
            //if value at mid is greater than target, set r to mid - 1
        }

        return -1;

        // if we reach this point then l == r so return -1
    }
}
