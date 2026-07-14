public class Solution {
    public bool IsValid(string s) {
        int n = s.Length;

        List<char> stack = new List<char>();
        char ch = 'z';
        char popped = 'z';
        char[] startParens = { '{', '(', '['};
        char[] endParens = { '}', ')', ']'};

        if(n % 2 != 0) {
            return false;
        };

        for(int i  = 0; i < n; i++){
            ch = s[i];

            if(startParens.Contains(ch)){
                stack.Add(ch);
            }else if(endParens.Contains(ch) && stack.Count == 0){
                return false;
            } 
            else{
                popped = stack[stack.Count-1];
                stack.RemoveAt(stack.Count - 1);

                if(ch == ')' && popped != '('){
                    return false;
                }

                if(ch == ']' && popped != '['){
                    return false;
                }   

                if(ch == '}' && popped != '{'){
                    return false;
                }                                        
            }
        }

        return stack.Count == 0;

    }
}
