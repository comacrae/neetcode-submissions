class Solution {
    /**
     * @param {number[][]} matrix
     * @param {number} target
     * @return {boolean}
     */
    searchMatrix(matrix: number[][], target: number): boolean {
        //find row using binary search
        // set row top and row bottom
        let rowTop = 0;
        let rowBottom = matrix.length - 1;
        // while row top <= row bottom:
        while(rowTop <= rowBottom){
            // set row idx to middle of window
            let rowMid = Math.floor((rowTop + rowBottom) / 2);
            let row = matrix[rowMid];
            let eor = row[row.length - 1];
            // check the end of that row (EOR):
                if(eor == target)
                    // if EOR == target return true
                    return true;
                else if (eor < target){
                    // if EOR < target, move row top down
                    rowTop = rowMid + 1;
                }else{
                // if EOR > target, search that row
                    // set l to beginning and r to end idx
                    let l = 0;
                    let r = row.length - 1;
                    // while l <= r
                    while(l <= r){
                        // get mid idx
                        let mid = Math.floor((l+r)/2);

                        // if value at mid == target, return true
                        if (row[mid] == target)
                            return true;
                        else if (row[mid] > target)
                            // if value at mid > target, move r to left of mid
                            r = mid - 1;
                        else
                        // if value at mid < target, move l to right of mid
                            l = mid + 1
                    }
                    // if we break out of loop, didnt find value so move row bottom up
                    rowBottom = rowMid - 1;
                }
        }
        // if we reach this point return false
        return false;
    }
}
