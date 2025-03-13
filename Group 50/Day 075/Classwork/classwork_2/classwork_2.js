// 1) Prompით მომხმარებელს შემოატანინეთ მისი სახელი, გვარი, ასაკი და ჰობი, შემდეგ ეს ინფორმაცია შეინახეთ ობიექტში, ასევე ამ ობიექტს დაუმატეთ ფუნქცია, რომლის გამოძახებაზეც კონსოლში გამოიტანს "Welcome {name}"
// 2) შექმნილი ობიექტებიდან გამოიტანეთ მხოლოდ Keyები შემდეგ კი მხოლოდ Valueები
// 3) შექმნილ ობიექტს გადაუარეთ for ციკლით და გამოიტანეთ key და value შემდეგი ფორმატით: "{key} is {value}"

const userInfo = {
    firstName : prompt('Enter your name: '),
    lastName : prompt('Enter your last name: '),
    age: prompt("How old are you?"),
    hobby : prompt("What's your hobby?"),

    Welcome() {  //--- 1 ---
        return 'Welcome ' + this.firstName + ' ' + this.lastName + '!'
    }
}

console.log(userInfo.Welcome())


for (let key of Object.keys(userInfo)){    //--- 2 ---
    console.log(key)
}

for (let value of Object.values(userInfo)){    //--- 2 ---
    console.log(value)
}


for (let key of Object.keys(userInfo)){    //--- 3 ---
    console.log(key + ' is ' + userInfo.key)
}