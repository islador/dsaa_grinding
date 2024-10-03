module.exports = class Solution {
  /**
   * @param {string[]} strs
   * @returns {string}
   */
  encode(strs) {
    if(strs.length == 0) { return undefined }
    let encodedString = ""

    for(let i = 0; i < strs.length; i++) {
      encodedString = encodedString.concat('\"',strs[i],'\"')
      if(i < (strs.length - 1)){
        encodedString = encodedString.concat(',')
      }
    }
    //console.log("encodedString: ", encodedString)
    return encodedString
  }

  /**
   * @param {string} str
   * @returns {string[]}
   */
  decode(str) {
    if(str == undefined) { return [] }
    console.log("str: ", str)
    if (str.length > 0){
      return str.split('","')
    } else {
      return []
    }
  }
}