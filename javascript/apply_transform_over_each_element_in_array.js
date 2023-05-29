/**
 * @param {number[]} arr
 * @param {Function} fn
 * @return {number[]}
 */
var map = function(arr, fn) {
    const transformed_arr = []
    for (let i = 0; i < arr.length; i++) {
        transformed_arr.push( fn(arr[i], i) )
    }   
    return transformed_arr
};