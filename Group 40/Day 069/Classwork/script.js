
let num = Number(prompt('Enter a number: '))

let choice = prompt("Filter the numbers from 1 to your number. Which numbers would you like? 1) Eeven; 2) Odd; 3)Their Squares; 4) Multiples of three. Your choice should be a number.")

if(choice=='1'){
    for (let i = 1; i<num; i++){
        if (i%2==0){
            console.log(i)
        }
    }
}else if(choice=='2'){
    for (let i = 1; i<num; i++){
        if (i%2!=0){
            console.log(i)
        }
    }
}else if(choice=='3'){
    for (let i = 1; i<num; i++){
        console.log(i**2)
    }
}else if(choice=='4'){
    for (let i = 1; i<num; i++){
        if (i%3==0){
            console.log(i)
        }
    }
}