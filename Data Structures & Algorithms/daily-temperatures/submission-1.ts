class Solution {
    /**
     * @param {number[]} temperatures
     * @return {number[]}
     */
    dailyTemperatures(temperatures: number[]): number[] {
        //init stack
        const st = [];
        const output = new Array(temperatures.length).fill(0);
        // for each value
        for (const [index, temp] of temperatures.entries()){
            // if stack is not empty
            if(st.length != 0){
                // while curr val > top of stack
                while(st.length > 0 && temp > st[st.length-1][0] ){
                    // pop top of stack
                    let top = st.pop();
                    // at that stack val's idx, set diff(curr idx, stack val idx)
                    output[top[1]] = index - top[1];
                }   
            }
            // add curr value to stack 
            st.push([temp,index]);
        }
        // skip remaining stack vals and return
        return output;
    }
}
