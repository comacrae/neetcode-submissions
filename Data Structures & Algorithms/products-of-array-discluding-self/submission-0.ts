class Solution {
    /**
     * @param {number[]} nums
     * @return {number[]}
     */
    productExceptSelf(nums: number[]): number[] {
        const output: number[] = [];
        let product:number = 1;
        let zerosCount:number = 0;
        for(const num of nums){
            if(num != 0){
                product = product * num;
            }else{
                zerosCount+=1;
            }
        }
        if(zerosCount > 1){
            return Array.from({length:nums.length}, () => 0);
        }

        for(let i = 0; i < nums.length; i++){
            if(zerosCount == 1){
                if(nums[i] == 0) output[i] = product
                else output[i] = 0;
            }else{
                output[i] = product / nums[i];
            }
        }

        return output;
    }
}
