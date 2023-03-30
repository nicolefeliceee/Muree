console.log("helo")

// FOTO LAGU

var images = ["static/images/1.jfif", "static/images/2.jfif", "static/images/3.jfif",
"static/images/4.jfif", "static/images/5.jpg", "static/images/6.jfif", "static/images/7.jfif",
"static/images/8.jfif", "static/images/9.jfif", "static/images/10.jfif", "static/images/11.jfif",
"static/images/12.jfif", "static/images/13.jfif", "static/images/14.jpg", "static/images/15.jfif",
"static/images/16.jfif", "static/images/17.jfif", "static/images/18.jfif", "static/images/19.jfif",
"static/images/20.jfif", "static/images/21.jfif", "static/images/22.jfif", "static/images/23.jfif",
"static/images/24.jfif", "static/images/25.jfif", "static/images/26.jfif", "static/images/27.jfif",
"static/images/28.jfif", "static/images/29.jfif", "static/images/30.jfif", "static/images/31.jfif",
"static/images/32.jfif", "static/images/33.jfif", "static/images/34.jfif", "static/images/35.jfif",
"static/images/36.jfif", "static/images/37.jfif", "static/images/38.jfif", "static/images/39.jfif",
"static/images/40.jfif", "static/images/41.jfif", "static/images/42.jfif", "static/images/43.jfif",
"static/images/44.jfif", "static/images/45.jfif", "static/images/46.jfif", "static/images/47.jfif",
"static/images/48.jfif", "static/images/49.jfif", "static/images/50.jfif", "static/images/51.jfif",
"static/images/52.jfif", "static/images/53.jfif", "static/images/54.jfif", "static/images/55.jfif",
"static/images/56.jfif", "static/images/57.jfif", "static/images/58.jfif", "static/images/59.jfif",
"static/images/60.jfif", "static/images/61.jfif", "static/images/62.jfif", "static/images/63.jfif",
"static/images/64.jfif", "static/images/65.jfif", "static/images/66.jfif", "static/images/67.jfif",
"static/images/68.jfif", "static/images/69.jfif", "static/images/70.jfif", "static/images/71.jfif",
"static/images/72.jfif", "static/images/73.jfif", "static/images/74.jfif", "static/images/75.jfif",
"static/images/76.jfif", "static/images/77.jfif", "static/images/78.jfif", "static/images/79.jfif",
"static/images/80.jfif", "static/images/81.jfif", "static/images/82.jfif", "static/images/83.jfif",
"static/images/84.jfif", "static/images/85.jfif", "static/images/86.jfif", "static/images/87.jfif",
"static/images/88.jfif", "static/images/89.jfif", "static/images/90.jfif", "static/images/91.jfif",
"static/images/92.jfif", "static/images/93.jfif", "static/images/94.jfif", "static/images/95.jfif",
"static/images/96.jfif", "static/images/97.jfif", "static/images/98.jfif", "static/images/99.jfif",
"static/images/100.jfif"]

counter = document.getElementById('counter').innerText

x = 1
while (x <= 100) {
    imgBtn = document.getElementById('btn_img'+x)
    songNum = document.getElementById('num'+x).innerText
    imgBtn.src = images[songNum - 1]

    box = document.getElementById('list'+x)
    if(x == counter) {
        box.style.backgroundColor = "rgb(116,116,116)"
    }
    
    if(x > counter) {
        box.style.filter = "brightness(30%)"
    }

    x += 1
}

// CURRENTLY PLAYING
curr_num = document.getElementById('curr_num').innerText
playing = sessionStorage.getItem('playing')
currsec = sessionStorage.getItem('currsec')
if (curr_num != sessionStorage.getItem('curr_num')) {
    currsec = 0
    playing = 0
}
sessionStorage.setItem('curr_num', curr_num)
curr_photo = document.getElementById('currphoto')
console.log(curr_num)
curr_photo.src = images[curr_num - 1]

// MEDIA BUTTON
const backwardBtn = document.getElementById('backward');
const playBtn = document.getElementById('play');
const pauseBtn = document.getElementById('pause');
const forwardBtn = document.getElementById('forward');

if (counter == 1) {
    backwardBtn.disabled = true
} else if (counter == 100){
    forwardBtn.disabled = true
}

time = 0

// if (curr_num != sessionStorage.getItem('curr_num')) {
//     currsec = 0
//     playing = 0
// }

console.log("playing " + playing)
console.log("currsec " + currsec)

audio = new Audio('static/songs/'+curr_num+'.mp3')

audio.currentTime = currsec

if(currsec > 0 && playing == 0) {
    playing = 1
} else if (currsec > 0 && playing == 1) {
    playing = 0
}

playPause()

function updatesec() {
    currsec = audio.currentTime
    sessionStorage.setItem("currsec", currsec)
    console.log(currsec)
    console.log(audio.duration)
    if(currsec > audio.duration - 0.5) {
        forwardBtn.click()
    }
}

playBtn.addEventListener('click', () => {
    playstatements()
})

function playstatements() {
    playPause()
}

pauseBtn.addEventListener('click', () => {
    pausestatements()
})

function pausestatements() {
    playPause()
}

backwardBtn.addEventListener('click', () => {
    console.log('backward')
    currsec = 0;
    sessionStorage.setItem("currsec", currsec)
})

// function bck() {
//     console.log('backward')
//     currsec = 0;
//     sessionStorage.setItem("currsec", currsec)
// }

forwardBtn.addEventListener('click', () => {
    console.log('forward')
    currsec = 0;
    sessionStorage.setItem("currsec", currsec)
    playBtn.click()
})

// function fwd() {
//     console.log('forward')
//     currsec = 0;
//     sessionStorage.setItem("currsec", currsec)
// }

function playPause() {
    if(playing == 1){
        console.log('pause')
        clearInterval(time)
        pausefunc()
    } else {
        console.log('play')
        time = setInterval(updatesec, 250)
        playfunc()
    }
}

function pausefunc() {
    audio.pause()
    playing = 0
    sessionStorage.setItem("playing", playing)
    playBtn.style.display = 'block'
    pauseBtn.style.display = 'none'

}

function playfunc() {
    audio.play()
    playing = 1
    sessionStorage.setItem("playing", playing)
    playBtn.style.display = 'none'
    pauseBtn.style.display = 'block'
}

document.body.onkeyup = function(e) {
    if (e.key == " " ||
        e.code == "Space" ||      
        e.keyCode == 32      
    ) {
      playPause()
    }
  }

