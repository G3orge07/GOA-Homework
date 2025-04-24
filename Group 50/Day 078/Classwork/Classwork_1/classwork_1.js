// 1)შექმენით დოკუმენტში რამდენიმე ერთნაირი ელემენტი და querySelector()ის და  querySelectorAll() ის გამოყენებით javascript-იდან შეუცვალეთ სტილები

let title = document.querySelector('h1')

let list = document.querySelector('ul')

let ul_item = document.querySelectorAll('li')

let par = document.querySelector('p')


title.style.color = 'blue'
title.style.fontWeight = '900'


list.style.listStyleType = 'decimal'


ul_item[0].style.textDecoration = 'overline'
ul_item[1].style.textDecoration = 'line-through'
ul_item[2].style.textDecoration = 'underline'

par.style.color = 'brown'
par.style.fontSize = '25px'