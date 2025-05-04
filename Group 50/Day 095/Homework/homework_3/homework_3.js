// 3)შექმენით სია სადაც გექნებათ ობიექტები , ამ ობიექტებში უნდა გქონდეთ სტუდენტის სახელი,გვარი და ქულები, ქულები უნდა იყოს სია , 
// თქვენი დავალებაა გამოთვალოთ ქულების საშუალო შემდეგ გაფილტროთ მთავარი სია, ვისი საშუალო ქულაც იქნება მეტი ან ტოლი 90-ზე 
// ისინი გადაიტანეთ გაფილტრულ სიაში , შემდეგ map()-ის საშუალებით გადაუარეთ გაფილტრულ სიას და დააბრუნეთ ახალ სიაში მხოლოდ სტუდენტის სახელები

const student1 = {
    firstName: 'Noah',
    lastName: 'Thompson',
    scores: [75, 62, 81, 59, 59]
}

const student2 = {
    firstName: 'Liam',
    lastName: 'Carter',
    scores: [93, 88, 92, 89, 91, 91]
}

const student3 = {
    firstName: 'James',
    lastName: 'Reynolds',
    scores: [38, 52, 44, 61, 42]
}

const student4 = {
    firstName: 'Olivia',
    lastName: 'Bennett',
    scores: [78, 70, 80, 65, 76]
}

const student5 = {
    firstName: 'Ava',
    lastName: 'Morgan',
    scores: [95, 91, 89, 94, 90]
}

let studentArr = [student1, student2, student3, student4, student5]

let averageOf90Plus = student => {
    let sum = 0
    for(let num of student.scores){
        sum += num
    }
    return sum / student.scores.length >= 90
}

let filteredArr =  studentArr.filter(averageOf90Plus)
console.log(filteredArr)

let studentNames = student => student.firstName + ' ' + student.lastName

console.log(filteredArr.map(studentNames))