let limit = 15;

for (let i = 1; i <= limit; i++) {
  if (i % 3 === 0 && i % 5 === 0) {
    console.log("FizzBuzz"); // multiples of both 3 and 5
  } else if (i % 3 === 0) {
    console.log("Fizz");     // multiples of 3
  } else if (i % 5 === 0) {
    console.log("Buzz");     // multiples of 5
  } else {
    console.log(i);          // numbers not divisible by 3 or 5
  }
}
