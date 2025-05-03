// 3)შექმენით ფუნქცია რომელიც სიიდან ამოიღებს ყველა ელემენტს და დააბრუნებს ახალ სიას სადაც მხოლოდ 5 სიმბოლოზე მეტი სიტყვები მოხვდებიან

let stringArr = ['db3ivryftcer', 'eycg', '2jk', 'gdi3bq7f6q3fn3iq7', 'ecbkgvjyejwhrvnhewrvcmhesg', 'kufe56vt', 'weud', '2ufd62u2', 'a', 'ks']

const moreThanFive = string => string > 5

console.log(stringArr.filter(moreThanFive))