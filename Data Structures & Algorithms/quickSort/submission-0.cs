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
    public void QSort(List<Pair> pairs, int s, int e){

        if(e - s + 1 <= 1){
            return; // base case
        }

        //partition
        Pair tmp; // for swapping
        int pvt = e;
        int left = s;
        for(int i = s; i< e; i++){
            if(pairs[i].Key < pairs[pvt].Key){
                tmp = pairs[i]; // the one that is to be replaced by left
                pairs[i] = pairs[left];
                pairs[left] = tmp;
                left++;
            }
        }

        //swap left and pvt
        tmp = pairs[pvt];
        pairs[pvt] = pairs[left];
        pairs[left] = tmp;

        // do quicksort on left half and right half
        QSort(pairs, s, left - 1); //left half
        QSort(pairs, left+1, e); // right half
    }
    public List<Pair> QuickSort(List<Pair> pairs) {
            if(pairs == null){
                return pairs;
            }else if(pairs.Count == 0){
                return pairs;
            }

            QSort(pairs,0, pairs.Count() - 1);
            return pairs;
    }
}
