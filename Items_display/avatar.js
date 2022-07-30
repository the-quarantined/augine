let icons = document.querySelectorAll(".requirement");
console.log(Array.from(icons));
Array.from(icons).forEach(element => {
    element.addEventListener("mouseenter",() => {
        let music = new Audio("../Assets/mixkit-plastic-bubble.wav");
        music.volume = 0.3;
        music.play();
    })
});

let shirt = document.getElementById('shirt');
let shorts = document.getElementById('shorts');
let trouser = document.getElementById('trouser');
let frock = document.getElementById('frock');
let socks = document.getElementById('socks');
let shoes = document.getElementById('shoes');
let heels = document.getElementById('heels');
let sunglasses = document.getElementById('sunglasses');
let watch = document.getElementById('watch');
let cap = document.getElementById('cap');
let jewelry = document.getElementById('jewelry');

let products = document.querySelectorAll(".interior svg");
console.log(Array.from(products));

Array.from(products).forEach(element => {
    element.addEventListener("click",() => {
        
        shirt.classList.remove("add_color");
        shorts.classList.remove("add_color");
        trouser.classList.remove("add_color");
        frock.classList.remove("add_color");
        socks.classList.remove("add_color");
        shoes.classList.remove("add_color");
        heels.classList.remove("add_color");
        sunglasses.classList.remove("add_color");
        watch.classList.remove("add_color");
        cap.classList.remove("add_color");
        jewelry.classList.remove("add_color");
        element.classList.add("add_color");  
        let music = new Audio("../Assets/mixkit-typewriter-soft-click.wav");
        music.volume = 0.3;
        music.play();         
    })  
});
