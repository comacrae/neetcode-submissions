class NumArray {
    /**
     * @param {number[]} nums
     */
    private prefixSums:number[];
    private nums:number[];

    constructor(nums: number[]) {
        this.prefixSums = new Array<number>(nums.length);
        this.nums = nums;
        for(let i = 0; i < this.prefixSums.length; i++){
            if(i === 0)
                this.prefixSums[i] = nums[i];
            else
                this.prefixSums[i] = nums[i] + this.prefixSums[i-1];
        }
    }

    /**
     * @param {number} left
     * @param {number} right
     * @return {number}
     */
    sumRange(left: number, right: number): number {
        // 3 -1 2 4
        // 0  1 2 3
        // 3  2 4 8
        if(left === right)
            return this.nums[left];
        else if(left === 0)
            return this.prefixSums[right];
        else
            return this.prefixSums[right] - this.prefixSums[left - 1];

    }
}
