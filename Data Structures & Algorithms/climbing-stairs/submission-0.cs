public class Solution {
    public int ClimbStairs(int n) {     
        if(n < 0 ){
            return 0;
        }else if (n == 0){
            return 1;
        }else{
            return ClimbStairs(n-2) + ClimbStairs(n-1);
        }
    }
}
