class Solution {
    /**
     * @param {number[]} temperatures
     * @return {number[]}
     */
    dailyTemperatures(temperatures: number[]): number[] {
        // init output and stack
        const output = new Array(temperatures.length).fill(0);
        const st: number[]=[]; //idx array
        // for each element
        for(let i =0; i < temperatures.length; i++){

            const t = temperatures[i];
            
            //while stack not empty and curr temp > top of stack temp
            while(st.length > 0 && t > temperatures[st[st.length - 1]] ){
                // pop top of stack
                const prevIdx = st.pop();
                // for that temp's idx in output array, assign diff(curr_idx, temp_idx)
                output[prevIdx] = i - prevIdx;
            }

            // put current temp on idx
            st.push(i);
        }

        //return output
        return output;
    }
}
