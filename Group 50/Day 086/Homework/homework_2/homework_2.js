// 2) 2)შექმენით ცვლადი სადაც მომხმარებელი შემოიყვანს საათს, 
// თქვენი დავალებაა გაიგოთ ეს საათი რომელ დღის მონაკვეთს ეკუთვნის(დილა,შუადღე,საღამო,ღამე)

let time = prompt('რომელი საათია? (0:00 - 23:59)')

let hours = Number(time.split(':')[0])

switch(hours){
    case 6:
    case 7:
    case 8:
    case 9:
    case 10:
    case 11:
        console.log('ახლა დილაა')
        break
    
    case 12:
    case 13:
    case 14:
        console.log('ახლა შუადღეა')
        break

    case 15:
    case 16:
    case 17:
    case 18:
    case 19:
    case 20:
        console.log('ახლა საღამოა')
        break
    
    case 21:
    case 22:
    case 23:
    case 0:
    case 1:
    case 2:
    case 3:
    case 4:
    case 5:
        console.log('ახლა ღამეა')
        break
    
    default:
        console.log('Invalid Input')
}
