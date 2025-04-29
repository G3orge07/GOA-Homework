// 2)შექმენი სია სადაც რენდომულად შეიყვან რამდენიმე სახელს და გვარს,
// შემდეგ დაწერე ფუნქცია რომელიც დააბუნებს ახალ სიას სადაც წარმოდგენილი იქნება თითოეული სახელი და გვარი ისე როგორც ინიციალები
// (Giorgi Bibilashvili => G.B)

let nameArr = ['Giorgi Tavadze', 'Keso Chichua', 'Saba Bokuchava', 'Goga Asatiani', 'Aleqsandre Dzukaevi', 'Giorgi Samsonadze']

function makeInitials(names) {
    let result = []
    for (let name of names){
        result.push(name.split(' ')[0][0] + '.' + name.split(' ')[1][0] + '.')
    }
    return result
}

console.log(makeInitials(nameArr))