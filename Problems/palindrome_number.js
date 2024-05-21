var isPalindrome = function(x) {
    // x=x.toString()
    // for (i = 0; i < x.length; i++){
    //     for(j = 0; j > x.length-1; j--){
    //        if(x[i]===x[j]){
    //        return true}
    //     }
    // }return false

    const str = String(x);

  if(x.length <= 1) {
    return true;
  }

  if (str[0] !== str[str.length - 1]) {
    return false;
  }

  return isPalindrome(str.slice(1, str.length - 1));
};