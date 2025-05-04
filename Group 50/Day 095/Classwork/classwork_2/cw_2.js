// 2)შექმენით სია სადაც გექნებათ რენდომ რიცხვები , შემდეგ ამ რიცხვებს გაფილტრავთ და ამოიღებთ მხოლოდ უარყოფით რიცხვებს , შემდეგ ამ სიას გადამაპავთ და თითოეულ ელემენტს გადააქცევთ დადებით რიცხვად

let numArr = [-354, 728, -912, 445, 159, -657, 803, -229, 976, -781,
    112, -88, 374, -631, 590, -1000, 911, -456, 73, -194,
    308, -707, 692, 820, -27, -993, 504, -358, 281, -123
]

const onlyNegatives = num => num < 0

let negatives = numArr.filter(onlyNegatives)

const negativeToPositive = num => num * -1

console.log(negatives.map(negativeToPositive))