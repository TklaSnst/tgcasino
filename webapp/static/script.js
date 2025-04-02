const set_degree = () => {
    var wheel = document.getElementById("wheel");
    angle =(360 / 37) / 2 + 6 * (360 / 37);
    wheel.style.transform = 'rotate(' + String(angle) + 'deg)';
}