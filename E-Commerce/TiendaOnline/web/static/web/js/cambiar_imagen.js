let imgp = document.getElementById('imgp')
let img1 = document.getElementById('img1')
let img2 = document.getElementById('img2')
let img3 = document.getElementById('img3')
let img4 = document.getElementById('img4')

const cambiar1 = function(){
    imgp.src = img1.src
}
const cambiar2 = function(){
    imgp.src = img2.src
}
const cambiar3 = function(){
    imgp.src = img3.src
}
const cambiar4 = function(){
    imgp.src = img4.src
}

img1.addEventListener('click', cambiar1)
img2.addEventListener('click', cambiar2)
img3.addEventListener('click', cambiar3)
img4.addEventListener('click', cambiar4)