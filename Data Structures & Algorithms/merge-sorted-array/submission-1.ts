class Solution {
    /**
     * @param {number[]} nums1
     * @param {number} m
     * @param {number[]} nums2
     * @param {number} n
     * @return {void} Do not return anything, modify nums1 in-place instead.
     */
    merge(nums1: number[], m: number, nums2: number[], n: number): void {
        //make copy of nums1 from [0,m)
        const copy = nums1.slice(0,m);
        // init 3 pointers
        let n1 = 0;
        let n2 = 0;
        let c = 0;
    

        // while all pointers in bounds
        while(c < m && n2 < n && n1 < (m+n)){
            // if copy <= nums2:
            if(copy[c] <= nums2[n2]){
                //get copy val & increment copy ptr
                nums1[n1] = copy[c];
                c+=1;
            }else{
                // else get n2 val and increment n2 ptr
                nums1[n1] = nums2[n2];
                n2+=1;
            }
            //increment nums1 ptr
            n1+=1;
        }

        // fill n1 with leftovers from copy
        while(c < m){
            nums1[n1] = copy[c];
            c+=1;
            n1+=1;
        }
        // fill n1 with leftovers from n2
        while(n2 < n){
            nums1[n1] = nums2[n2];
            n2+=1;
            n1+=1;
        }

        return;
    }
}
