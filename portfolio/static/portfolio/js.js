let button = document.querySelector('.toggle')
let menu = document.querySelector('.navmenu')

button.addEventListener('click', () => {
    if (menu.style.display == 'flex') {
        menu.style.display = 'none'
    }
    else {
        menu.style.display = 'flex'
    }
})


let page = window.location.href
let splitpage = page.split('/')
let currpage = splitpage[3]
if (currpage == '') {
    let img = document.querySelector('#homebutton')
    let activeimg = img.src.replace('.png', 'active.png')
    img.src = activeimg
} else if (currpage == 'blog') {
    let img = document.querySelector('#blogbutton')
    let activeimg = img.src.replace('.png', 'active.png')
    img.src = activeimg
} else if (currpage == 'gallery') {
    let img = document.querySelector('#gallerybutton')
    let activeimg = img.src.replace('.png', 'active.png')
    img.src = activeimg
} else if (currpage == 'about') {
    let img = document.querySelector('#aboutbutton')
    let activeimg = img.src.replace('.png', 'active.png')
    img.src = activeimg
} else if (currpage == 'contact') {
    let img = ocument.querySelector('#contactbutton')
    let activeimg = img.src.replace('.png', 'active.png')
    img.src = activeimg
} else if (currpage == 'shop') {
    let img = document.querySelector('#shopbutton')
    let activeimg = img.src.replace('.png', 'active.png')
    img.src = activeimg
}



function lightboxshow(link, alt) {
    let lightbox = document.querySelector("#lightbox")
    lightbox.classList.remove("hide")
    let close = document.querySelector("#lightboxcloselink")

    let imgbox = document.querySelector("#imgdisplay")
    let img = document.createElement("img")
    img.src = link
    img.alt = alt
    img.id = "displayedimage"


    imgbox.appendChild(img)


    close.onclick = function () { closebox() }
    lightbox.onclick = function () { closebox() }
}

function closebox() {

    lightbox.classList.add("hide")
}
