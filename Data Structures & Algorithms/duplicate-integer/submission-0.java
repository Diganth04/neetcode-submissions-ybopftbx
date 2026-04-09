class Solution {
    public boolean hasDuplicate(int[] nums) {
        Set<Integer> sset= new HashSet<>();
        for(int num:nums){
            sset.add(num);
        }
        if(sset.size()==nums.length){
            return false;
        }
        return true;
        
    }
}