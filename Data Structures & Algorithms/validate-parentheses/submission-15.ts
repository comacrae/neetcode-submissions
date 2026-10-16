class Solution {
    /**
     * @param {string} s
     * @return {boolean}
     */
    isValid(s: string): boolean {
        //set up the stack
        const open = ["[","(","{"];
        const closed = ["]",")","}"];
        const parensMap: Record<string,string> = {
            "]":"[",
            ")":"(",
            "}":"{"
        };
        const st: Array<string> = new Array<string>();
        //for each char in string
        for(let i = 0; i < s.length; i++){
            let ch = s[i];
            // if it's an open parens push onto stack
            if(open.includes(ch)){
                st.push(ch)
            }else if (closed.includes(ch)){
            // if it's a closed paren pop the top element off the stack
                const top = st.pop();
            // and check if it matches the closed paren type
            // if it doesn't return false
                if(top !== parensMap[ch])
                    return false;
            }else{
            // if it's not a closed or open paren so  return false
                return false;
            }

        }
            
        // once we've reached end of loop, if stack is empty,
        // return true (is valid) else return false
        return st.length === 0;
    }
}
