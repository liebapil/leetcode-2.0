/**
 * @param {string} s
 * @return {number}
 */
var romanToInt = function(s) {
    const romToIntMap = {'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000 }
    let total = 0;
    let prevValue = 0;

    for (let i=0; i<s.length; i++){
        let curVal = romToIntMap[s[i]]
    
    if (curVal > prevValue){
        total += curVal -2 * prevValue;
    } else {
        total += curVal
    }

    prevValue = curVal
    }
    return total
};