class Solution {
    /**
     * @param {number[]} numbers
     * @param {number} target
     * @return {number[]}
     */
    twoSum(numbers: number[], target: number): number[] {
        //edge case: two numbers, so return [1,2]
        if(numbers.length === 2)
            return [1,2];
        
        //create a idx ptr starting from the leftmost + rightmost values

        let l:number = 0;
        let r:number = numbers.length - 1;

        while(l < r){
            //sum the values at these pointers
            const sum: number = numbers[l] + numbers[r];

            if(sum < target)
                l+=1
            else if(sum > target)
                r-=1
            else
                return [l+1, r+1]            
        }

    }
}
