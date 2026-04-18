class Solution {
    /**
     * @param {string} s
     * @param {string} t
     * @return {boolean}
     */

    // "racecar" 
    // "carrace"

    // {""}

    isAnagram(s, t) {
        if (s.length !== t.length) {
            return false;
        }
        let wordMapS = {}
        for (let char of s) {
            if (wordMapS.hasOwnProperty(char)) {
                wordMapS[char] += 1 
            } else {
                wordMapS[char] = 1
            }
        }
        let wordMapT = {}
        for (let char of t) {
            if (wordMapT.hasOwnProperty(char)) {
                wordMapT[char] += 1 
            } else {
                wordMapT[char] = 1 
            }
        }
        for (let char of Object.keys(wordMapS)) {
            if (wordMapT[char] !== wordMapS[char]) {
                return false
            }
        }
        return true;
    }
}
