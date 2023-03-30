const backwardBtn = document.getElementById('backward');
const playBtn = document.getElementById('play');
const pauseBtn = document.getElementById('pause');
const forwardBtn = document.getElementById('forward');
const mediaBtn = document.getElementById('mediaaction');
const curr_counter = document.getElementById('curr_counter');
let loop_idx = document.getElementById('loop_idx')
let txt_curr = document.getElementById('curr_playing')
// var counter = 1

// console.log(playBtn)
// console.log(pauseBtn)

pauseBtn.style.display = 'none'
mediaBtn.textContent = "playing"
curr_counter.textContent = counter
checkcurr()

playBtn.addEventListener('click', () => {
    console.log('play')
    mediaBtn.textContent = "playing"
    playPause()
    // playBtn.value = counter
})

pauseBtn.addEventListener('click', () => {
    console.log('pause')
    mediaBtn.textContent = "paused"
    playPause()
    // pauseBtn.value = counter
})

backwardBtn.addEventListener('click', () => {
    console.log('backward')
    // counter--
    // curr_counter.textContent = counter
    mediaBtn.textContent = "backward"
    // checkcurr()
    // backwardBtn.value = counter
})

forwardBtn.addEventListener('click', () => {
    console.log('forward')
    // counter++
    // curr_counter.textContent = counter
    mediaBtn.textContent = "forward"
    // checkcurr()
    // forwardBtn.value = counter
})

function checkcurr() {
    if(counter === 1) {
        backwardBtn.disabled = true
    } else if (counter === 100) {
        forwardBtn.disabled = true
    }else {
        backwardBtn.disabled = false
        forwardBtn.disabled = false
    }
    playBtn.style.display = 'none'
    pauseBtn.style.display = 'block'
    // checknum()
}

function checknum() {
    if(loop_idx === counter) {
        txt_curr.textContent = "currently playing"
    } else {
        txt_curr.textContent = ""
    }
}


function playPause() {
    if(playBtn.style.display === 'none'){
        playBtn.style.display = 'block'
        pauseBtn.style.display = 'none'
    } else {
        playBtn.style.display = 'none'
        pauseBtn.style.display = 'block'
    }
}