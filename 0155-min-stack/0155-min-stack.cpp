class MinStack {
    stack<int> all_nums;
    stack<int> min_nums;
public:
    MinStack() {
    }
    
    void push(int val) {
        all_nums.push(val);
        if(!min_nums.empty()){
            int top_min = min_nums.top();
            if(top_min >= val){
                min_nums.push(val);
            }
        } else{
            min_nums.push(val);
        }
    }
    
    void pop() {
        if(!all_nums.empty()){
            int val = all_nums.top();
            all_nums.pop();
            if(val == min_nums.top()){
                min_nums.pop();
            } 
        }       
    }
    
    int top() {
        if(!all_nums.empty())
            return all_nums.top();
        else
            return 0;
    }
    
    int getMin() {
        if(!min_nums.empty())
            return min_nums.top();
        else
            return INT_MAX;
    }
};

/**
 * Your MinStack object will be instantiated and called as such:
 * MinStack* obj = new MinStack();
 * obj->push(val);
 * obj->pop();
 * int param_3 = obj->top();
 * int param_4 = obj->getMin();
 */