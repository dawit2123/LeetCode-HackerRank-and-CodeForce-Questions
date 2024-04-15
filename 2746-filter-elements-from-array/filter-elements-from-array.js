/**
 * @param {number[]} arr
 * @param {Function} fn
 * @return {number[]}
 */
var filter = function(arr, fn) {
    let filteredArray=[];
    arr.forEach((value,index)=>{
        if(fn(value,index)){
            filteredArray.push(value);
        }
    });
    return filteredArray;
};