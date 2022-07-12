let icons = document.querySelectorAll(".requirement");
Array.from(icons).forEach(element => {
    element.addEventListener("mouseenter",() => {
        let music = new Audio("mixkit-plastic-bubble.wav");
        music.volume = 0.3;
        music.play();
    })
});

Array.from(icons).forEach(element => {
    element.addEventListener("click",() => {
        element.classList.toggle("tog");
        let music = new Audio("mixkit-typewriter-soft-click.wav");
        music.volume = 0.3;
        music.play();
    })
});

// Array.from(icons).forEach(element => {
//     console.log(element);    
//     element.addEventListener("click",() => {
//         element.classList.toggle("add_color")
//     })
// });
