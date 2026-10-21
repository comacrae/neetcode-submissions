class Solution {
    /**
     * @param {string[]} operations
     * @return {number}
     */
    calPoints(operations: string[]): number {
        //init stack
        const st:number[] = [];
        //for each operation
        for(const op of operations){
            // if symbol is a plus, pop top two of stack and add sum to stack
                if(op === "+"){
                    st.push(st[st.length-1] + st[st.length-2]);
                }else if(op === "D"){
                // if symbol is a D, pop top of stack and double and add to stack
                    st.push(st[st.length-1] * 2);
                }else if( op === "C"){
                // if symbol is a C, pop top of stack (removing it)
                    st.pop();
                }else{
                //if symbol is a number, add to top of stack
                    st.push(Number(op));
                }            
        }
            return st.reduce((prev,curr)=> prev + curr,0);
        // return the sum of the stack
    }
}
