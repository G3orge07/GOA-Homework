// 2)შექმენით სია სადაც გექნებათ 5 ობიექტი , ამ ობიექტებში შეინახავთ მომხმარებლის სახელს და ასაკს , 
// თქვენი დავალებაა გაფილტროთ ეს სია და დატობოთ მხოლოდ იმ მომხმარებლის ობიექტები ვისი ასაკიც მეტი ან ტოლი იქნება 18 ზე

const user1 = {
    name: 'George',
    age: 16
}

const user2 = {
    name: 'Mark',
    age : 21
}

const user3 = {
    name: 'Helly',
    age: 34
}

const user4 = {
    name: 'Steve',
    age: 17
}

const user5 = {
    name: 'Chris',
    age: 41
}

let userArr = [user1, user2, user3, user4, user5]

let over18 = user => user.age >= 18

console.log(userArr.filter(over18))