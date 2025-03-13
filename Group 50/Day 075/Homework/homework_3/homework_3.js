// 3) შექმენით ობიექტი user , ამ ობიექტში შეინახე შესაბამისი key-ები , for in - ციკლის  გამოყენებით გადაუარე თითოეულ key-ს და გამოსახე console-ში

const user = {
    firstname : 'Giorgi', 
    lastName : 'Tavadze',
    age : 16,
    email : 'giorgi.tavadze0701@gmail.com'
}

for (let data of Object.keys(user)){
    console.log(data)
}