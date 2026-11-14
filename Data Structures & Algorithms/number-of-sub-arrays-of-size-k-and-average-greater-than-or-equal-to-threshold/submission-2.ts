class Solution {
    /**
     * @param {number[]} arr
     * @param {number} k
     * @param {number} threshold
     * @return {number}
     */
    numOfSubarrays(arr: number[], k: number, threshold: number): number {
        //return # of subarrays of size k where avg(subarr) >= threshold
        //start with window at L = 0, R = L + 1;
        let L:number = 0;
        let sum = 0;
        let count = 0;
        let avg = 0;

        for(let i = 0; i < k - 1; i++){
            sum += arr[i];
        }
        for(let R = k - 1; R < arr.length; R++){
            sum += arr[R];
            avg = sum / k;
            if (avg >= threshold)
                count++;
            sum -= arr[L];
            L++;
        }
        return count;
    }
}
