/**
 * @param {Array} arr
 * @param {number} size
 * @return {Array}
 */
var chunk = function(arr, size) {
    let finalArray=[];
    for(let i=0; i<arr.length; i+=size){
        if(i+size>arr.length){
            finalArray.push(arr.slice(i,arr.length));
        }else{
            finalArray.push(arr.slice(i,i+size));
        }
    }
    return finalArray;
};
