class Solution {
    /**
     * @param {string[]} strs
     * @return {string[][]}
     */
    groupAnagrams(strs) {
        let knownAnagrams = new Map()
        for(let string of strs){
            // Assemble a count of all the letters
            let letterHash = new Map()
            let sortedString = string.split("").sort().join("")
            for (let character of sortedString) {
                if (letterHash.get(character) != undefined) {
                    letterHash.set(character, letterHash.get(character) +1) 
                } else {
                    letterHash.set(character, 1)
                }
            }
            // Turn the map into a lookup key
            let lookupKey = ""
            letterHash.forEach((values, keys) => {
                lookupKey = lookupKey.concat(keys,values)
            })
            // Group anagrams
            if (knownAnagrams.get(lookupKey) != undefined) {
                let answerList = knownAnagrams.get(lookupKey)
                answerList.push(string)
                knownAnagrams.set(lookupKey, answerList) 
            } else {
                knownAnagrams.set(lookupKey, [string])
            }
        }
        let results = []
        knownAnagrams.forEach((values, keys) => {
            results.push(values)
        })
        return results
    }
}
