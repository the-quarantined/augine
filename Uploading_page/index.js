let access = document.querySelector('.choose-image');
let visible= document.querySelector('.option');
access.addEventListener('click',()=>{
    let music = new Audio("../Assets/mixkit-typewriter-soft-click.wav");
    music.volume = 0.3;
    music.play();
    visible.style.visibility = 'visible'; 
})

const img_input = document.querySelector('#acc');
let dis = document.querySelector('#dis_in');
var uploaded_image= "";

img_input.addEventListener("change",function(){
    const reader = new FileReader();
    let x=1;
    reader.addEventListener("load",()=>{
        uploaded_image= reader.result;
        document.querySelector("#display").style.backgroundImage = `url(${uploaded_image})`;
        dis.style.visibility='hidden';
        sessionStorage.setItem("recent-image",uploaded_image);
    })
    reader.readAsDataURL(this.files[0]);
    // document.querySelector('.pw img').style.visibility = 'visible';
})
document.addEventListener("DOMContentLoaded", () => {
    const recentImageDataUrl = sessionStorage.getItem("recent-image");
    // console.log(recentImageDataUrl);
    if (recentImageDataUrl){
        document.querySelector("#preview").setAttribute("src", recentImageDataUrl);
    }
});

let cam = document.querySelector('#camera');
let snaper = document.querySelector('#snap');
let video = document.querySelector('#display');
let snapshot = document.getElementById('results')
let extract = document.querySelector('#val');

cam.addEventListener('click',function(){
    access.style.visibility = 'hidden';
    visible.style.visibility = 'hidden';
    snaper.style.visibility = 'visible';
    Webcam.set({
        width: 700,
        height: 350,
        image_format:'jpeg/png',
        jpeg_quality:90
    })
    Webcam.attach('#display');
})
function take_snapshot() {
    Webcam.snap( function(data_uri) {
        snapshot.innerHTML = '<img src="'+data_uri+'"/>';
        sessionStorage.setItem("snap-photo",snapshot.innerHTML);
        extract.setAttribute('value',snapshot.innerHTML);
        console.log(extract);
    });
}