class Solution {
    /**
     * @param {number[]} nums
     * @param {number} target
     * @return {number[]}
     */
    twoSum(nums, target) {
        let soughtAddends = new Map()
        let seenNumbers = new Map()
        for(let i = 0; i < nums.length; i++) {
            let inputNumber = nums[i]
            const soughtAddend = target - inputNumber
            if(soughtAddends.has(inputNumber)) {
                return [soughtAddends.get(inputNumber), i]
            }
            if(seenNumbers.has(soughtAddend)) {
                return [seenNumbers.get(soughtAddend), i]
            }
            // I want to preserve the lowest index value of the seen and sought numbers, so I can't just overwrite them.
            if(soughtAddends.has(soughtAddend) == false) {
                soughtAddends.set(soughtAddend, i)
            }
            if(seenNumbers.has(inputNumber) == false) {
                seenNumbers.set(inputNumber, i)
            }
        }

    }
}
