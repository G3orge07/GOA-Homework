//შექმენით სია შეიყვანეთ user-ების სახელი და გვარი თუ user-ების სახელი და გვრი იწყება პატარა ასოთი slice-მეთოდის გამოყენებით ამოშალეთ ასეთი სახელები და გვარები სიიდან

let names = ['Giorgi Tavadze', 'giorgi Khutsishvili', 'nika tavartqiladze', 'Aleqsandre dzukaevi', 'Mariam Mchedlishvili', 'goga asatiani', 'nikoloz Abuladze', 'tornike xozrevanidze', 'Ana Futuridze', 'giorgi Takhadze']

for (let name of names){
    if (name[0] == name[0].toLowerCase() && name[name.indexOf(' ')+1] == name[name.indexOf(' ')+1].toLowerCase()){
        names.splice(names.indexOf(name), 1)
    }
}

console.log(names)