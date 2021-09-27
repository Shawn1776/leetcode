class Solution {
public:
    int canCompleteCircuit(vector<int>& gas, vector<int>& cost) {
        // if total_gas < total_cost; then no way
        // a   --> x ---> b: 
        
        
        int n = gas.size();
        
        int total_gas = 0, total_cost = 0;
        int cur_gas = 0;
        int start = 0;
        
        for (int i = 0; i < n; i++){
            total_gas += gas[i] - cost[i];
            cur_gas += gas[i] - cost[i];
            
            if (cur_gas < 0){
                cur_gas = 0;
                start = i + 1;
            }// if  
        }//for 
        
        return total_gas >= 0 ? start : -1;
        
    }//fn
};
