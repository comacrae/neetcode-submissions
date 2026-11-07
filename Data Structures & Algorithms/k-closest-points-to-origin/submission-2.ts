class Solution {
    /**
     * @param {number[][]} points
     * @param {number} k
     * @return {number[][]}
     */

    /*
    *Qsort: pick the closest point to the origin  
    */
    qsort(distances:{pt:number[],dist:number}[], st:number, end:number, k:number){
        // init ptrs
        let left:number = st;
        const pivotIdx = st + Math.floor((Math.random() * (end - st + 1))); // btw st and end
        //swap pivot to end temporarily
        const pivot = distances[pivotIdx];
        distances[pivotIdx] = distances[end];
        distances[end] = pivot;

        for(let i = st; i < end; i++){
            // for each val in idx
            if(distances[i].dist <= pivot.dist){
                // if less than pivot, swap with the left holder
                const tmp = distances[i];
                distances[i] = distances[left];
                distances[left] = tmp;
                left +=1;
            }
        }
        //swap val at left and pivot idx
        const tmp = distances[left];
        distances[left] = pivot
        distances[end] = tmp;
        // now everything to left of pivot is less than pivot
        if(left === (k-1))
            return
        else if (left < (k-1)) // still more values in right of array, so sort those
            this.qsort(distances,left+1, end, k) 
        else // we need to sort the left half some more
            this.qsort(distances,st, left-1, k);
    }
    kClosest(points: number[][], k: number): number[][] {
        //convert points to an array of (points, dist) so we can sort by dist

        //eucl dist from origin
        const eucl = (pt:number[]): number => Math.sqrt(((pt[1])**2) + ((pt[0])**2));

        const distances = points.map((pt) => ({'pt':pt, 'dist':eucl(pt)}))

        //sort via quicksort modified
        this.qsort(distances,0, distances.length - 1, k);

        return distances.map((d) => d.pt).slice(0,k);
    }
}
