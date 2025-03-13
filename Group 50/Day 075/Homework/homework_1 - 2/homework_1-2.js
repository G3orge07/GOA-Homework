//   1)შექმენით ობიექტი car , რომელსაც ექნება 5 key -  company(მწარმოებელი) , model , milage ,year , condition , ამ ობიექტში ასევე უნდა იყოს შენახული ფუნქცია , ამ ფუნქციას პარამეტრად ჰქონდეს condition ,და ამ ფუნქციაში შეამოწმეთ , რომ თუ condition-არის კარგი ან ცუდი დაბეჭდეთ შემდეგი ტექსტი car is in {condition} condition გამოიყენეთ format-ი

const car = {
    company: 'BMW',
    model: '3 Series',
    mileage: '10KM',
    year: 2024,
    condition: 'good',
    Condition() {
        console.log('The car is in ' + this.condition + ' condition.')
    }

}

car.Condition()


// 2)არსებულ car ობიექტს , ობიექტის გარედან დაამატეთ color  და price  , ასევე ამოშალეთ milage , შემდეგ ყველაფერი გამოსახეთ console-ში 

car.color = 'black'
car.price = 44000

delete car.mileage

console.log(car)