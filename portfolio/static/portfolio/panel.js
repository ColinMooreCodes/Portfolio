var newPost = document.querySelector('#newposts')
var manage = document.querySelector('#managedrop')

newPost.addEventListener('mouseover', () => {
    newPost.querySelector('#newpost').classList.remove('hide')
})
newPost.addEventListener('mouseout', () => {
    newPost.querySelector('#newpost').classList.add('hide')
})

manage.addEventListener('mouseover', () => {
    manage.querySelector('#manage').classList.remove('hide')
})
manage.addEventListener('mouseout', () => {
    manage.querySelector('#manage').classList.add('hide')
})


document.addEventListener('DOMContentLoaded', function (event) {
    var smallimgs = document.querySelectorAll('.manageimgwrap')

    for (let i = 0; i < smallimgs.length; i++) {
        let height = window.innerHeight;
        let imgbox = smallimgs[i]
        let img = imgbox.querySelector('.manageimg')
        let imghover = imgbox.querySelector('.imghover')
        let imgarrow = imgbox.querySelector('.imghoverarrow')

        img.addEventListener('mouseover', () => {
            imghover.classList.remove('hide')
            imgarrow.classList.remove('hide')
            let boxrect = imghover.getBoundingClientRect()
            let boxtop = boxrect.height / 2 * -1
            imghover.style.top = boxtop + 'px'

            let newboxrect = imghover.getBoundingClientRect()

            if (newboxrect.top < 0) {
                let diff = (i + 1) * -50
                imghover.style.top = diff + 'px'
            }

            if (boxrect.bottom > height) {
                let diff = height - boxrect.bottom
                imghover.style.top = boxtop + (diff / 2) + 'px'
                let checkrect = imghover.getBoundingClientRect()
                if (checkrect.bottom > height) {
                    imghover.style.top = boxtop + diff + 'px'
                }
            }

        })

        img.addEventListener('mouseout', () => {
            imghover.style.top = 0
            imghover.classList.add('hide')
            imgarrow.classList.add('hide')
        })
    }


})


function closebox() {


    let img = document.querySelector("#imgdisplay").children
    img[2].remove()
    img[1].remove()

    lightbox.classList.add("hide")
}