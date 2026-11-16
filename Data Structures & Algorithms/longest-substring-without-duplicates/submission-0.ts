class Solution {
    /**
     * @param {string} s
     * @return {number}
     */
    lengthOfLongestSubstring(s: string): number {
        let currMax = 0;
        let L = 0;
        let set = new Set<string>();
        for (let R = L; R < s.length; R++){
            if(!set.has(s[R])){
                set.add(s[R]);
                if(R - L + 1 > currMax)
                    currMax = R - L + 1;
            }else{
                while(s[L] !== s[R]){
                    set.delete(s[L]);
                    L++;
                }
                L++;
            }
        }
        return currMax;
    }
}
