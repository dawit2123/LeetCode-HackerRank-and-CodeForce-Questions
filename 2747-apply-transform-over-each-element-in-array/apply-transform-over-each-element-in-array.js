/**
 * @param {number[]} arr
 * @param {Function} fn
 * @return {number[]}
 */
var map = function(arr, fn) {
    let finalArray=[];
    arr.forEach((value, index)=>{
        finalArray.push(fn(value, index));
    });
    return finalArray;
};