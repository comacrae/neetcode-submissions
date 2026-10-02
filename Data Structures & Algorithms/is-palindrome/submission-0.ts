class Solution {
    /**
     * @param {string} s
     * @return {boolean}
     */
    isPalindrome(s: string): boolean {
        const regex:RegExp = /[^\w\d]/g;
        const cleanedStr: string = s.toLowerCase().replaceAll(regex, "");
        let L:number = 0;
        let R:number = cleanedStr.length - 1;
        while(L < R && cleanedStr[L] === cleanedStr[R]){
            L += 1;
            R -= 1;
        }
        return L >= R;
    }
}
