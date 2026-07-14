// Definition for a pair.
// public class Pair {
//     public int Key;
//     public string Value;
//
//     public Pair(int key, string value) {
//         Key = key;
//         Value = value;
//     }
// }
public class Solution {
    public void Merge(List<Pair> pairs, int l, int m, int r){
        int leftSize = m - l + 1;
        int rightSize = r - m;

        //create copy lists

        List<Pair> leftCopy = new List<Pair>();
        List<Pair> rightCopy = new List<Pair>();

        for(int i = l; i <= m; i++){
            leftCopy.Add(pairs[i]);
        }

        for(int i = m + 1; i <= r; i++){
            rightCopy.Add(pairs[i]);
        }

        //merge copy lists into input list while sorting, maintaining a pointer for
        // each copy list and the input list
        int lPtr = 0;
        int rPtr = 0;
        int mergePtr = l;
        while(lPtr < leftSize && rPtr < rightSize){
            if(leftCopy[lPtr].Key <= rightCopy[rPtr].Key){
                pairs[mergePtr] = leftCopy[lPtr++];
            }else{
                pairs[mergePtr] = rightCopy[rPtr++];
            }
            mergePtr++;
        }
        // at this point, there may still be some values left over; fill the rest
        if(lPtr < leftSize){
            while(lPtr < leftSize){
                pairs[mergePtr] = leftCopy[lPtr];
                mergePtr++;
                lPtr++;
            }
        }else if(rPtr < rightSize){
            while(rPtr < rightSize){
                pairs[mergePtr] = rightCopy[rPtr];
                mergePtr++;
                rPtr++;
            }
        }
    }
    public List<Pair> MergeSortNeet(List<Pair> pairs, int l, int r){
        
        if(l < r){
            int m = (l + r) / 2; //determine split index
            MergeSortNeet(pairs, l, m);
            MergeSortNeet(pairs,m+1,r);
            Merge(pairs, l, m, r);
        }
        return pairs;
    }
    public List<Pair> MergeSort(List<Pair> pairs) {
            return MergeSortNeet(pairs, 0, pairs.Count - 1);
    }

}
