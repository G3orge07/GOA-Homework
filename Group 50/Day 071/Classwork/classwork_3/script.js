
let list = [9, 7, 13, 24, 34, 2, 5, 11, 8, 93, 45, 30, 21, 7, 9, 7, 13, 24, 34, 2, 5, 11, 8, 93, 45, 30, 21, 7,1]

let sum = 0

for (let num of list){
    if (num%2 == 0){
        sum += num**2
    }
}

console.log(sum)