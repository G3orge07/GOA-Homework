// 1)შექმენით ცვლადი word - გადაეცით თქვენთვის სასურველი სიტყვა, შემდეგ მომხმარებელს შემოატანინეთ სასუველი ენა
// (მაგ:ქართული,ინგლისური,ფრანგული) და switch-კონსტრუქტორის გამოყენებით გააკეთეთ მარტივი translate როდესაც მომხმარებელი შემოიყვანს 
// მაგალითად "ფრანგულს" თქვენი სიტყვა კონსოლში გადაითარგმნოს "ფრანგულად", ხოლო თუ მომხმარებელი შემოიტანს სხვა სიტყვას მაგ შემთხვევაში 
// კონსოლში გამოიტანოს რომ ასეთი ენა არ არსებობს და ახლიდან სთხოვოს შეყვენა

let word  = 'მაგიდა'

let language = prompt('Enter a language to translate the word "მაგიდა":\n(English, French, Spanish, Greek, German, Chinese, Japanese)')

switch(language){
    case 'English':
        console.log('Table')
        break

    case 'French':
        console.log('Tableau')
        break
    
    case 'Spanish':
        console.log('Mesa')
        break

    case 'Greek':
        console.log('Τραπέζι (Trapézi)')
        break
    
    case 'German':
        console.log('Tisch')
        break

    case 'Chinese':
        console.log('桌子 (Zhuōzǐ)')
        break

    case 'Japanese':
        console.log('テーブル (Tēburu)')
        break
    
    default:
        console.log('Invalid Input')
}