// მომხმარებელს შემოატანინეთ თვის სახელი მაგ:("იანვარი" , "თებერვალი") , თქვენი მიზანია დაადგინოთ მომხმარებლის შემოტანილი თვე სეზონის რომელი პერიოდია (ზაფხული,ზამთარი,შემოდგომა,თუ გაზაფხული)

let month = prompt('What month were you born in? (January - December) : ')

switch(month){
    case 'December':
    case 'January':
    case 'February':
        console.log('Winter')
        break

    case 'March':
    case 'April':
    case 'May':
        console.log('Spring')
        break

    case 'June':
    case 'July':
    case 'August':
        console.log('Summer')
        break

    case 'September':
    case 'October':
    case 'November':
        console.log('Fall')
        break

    default:
        console.log('Invalid Input')
}