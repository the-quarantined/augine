let icons = document.querySelectorAll(".requirement");
console.log(Array.from(icons));
Array.from(icons).forEach(element => {
    element.addEventListener("mouseenter",() => {
        let music = new Audio("Assets/mixkit-plastic-bubble.wav");
        music.volume = 0.3;
        music.play();
    })
});


let txt = document.getElementById('text');
let item_1 = document.getElementById('item-1');
let item_2 = document.getElementById('item-2');
let item_3 = document.getElementById('item-3');
let item_4 = document.getElementById('item-4');
let item_5 = document.getElementById('item-5');
let item_6 = document.getElementById('item-6');
let item_7 = document.getElementById('item-7');
let item_8 = document.getElementById('item-8');
let item_9 = document.getElementById('item-9');
let item_10 = document.getElementById('item-10');
let item_11= document.getElementById('item-11');



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
        let music = new Audio("Assets/mixkit-typewriter-soft-click.wav");
        music.volume = 0.3;
        music.play();         
        txt.style.display = 'none';
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
        
        item_1.style.display= 'none';
        item_2.style.display= 'none';
        item_3.style.display= 'none';
        item_4.style.display= 'none';
        item_5.style.display= 'none';
        item_6.style.display= 'none';
        item_7.style.display= 'none';
        item_8.style.display= 'none';
        item_9.style.display= 'none';
        item_10.style.display= 'none';
        item_11.style.display= 'none';
        
        if(element.id=='shirt'){
            item_1.style.display= 'flex';
            // document.getElementsByClassName('things').style.overflow = 'scroll';
        }
        else if(element.id=='shorts'){
            item_2.style.display= 'flex';
        }
        else if(element.id=='trouser'){
            item_3.style.display= 'flex';
        }
        else if(element.id=='frock'){
            item_4.style.display= 'flex';
        }
        else if(element.id=='socks'){
            item_5.style.display= 'flex';
        }
        else if(element.id=='shoes'){
            item_6.style.display= 'flex';
        }
        else if(element.id=='heels'){
            item_7.style.display= 'flex';
        }
        else if(element.id=='sunglasses'){
            item_8.style.display= 'flex';
        }
        else if(element.id=='watch'){
            item_9.style.display= 'flex';
        }
        else if(element.id=='cap'){
            item_10.style.display= 'flex';
        }
        else if(element.id=='jewellary'){
            item_11.style.display= 'flex';
        }
    })  
});



let shirt_pics = document.querySelectorAll('#item-1 img');
let short_pics = document.querySelectorAll('#item-2 img');
let trouser_pics = document.querySelectorAll('#item-3 img');
let frock_pics = document.querySelectorAll('#item-4 img');
let socks_pics = document.querySelectorAll('#item-5 img');
let shoes_pics = document.querySelectorAll('#item-6 img');
let heels_pics = document.querySelectorAll('#item-7 img');
let sunglasses_pics = document.querySelectorAll('#item-8 img');
let watch_pics = document.querySelectorAll('#item-9 img');
let cap_pics = document.querySelectorAll('#item-10 img');
let jewellary_pics = document.querySelectorAll('#item-11 img');


// console.log(Array.from(shirt_pics));
let display = document.getElementById('display');

Array.from(shirt_pics).forEach(element => {
    element.addEventListener("click",() => {
        let at = element.getAttribute('src');
        console.log(at);
        display.style.backgroundImage = "url("+at+")";
        display.style.backgroundSize = 'cover';
    })  
});
Array.from(short_pics).forEach(element => {
    element.addEventListener("click",() => {
        let at = element.getAttribute('src');
        console.log(at);
        display.style.backgroundImage = "url("+at+")";
        display.style.backgroundSize = 'cover';
    })  
});
Array.from(trouser_pics).forEach(element => {
    element.addEventListener("click",() => {
        let at = element.getAttribute('src');
        console.log(at);
        display.style.backgroundImage = "url("+at+")";
        display.style.backgroundSize = 'cover';
    })  
});
Array.from(frock_pics).forEach(element => {
    element.addEventListener("click",() => {
        let at = element.getAttribute('src');
        console.log(at);
        display.style.backgroundImage = "url("+at+")";
        display.style.backgroundSize = 'cover';
    })  
});
Array.from(socks_pics).forEach(element => {
    element.addEventListener("click",() => {
        let at = element.getAttribute('src');
        console.log(at);
        display.style.backgroundImage = "url("+at+")";
        display.style.backgroundSize = 'cover';
    })  
});
Array.from(shoes_pics).forEach(element => {
    element.addEventListener("click",() => {
        let at = element.getAttribute('src');
        console.log(at);
        display.style.backgroundImage = "url("+at+")";
        display.style.backgroundSize = 'cover';
    })  
});
Array.from(heels_pics).forEach(element => {
    element.addEventListener("click",() => {
        let at = element.getAttribute('src');
        console.log(at);
        display.style.backgroundImage = "url("+at+")";
        display.style.backgroundSize = 'cover';
    })  
});
Array.from(sunglasses_pics).forEach(element => {
    element.addEventListener("click",() => {
        let at = element.getAttribute('src');
        console.log(at);
        display.style.backgroundImage = "url("+at+")";
        display.style.backgroundSize = 'cover';
    })  
});
Array.from(watch_pics).forEach(element => {
    element.addEventListener("click",() => {
        let at = element.getAttribute('src');
        console.log(at);
        display.style.backgroundImage = "url("+at+")";
        display.style.backgroundSize = 'cover';
    })  
});
Array.from(cap_pics).forEach(element => {
    element.addEventListener("click",() => {
        let at = element.getAttribute('src');
        console.log(at);
        display.style.backgroundImage = "url("+at+")";
        display.style.backgroundSize = 'cover';
    })  
});
Array.from(jewellary_pics).forEach(element => {
    element.addEventListener("click",() => {
        let at = element.getAttribute('src');
        console.log(at);
        display.style.backgroundImage = "url("+at+")";
        display.style.backgroundSize = 'cover';
        display.style.backgroundPosition = 'center';
    })  
});