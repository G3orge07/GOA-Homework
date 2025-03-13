// Kata - Find Twins
//https://www.codewars.com/kata/5834315e06f227a6ac000099/train/javascript

function elimination(arr){

    for (let i=0; i<arr.length; i++){

      if (arr.slice(0,i).includes(arr[i]) || arr.slice(i+1).includes(arr[i])){
        return arr[i]
      }
    }

    return null
  }