class Solution {
    /**
     * @param {number[]} temperatures
     * @return {number[]}
     */
    dailyTemperatures(temperatures: number[]): number[] {
        //init stack
        const st: Array<number[]> = new Array<number[]>();
        const output:Array<number> = new Array(temperatures.length).fill(0);
        // iterate through array
        for(let i = 0; i < temperatures.length; i++){
        // build input tuple (idx in temperatures arr, val at arr[idx])
            const tuple = [i, temperatures[i]];
            //check stack
            if(st.length > 0){ // if element on stack, is it less than curr?
                // look at stack top
                let top = st[st.length - 1];
                let topVal = top[1];
                let topIdx = top[0];
                //while stack.top < curr, calculate idx diffs
                // this works because stack stores in monotonically decreasing order
                while(topVal < temperatures[i] && st.length > 0){
                    top = st.pop();
                    topIdx = top[0];
                    output[topIdx] = i - topIdx;
                    if(st.length > 0)
                        topVal = st[st.length - 1][1];
                }
            }

            // push curr onto stack
            st.push(tuple);
        }

        //once through, return output array
        return output;
    }
}
