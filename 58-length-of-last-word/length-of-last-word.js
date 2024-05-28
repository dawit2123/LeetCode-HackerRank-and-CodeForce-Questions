/**
 * @param {string} s
 * @return {number}
 */
var lengthOfLastWord = function(s) {
    let modifiedStr= s.trim();
    let strArr=modifiedStr.split(' ');
    return strArr[strArr.length-1].length;
};