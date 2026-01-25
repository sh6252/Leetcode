class Solution {
public:
    int lengthOfLastWord(string s) {
        int length=s.size();
        int l_i=length-1;
        while(l_i>=0&&s[l_i]==' '){
            l_i--;
        }
        if(l_i==-1){
            return 0;
        }
        int b_i=l_i;
        while(b_i>=0&&s[b_i]!=' '){
            b_i--;
        }
        return (b_i==-1)?l_i+1:l_i-b_i;
    }
};