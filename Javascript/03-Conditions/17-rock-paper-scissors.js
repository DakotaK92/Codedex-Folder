const player = 2;
const computer = Math.floor(Math.random()*3);

if (player === 0) {
  if (computer === 0){
    console.log('Draw');
  }else if (computer === 1) {
    console.log('The computer wins!')
  }else if (computer===2) {
    console.log('The player wins!')
  }else{
    console.log('An error has occurred')
  }

}else if (player === 1) {
  if (computer === 0) {
    console.log('The player has won!')
  }else if (computer ===1) {
    console.log('Draw')
  } else if (computer === 2) {
    console.log('The computer won!')
  }else {
    console.log('An error has occurred')
  }

}else if (player === 2) {
  if (computer === 0) {
    console.log('The computer won!')
  }else if ('computer === 1') {
    console.log('the player has won!')
  }else if ('computer === 2') {
    console.log('Draw')
  }else {
    console.log('An error has occurred')
  }

}else {
  console.log('An errors has occurred')
}