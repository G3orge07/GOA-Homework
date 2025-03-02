
let num = prompt("Enter a num: ")

let count = 0

for(let i = 1; i<=num; i++){
    if (i%2 == 0){
        count+=i
    }
}

console.log(count)