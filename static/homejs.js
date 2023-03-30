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

x = 1
while (x <= 100) {
    imgBtn = document.getElementById('btn_img'+x)
    songNum = document.getElementById('num'+x).innerText
    imgBtn.src = images[songNum - 1]
    x += 1
}

// CURRENTLY PLAYING

const singertxt = document.getElementById('judulPlaylist').textContent
const divplaying = document.getElementById('playing')

if(singertxt === "Nothing") {
    divplaying.style.visibility='hidden'
} else {
    divplaying.style.visibility='visible'
}

curr_num = document.getElementById('curr_num').innerText
curr_photo = document.getElementById('currphoto')
console.log(curr_num)
curr_photo.src = images[curr_num - 1]
divplaying.style.backgroundImage = "url("+images[curr_num - 1]+")"
divplaying.style.backgroundSize = "300px 300px"

// song second

playing = 0
currsec = 0
if (sessionStorage.getItem('playing') == null) {
    sessionStorage.setItem("playing", playing)
    sessionStorage.setItem("currsec", currsec)
} else if (sessionStorage.getItem('playing') == 0) {
    console.log(sessionStorage.getItem('playing'))
    console.log(sessionStorage.getItem('currsec'))
} else {
    audio = new Audio('static/songs/'+curr_num+'.mp3')
    playing = sessionStorage.getItem('playing')
    currsec = sessionStorage.getItem('currsec')
    audio.currentTime = currsec
}

console.log("playing " + playing)
console.log("currsec " + currsec)

playfunc()

time = setInterval(updatesec, 250)

function updatesec() {
    currsec = audio.currentTime
    sessionStorage.setItem("currsec", currsec)
    console.log(currsec)
}

// function playPause() {
//     if(playing == true){
//         playfunc()
//     } else {
//         pausefunc()
//     }
// }

// function pausefunc() {
//     audio.pause()
//     playing = false
//     sessionStorage.setItem("playing", playing)
//     clearInterval(time)
// }

function playfunc() {
    audio.play()
    playing = 1
    sessionStorage.setItem("playing", playing)
}