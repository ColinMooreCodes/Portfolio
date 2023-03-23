var newPost = document.querySelector('#newposts')
var manage = document.querySelector('#managedrop')

newPost.addEventListener('mouseover', () => {
    newPost.querySelector('#newpost').classList.remove('hidden')
})
newPost.addEventListener('mouseout', () => {
    newPost.querySelector('#newpost').classList.add('hidden')
})

manage.addEventListener('mouseover', () => {
    manage.querySelector('#manage').classList.remove('hidden')
})
manage.addEventListener('mouseout', () => {
    manage.querySelector('#manage').classList.add('hidden')
})


document.addEventListener('DOMContentLoaded', function () {
    var smallimgs = document.querySelectorAll('.manageimg')
    // console.log(smallimgs)
    for (let i = 0; i < smallimgs.length; i++) {
        smallimgs[i].addEventListener('mouseover', () => {
            // TODO: add hover of larger image to right
        })
    }
})


function closebox() {


    let img = document.querySelector("#imgdisplay").children
    img[2].remove()
    img[1].remove()

    lightbox.classList.add("hide")
}