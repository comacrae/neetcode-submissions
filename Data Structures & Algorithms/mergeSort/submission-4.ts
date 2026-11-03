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
    merge(pairs:Pair[], l:number, m:number, r:number):void{
        const leftHalf = pairs.slice(l,m+1);
        const rightHalf = pairs.slice(m+1,r+1);
        let srcPtr = l; 
        let lPtr = 0;
        let rPtr = 0;
        while(srcPtr <= r && lPtr < leftHalf.length && rPtr < rightHalf.length){
            if(rightHalf[rPtr].key < leftHalf[lPtr].key){
                pairs[srcPtr] = rightHalf[rPtr];
                rPtr +=1;
            }else{
                pairs[srcPtr] = leftHalf[lPtr];
                lPtr +=1;
            }
            srcPtr +=1;
        }

        while(lPtr < leftHalf.length){
            pairs[srcPtr] = leftHalf[lPtr];
            srcPtr +=1;
            lPtr +=1;
        }

        while(rPtr < rightHalf.length){
            pairs[srcPtr] = rightHalf[rPtr];
            srcPtr +=1;
            rPtr +=1;
        }
    }

    mSort(pairs:Pair[], l:number,r:number):void{
        if(r <= l)
            return;
        let m = Math.floor((l+r)/2);
        this.mSort(pairs,l,m);
        this.mSort(pairs,m+1,r);
        this.merge(pairs,l,m,r);
    }
    mergeSort(pairs: Pair[]): Pair[] {
        this.mSort(pairs,0,pairs.length-1);
        return pairs;
    }
}
