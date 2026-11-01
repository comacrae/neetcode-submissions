class Solution {
    /**
     * @param {number[]} numbers
     * @param {number} target
     * @return {number[]}
     */
    twoSum(numbers: number[], target: number): number[] {
        //idx1 < idx2
        //no hashmap
        // start pointer at the beginning and end
        let s = 0;
        let e = numbers.length - 1;
        //while s < e
        while(s < e ){
            // get sum
            let sum = numbers[s] + numbers[e];
            if(sum === target)
            // if sum == target, return [s + 1,e + 1]

                return [s+1,e+1];
            else if (sum > target){
                // if sum < target, move e left until new val
                while(e > 1 && numbers[e-1] === numbers[e])
                    e-=1;
                e-=1;

            }else{
                // if sum > target, move s right until new val
                while(s < numbers.length - 2 && numbers[s] === numbers[s+1])
                    s+=1;
                s+=1;
            }
        }
            
    }
}
