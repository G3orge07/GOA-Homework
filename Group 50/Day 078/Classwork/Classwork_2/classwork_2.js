// 2) createElement-ის გამოყენებით შექმენით ერთი მშობელი div-ელემენტი, ეს div-ი ჩაამატეთ body-ში , შემდეგ ამ მშობელ div-ში ჩაამატეთ კიდევ ორი შვილი div-ი და განალაგეთ ვერტიკალურად ერთმანეთისგან თანაბარი დაშორებით ,  პირველი დივი იყოს წითელი მეორე იყოს მწვანე , ასევე დაუმატეთ სასურველი სტილები

let parentDiv = document.createElement('div')

document.body.appendChild(parentDiv)

let div1 = document.createElement('div')
let div2 = document.createElement('div')

parentDiv.appendChild(div1)
parentDiv.appendChild(div2)

parentDiv.style.width = '300px'
parentDiv.style.height = '500px'
parentDiv.style.display = 'flex'
parentDiv.style.flexDirection = 'column'
parentDiv.style.justifyContent = 'space-around'
parentDiv.style.alignItems = 'center'
parentDiv.style.border = 'solid black'
parentDiv.style.margin = '100px'


div1.style.width = '200px'
div1.style.height = '150px'
div1.style.border = '2px solid black'
div1.style.backgroundColor = 'red'

div2.style.width = '200px'
div2.style.height = '150px'
div2.style.border = '2px solid black'
div2.style.backgroundColor = 'green'