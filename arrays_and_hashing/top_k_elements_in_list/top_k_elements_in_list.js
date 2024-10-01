class Solution {
    /**
     * @param {number[]} nums
     * @param {number} k
     * @return {number[]}
     */
    topKFrequent(nums, k) {
        let countFrequency = new Map()
        // Count the frequency of the numbers in the provided array
        for (let num of nums) {
            let currentCount = countFrequency.get(num)
            if (currentCount != undefined) {
                countFrequency.set(num, currentCount +1) 
            } else {
                countFrequency.set(num, 1)
            }
        }

        // Convert the countFrequency map into a grouped set of values
        let orderedCount = new Array((nums.length + 1))
        countFrequency.forEach((value, key) => {
            if(orderedCount[value] == undefined) {
                orderedCount[value] = [key]
            } else {
                orderedCount[value].push(key)
            }
        })

        // Assemble the results array
        let results = []
        let currentPosition = -1
        while(results.length < k){
            let numberArray = orderedCount.at(currentPosition)
            if (numberArray != undefined) {
                for(let number of numberArray){
                    results.push(number)
                    if(results.length == k) { break }
                }
            }
            currentPosition -=1
        }
        return results
    }
}
