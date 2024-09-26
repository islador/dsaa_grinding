class Solution {
    /**
     * @param {number[]} nums
     * @return {boolean}
     */
    hasDuplicate(nums) {
        let seen_numbers = []
        for (let i = 0; i < nums.length; i++){
            if (seen_numbers.includes(nums[i])){
                return true
            } else {
                seen_numbers.push(nums[i])
            }
        }
        return false
    }
}
