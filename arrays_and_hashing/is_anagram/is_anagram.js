class Solution {
    /**
     * @param {string} s
     * @param {string} t
     * @return {boolean}
     */
    isAnagram(s, t) {
        // Sliding pointers?
        for(let i = 0; i < s.length; i++) {
            let s_index = i
            let t_index = (t.length - i)-1
            
            console.log("t_index: ", t_index, "s_index: ", s_index)
            console.log("t at index: ", t.at(t_index), "s at index: ", s.at(s_index))
            if(s.at(s_index) != t.at(t_index)) { return false}
        }
        return true
    }
}
