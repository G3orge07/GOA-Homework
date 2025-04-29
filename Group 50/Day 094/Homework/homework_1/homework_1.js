// 1) შექმენით სია სადაც რენდომულად შეიტანთ რიცხვებს,
// შემდეგ დაწეეთ ფუნქცია რომელიც გადაუვლის თითოეულ ელემენტს სიაში და დააბრუნებს ახალ სიას სადაც იქნება მხოლოდ ლუწი რიცხვები,
// ასევე შექმენით იგივენაირი მეორე ფუნქცია კენტი რიცხვებისთვის

let numArr = [823, 510, -678, 902, 374, 156, 789, 91, -305, 667, 415, 22, 980, 731,
    -413, 308, 599,-729, 130, 486, 940, 61, -814, 237, -186, 771, 305, 194, -521, 843
]


function onlyEven(arr) {
    let result = []
    for (let num of arr){
        if (num % 2 == 0){
            result.push(num)
        }
    }
    return result
}

function onlyOdd(arr) {
    let result = []
    for (let num of arr){
        if (num % 2 != 0){
            result.push(num)
        }
    }
    return result
}

console.log(onlyEven(numArr))
console.log(onlyOdd(numArr))

