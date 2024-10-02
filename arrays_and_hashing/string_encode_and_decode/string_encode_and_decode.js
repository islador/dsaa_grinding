class Solution {
  /**
   * @param {string[]} strs
   * @returns {string}
   */
  encode(strs) {
    let encodedString = ""
    for(let str of strs) {

    }
    return encodedString
  }

  /**
   * @param {string} str
   * @returns {string[]}
   */
  decode(str) {
    if (str.length > 0){
      return str.split("//")
    } else {
      return []
    }
  }
}

let solution = new Solution()
let encoded = solution.encode(["cat","dog","","mouse"])
console.log("Encoded: ", encoded)
console.log("Decoded: ", solution.decode(encoded))

let encoded2 = solution.encode(["\/\/","^.02@","meow","|\|\|"])
console.log("Encoded: ", encoded2)
console.log("Decoded: ", solution.decode(encoded2))


console.log("One Empty String")
let encoded3 = solution.encode([""])
console.log("Encoded: ", encoded3)
console.log("Decoded: ", solution.decode(encoded3))


console.log("Empty Array")
let encoded4 = solution.encode([])
console.log("Encoded: ", encoded4)
console.log("Decoded: ", solution.decode(encoded4))