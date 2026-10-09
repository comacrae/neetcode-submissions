class Solution {
    /**
     * @param {number[]} nums
     * @return {number[]}
     */
    productExceptSelf(nums: number[]): number[] {
        const n = nums.length;
        //prefix[i] = product of all elements with idx < i
        const prefix = Array.from({length: n}, ()=>0);

        //suffix[i] = product of all elements with idx > i
        const suffix = Array.from({length: n}, ()=>0);

        //output[i] = product of all elements excluding i
        const output = Array.from({length: n}, ()=>0);

        prefix[0] = 1; // no values to left of idx 0
        suffix[n-1] =1; // no values to right of idx n-1
        
        for(let i = 1; i < n; i++){
            prefix[i] = prefix[i - 1] * nums[i-1];
        }
        for(let i = n - 2; i >= 0; i--){
            suffix[i] = suffix[i + 1] * nums[i+1];
        }
        for(let i = 0; i < n; i++){
            output[i] = suffix[i] * prefix[i];
        }

        return output;
    }
}
