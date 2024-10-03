module.exports = class Solution {
  /**
   * @param {string[]} strs
   * @returns {string}
   */
  encode(strs) {
    if(strs.length == 0) { return undefined }
    let encodedString = ""

    for(let inputString of strs) {
      encodedString = encodedString.concat(inputString.length).concat("@)").concat(inputString)
    }
    return encodedString
  }

  /**
   * @param {string} str
   * @returns {string[]}
   */
  decode(str) {
    if(str == undefined) { return [] }
    console.log("str: ", str)
    let results = []
    let readingEncodingInput = true
    let falseReadingEncodingInputNextIteration = false
    let atEncountered = false
    let closeParenEncountered = false
    let delimitedString = ""

    let remainingCharactersInEncodedString = 0
    let encodedString = ""    
    
    for(let character of str) {
      console.log("character: ", character)
      // Wait an iteration and reset everything
      if(falseReadingEncodingInputNextIteration == true){
        console.log("resetting")
        readingEncodingInput = false
        atEncountered = false
        closeParenEncountered = false
        delimitedString = ""
      }
      // Ingest and process the encoded input if that is where the cursor is
      if(readingEncodingInput == true) {
        console.log("building delimitedString")
        delimitedString = delimitedString.concat(character)
        if(character == "@") {
          atEncountered = true
        }
        if(atEncountered == true) {
          if(character == ")") {
            closeParenEncountered = true
          }
        }
        if(atEncountered == true && closeParenEncountered == true) {
          remainingCharactersInEncodedString = parseInt(delimitedString.split("@")[0])
          console.log("setting remainingCharactersInEncodedString:", remainingCharactersInEncodedString)

          if(remainingCharactersInEncodedString == 0){
            results.push("")
            console.log("Pushing zero string")
            atEncountered = false
            closeParenEncountered = false
            delimitedString = ""
          }else{
            falseReadingEncodingInputNextIteration = true
          }
        }
      }
      //
      if(readingEncodingInput == false) {
        console.log("remainingCharactersInEncodedString: ", remainingCharactersInEncodedString)
        encodedString = encodedString.concat(character)
        if(remainingCharactersInEncodedString == 1) {
          console.log("encodedString:", encodedString)
          readingEncodingInput = true
          falseReadingEncodingInputNextIteration = false
          results.push(encodedString)
          encodedString = ""
        }
        remainingCharactersInEncodedString -=1
      }
    }
    console.log("results Length: ", results.length)
    return results
  }
}