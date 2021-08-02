public class MyStack {
    Queue<int> queue1;
    Queue<int> queue2;
    
    /** Initialize your data structure here. */
    public MyStack() {
        queue1 = new Queue<int>();
        
    }
    
    /** Push element x onto stack. */
    public void Push(int x) {
            queue1.Enqueue(x);
         
    }
    
    /** Removes the element on top of the stack and returns that element. */
    public int Pop() {
        queue2 = new Queue<int>();
        if(queue1.Count==0)
            return -1;
        if (queue1.Count == 1)
            return queue1.Dequeue();
        while(queue1.Count>1)
            queue2.Enqueue(queue1.Dequeue());
        int top = queue1.Dequeue();
        queue1=queue2;
        return top;
    }
    
    /** Get the top element. */
    public int Top() {
        queue2 = new Queue<int>();
        if(queue1.Count==0)
            return -1;
        if (queue1.Count == 1)
            return queue1.Peek();
        while(queue1.Count>1)
            queue2.Enqueue(queue1.Dequeue());
        int top = queue1.Dequeue();
        queue2.Enqueue(top);
        queue1=queue2;
        return top;
    }
    
    /** Returns whether the stack is empty. */
    public bool Empty() {
        if(queue1.Count==0)
            return true;
        else
            return false;
    }
}

/**
 * Your MyStack object will be instantiated and called as such:
 * MyStack obj = new MyStack();
 * obj.Push(x);
 * int param_2 = obj.Pop();
 * int param_3 = obj.Top();
 * bool param_4 = obj.Empty();
 */