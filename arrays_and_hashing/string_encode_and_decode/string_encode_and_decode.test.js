const Solution = require('./string_encode_and_decode');
const solution = new Solution()
describe('Encode', () => {

  test('An empty array outputs undefined', () => {
    let param = []
    expect(solution.encode(param)).toBe(undefined)
  });

  test('An array with an empty string outputs a string of "0@)"', () => {
    let param = [""]
    expect(solution.encode(param)).toEqual("0@)")
  });

  test('An array with three strings outputs a string following our delimiter logic', () => {
    let param = ["cat","","dog"]
    expect(solution.encode(param)).toEqual("3@)cat0@)3@)dog")
  });

  test('An array with a string containing our delimiter still outputs the correct character counts', () => {
    let param = ["cat","2@)","dog"]
    expect(solution.encode(param)).toEqual("3@)cat3@)2@)3@)dog")
  });

  test('An array with a double digit length string encodes a double digit number', () => {
    let param = ["cat","1234567890","dog"]
    expect(solution.encode(param)).toEqual("3@)cat10@)12345678903@)dog")
  });
})

describe('Decode', () => {
  test('An undefined input outputs an empty array', () => {
    let param = undefined
    expect(solution.decode(param)).toEqual([])
  });

  test('An empty string input outputs an array with an empty string', () => {
    let param = "0@)"
    expect(solution.decode(param)).toEqual([""])
  });

  test('An encoded string outputs the pre-encoding array', () => {
    let param = "3@)cat2@)it3@)dog"
    expect(solution.decode(param)).toEqual(["cat","it","dog"])
  });

  test('An encoded string with a zero length string inside outputs the pre-encoding array', () => {
    let param = "3@)cat0@)3@)dog"
    expect(solution.decode(param)).toEqual(["cat","","dog"])
  });

  test('An encoded string with our delimiter scheme as an input outputs the pre-encoding array correctly', () => {
    let param = "3@)cat3@)2@)3@)dog"
    expect(solution.decode(param)).toEqual(["cat","2@)","dog"])
  });
})
