class Solution {

    private String recursive(int n){
        if(n == 1){
            return "1";
        }
        String prevString = recursive(n-1);
        String res = "";
        int len = prevString.length(),cnt = 1;
        char prev = prevString.charAt(0);
        for(int i = 1; i < len ; i++){
            if(prevString.charAt(i) == prev){
                cnt++;
                continue;
            }
            String t = "" + cnt + prev;
            res += t;
            prev = prevString.charAt(i);
            cnt = 1;
        }
        String t = "" + cnt + prev;
        res += t;
        return res;
    }

    public String countAndSay(int n) {
        return recursive(n);
    }
}