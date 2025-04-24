// 1) ნასწავლი მასალის დახმარებით გააკეთეთ სურათების სლაიდერი , დაუმატეთ რაიმე კარგი დიზაინი თქვენი წარმოსახვით

sources = [
    'images/java.svg',
    'images/python.webp',
    'images/cplusplus.png',
    'images/javascript.png',
    'images/html.jpg',
    'images/php.png',
    'images/matlab.png',
    'images/go.webp',
    'images/ruby.png',
    'images/visual_basic.png',
]


count = 0

images = document.getElementsByClassName('image')

images[0].src = sources[0]
images[1].src = sources[1]
images[2].src = sources[2]
images[3].src = sources[3]

arrowR = document.getElementById('arrowR')
arrowL = document.getElementById('arrowL')

arrowR.onclick = function() {
    if (count < 6) {
        count+=1
        for (let i = 0; i < 4; i++){
            images[i].src = sources[count+i]
        }
    }
}

arrowL.onclick = function() {
    if (count > 0) {
        count-=1
        for (let i = 0; i < 4; i++){
            images[i].src = sources[count+i]
        }
    }
}