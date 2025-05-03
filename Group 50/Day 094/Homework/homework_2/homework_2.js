// 2)შექმენი სია სადაც რენდომულად შეიყვან რამდენიმე სახელს და გვარს,
// შემდეგ დაწერე ფუნქცია რომელიც დააბუნებს ახალ სიას სადაც წარმოდგენილი იქნება თითოეული სახელი და გვარი ისე როგორც ინიციალები
// (Giorgi Bibilashvili => G.B)

let nameArr = ['Giorgi Tavadze', 'Keso Chichua', 'Saba Bokuchava', 'Goga Asatiani', 'Aleqsandre Dzukaevi', 'Giorgi Samsonadze']

const makeInitials = (name) => name.split(' ')[0][0] + '.' + name.split(' ')[1][0] + '.'

console.log(nameArr.map(makeInitials))