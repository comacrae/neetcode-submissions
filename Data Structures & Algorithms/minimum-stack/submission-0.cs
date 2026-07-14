public class MinStack {
    List<int> stack;
    List<int> mins;
    int min;

    public MinStack() {
        stack = new List<int>();
        mins = new List<int>();
    }
    
    public void Push(int val) {
        CheckMin(val);
        stack.Add(val);
    }
    
    public void Pop() {
        if(mins[mins.Count - 1] == stack[stack.Count - 1]) {
            mins.RemoveAt(mins.Count - 1);
        }

        stack.RemoveAt(stack.Count - 1);

        return;
    }
    
    public int Top() {
        return stack[stack.Count - 1];
    }
    
    public int GetMin() {
        return mins[mins.Count - 1];
    }

    private void CheckMin(int val) {
        if(mins.Count == 0){
            mins.Add(val);
        } else if (val <= mins[mins.Count - 1] ) {
            mins.Add(val);
        }
        return;
    }
}
