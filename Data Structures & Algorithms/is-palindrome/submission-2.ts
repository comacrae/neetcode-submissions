class Solution {
    /**
     * @param {string} s
     * @return {boolean}
     */
    isPalindrome(s: string): boolean {
        /*
        t   a   b   a   b   a   t
        0   1   2   3   4   5   6
                    lr 
        */
        let l = 0;
        s = s.toLowerCase().replace(/[^a-z0-9]/g, '');
        let r = s.length - 1;
        while (l <= r){
            if(s[l] !== s[r]){
                return false;
            }
            l = l + 1;
            r  = r - 1;
        }
        return true;

    }
}
