/**
 * @param {string} word1
 * @param {string} word2
 * @return {string}
 */
var mergeAlternately = function(word1, word2) {
    const word1Length = word1.length; 
    const word2Length = word2.length; 
    let mergedString = ''
    if (word1Length === word2Length) {
        for(let i = 0; i < word1Length; i++) {
            mergedString += `${word1[i]}${word2[i]}`
        }
    } else if (word1Length > word2Length) {
        for (let i = 0; i < word2Length; i++) {
             mergedString += `${word1[i]}${word2[i]}`
        }
        for (let i = word2Length; i < word1Length; i++) {
            mergedString += word1[i]
        }
    } else {
        for (let i = 0; i < word1Length; i++) {
             mergedString += `${word1[i]}${word2[i]}`
        }
        for (let i = word1Length; i < word2Length; i++) {
            mergedString += word2[i]
        }
    }
    return mergedString; 
};