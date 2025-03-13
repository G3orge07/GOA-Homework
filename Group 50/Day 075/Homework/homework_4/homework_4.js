// 4)შექმენი ობიექტი სახელად student რომელსაც ექნება fullName , scores(scores-უნდა იყოს სია რადგან შეინახოთ რამდენიმე მნიშვნელობა) , ასევე ექნება ორი ფუნქცია

const student = {
    fullName : 'Giorgi Tavadze',
    scores: [68, 94, 86],

    //1)averageScore()- რომელიც გამოითცლის საშუალო ქულას
    averageScore() {
        sum = 0
        for (let num of this.scores){
            sum += num
        }
        return Math.round(sum / this.scores.length)
    },

    // 2)checkStudent() - რომელიც გამოითლის მოსწავლის დონეს ქულების მიხედვით , 
    //   თუ საშუალო ქულა იქნება 90-ზე მეტი გამოსახეთ კონსოლში შემდეგი ტექსტი ("საუკეთესო სტუდენტი"),
    //   თუ საშუალო ქულა იქნება 90 ზე დაბალი და 60 ზე მაღალი გამოსახეთ "კარგი მოსწავლე", 
    //   ხოლო თუ საშუალო ქულა იქნება 60 ზე დაბალი გამოსახეთ "ნორმალური მოსწალე"
    checkStudent() {
        if (this.averageScore() >= 90){
            return "საუკეთესო სტუდენტი"
        }
        else if (this.averageScore() > 60 && this.averageScore() < 90){
            return "კარგი მოსწავლე"
        }
        else if (this.averageScore() < 60){
            return "ნორმალური მოსწალე"
        }
    }
}


console.log(student.averageScore())
console.log(student.checkStudent())