class Solution {
    /**
     * @param {string} s
     * @param {string} t
     * @return {boolean}
     */
    //An anagram is a string that contains the exact same characters as another string, but the order of the characters can be different.
    isAnagram(s, t) {
        // Immediately return if not equal
        if (s.length != t.length) { return false }

        // Build a map of all letters encountered, count them, then return if counts are equal
        let letter_count_s = new Map()
        let letter_count_t = new Map()
        for (let character of s) {
            if (letter_count_s.get(character) != undefined) {
                letter_count_s.set(character, letter_count_s.get(character) +1) 
            } else {
                letter_count_s.set(character, 0)
            }
        }

        for (let character of t) {
            if (letter_count_t.get(character) != undefined) {
                letter_count_t.set(character, letter_count_t.get(character) +1)
            } else {
                letter_count_t.set(character, 0)
            }
        }
        
        // Compare the maps
        if (letter_count_s.size == letter_count_t.size) {
            let s_map_iterator = letter_count_s.keys()
            for(let i = 0; i < letter_count_s.size; i++) {
                let active_key = s_map_iterator.next().value
                if(letter_count_s.get(active_key) != letter_count_t.get(active_key)) {
                    return false
                }
            }
        } else {
            return false
        }
        return true
    }
}
