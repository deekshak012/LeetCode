
#NOT THE BEST SOLUTION, REFER PY FOR THE BEST SOLUTION
public class MinStack {

    public Stack<int> stack;
    public MinStack() {
        stack = new Stack<int>();
    }
    
    public void Push(int val) {
        stack.Push(val);
        
    }
    
    public void Pop() {
        stack.Pop();
    }
    
    public int Top() {
        return stack.Peek();
    }
    
    public int GetMin() {
        int min=Int32.MaxValue;
        foreach (int num in stack)
            if (num< min)
                min=num;
        return min;
    }
}
