class Solution {
    /**
     * @param {number[]} nums
     * @return {boolean}
     */
    hasDuplicate(nums) {
        let seen_numbers_set = new Set()
        for (let num of nums){
            if (seen_numbers_set.has(num)) {
                return true 
            } else {
                seen_numbers_set.add(num)
            }
        }
        return false
    }
}
