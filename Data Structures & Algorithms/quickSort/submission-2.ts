/** Pair class to store key-value pairs */
// class Pair {
//   /**
//    * @param {number} key The key to be stored in the pair
//    * @param {string} value The value to be stored in the pair
//    */
//   constructor(key, value) {
//       this.key = key;
//       this.value = value;
//   }
// }
class Solution {
    /**
     * @param {Pair[]} pairs
     * @returns {Pair[]}
     */
    qSort(pairs:Pair[], s:number, e:number){
            // base case of empty pair or pair size 1: return
            if(e - s + 1 <= 1)
                return;
            // pick a pivot as end of list just cause
            const pivot = pairs[e].key;

            // perform partition
            // init left ptr at s
            let left = s;
            //for i from s to e
            for(let i = s; i < e; i++){
                // if value at i is less than pivot, swap val at i and left
                // and increment left

                if(pairs[i].key < pivot){
                    const tmp = pairs[i];
                    pairs[i] = pairs[left];
                    pairs[left] = tmp;
                    left +=1;
                }
            }

            //swap pivot element and left element
            const tmp = pairs[left];
            pairs[left] = pairs[e];
            pairs[e] = tmp;
            
            // perform qsort on arr left of pivot (s to left - 1)
            this.qSort(pairs,s,left-1);
            // perform qsort on arr right of pivot(left + 1 to e)
            this.qSort(pairs,left+1,e);

            //return
    }
    quickSort(pairs: Pair[]): Pair[] {
        this.qSort(pairs,0,pairs.length-1);
        return pairs;
    }
}
