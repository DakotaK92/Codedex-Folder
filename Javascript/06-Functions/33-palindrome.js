function isPalindrome(word) {
  let reversedWord = "";

  let lowerCase = word.toLowerCase();

  for(let i = lowerCase.length - 1; i >= 0; i--) {
    reversedWord += lowerCase[i]
  }

  return reversedWord === lowerCase

}

console.log(isPalindrome("Racecar"))