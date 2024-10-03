const Solution = require('./string_encode_and_decode');
const solution = new Solution()
describe('Encode', () => {

  test.skip('An empty array outputs undefined', () => {
    let param = []
    expect(solution.encode(param)).toBe(undefined)
  });

  test.skip('An array with an empty string outputs an escaped string', () => {
    let param = [""]
    expect(solution.encode(param)).toEqual("\"\"")
  });

  test.skip('An array with three strings outputs a string with multiple escapes', () => {
    let param = ["cat","","dog"]
    expect(solution.encode(param)).toEqual("\"cat\",\"\",\"dog\"")
  });
})

describe('Decode', () => {
  test.skip('An undefined input outputs an empty array', () => {
    let param = undefined
    expect(solution.decode(param)).toEqual([])
  });

  test('An empty string input outputs an array with an empty string', () => {
    let param = '""'
    expect(solution.decode(param)).toEqual([""])
  });

  test.skip('An escaped string outputs the pre-encoding array', () => {
    let param = "\"cat\",\"\",\"dog\""
    expect(solution.decode(param)).toEqual(["cat","","dog"])
  });
})
