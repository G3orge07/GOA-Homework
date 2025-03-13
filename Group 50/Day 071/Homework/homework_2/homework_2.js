
//for-ციკლის გამოყენებით იპოვეთ სიაში ყველაზე დიდი და ყველაზე პატარა რიცხვები

let list = [34, -2, 98, -45, 5, 12, 67, -13, 125, 77]

let largest = list[0]
let smallest = list[0]

for (let num of list){
    if (num > largest){
        largest = num
    }
    if (num < smallest){
        smallest = num
    }
}

console.log('Largest = ' + String(largest) + '   Smallest = ' + String(smallest))