class Solution {
    /**
     * @param {number[]} nums
     * @param {number} target
     * @return {number[]}
     */
    twoSum(nums: number[], target: number): number[] {
        //two ptr solution
        //convert nums to tuples of the value and their idx
        const tuples = nums.map((val,idx)=>[idx,val]);

        //sort tuples by their value
        tuples.sort((a,b) => a[1] - b[1]);

        //start ptr at beginning and end of arr
        let s = 0;
        let e = tuples.length - 1;
        while(s < e){
            const sum = tuples[s][1] + tuples[e][1];

            //if val_start and val_end sum == target return idxs
            if(sum == target)
                return [tuples[s][0], tuples[e][0]];
            //if sum < target, move start ptr up
            else if(sum < target){
                // move ptr up while next val same as curr val
                while(s < tuples.length - 2 && tuples[s][1] === tuples[s+1][1])
                    s+=1;
                s+=1;
            }else{ //if sum > target, move end ptr down
            //move ptr down while prev val same as curr val
                while(e > 1 && tuples[e][1] === tuples[e - 1][1])
                    e-=1;
                e-=1;
            }
        }
        

    }
}
