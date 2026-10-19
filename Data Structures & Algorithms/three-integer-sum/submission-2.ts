class Solution {
    /**
     * @param {number[]} nums
     * @return {number[][]}
     */
    threeSum(nums: number[]): number[][] {
        // sort the input array
        nums.sort((a,b)=> a - b);
        const output = [];
        let i = 0;
        while(i < nums.length - 2){
            //set the window
            let j = i + 1;
            let k = nums.length -1;
            // check out the values in the window
            while(j < k){
                const target = nums[i] * -1;
                const sum = nums[j] + nums[k];
                if(sum < target){
                    j++;
                }else if(sum > target){
                    k--;
                }else{
                    output.push([nums[i],nums[j],nums[k]]);
                    j++;
                    k--;
                    while(nums[j] === nums[j-1] && j < k)
                        j++;
                    while(nums[j] === nums[k + 1] && k > j)
                        k--;
                }
               
            }
            i++;
            while(i < nums.length - 2 && nums[i] == nums[i-1])
                i++;
        }
        return output;
    }
}
