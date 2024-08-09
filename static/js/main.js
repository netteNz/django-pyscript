// script.js
window.addEventListener('scroll', function() {
    const navbar = document.querySelector('.navbar');
    if (window.scrollY > 50) {
        navbar.style.backgroundColor = 'rgba(255, 255, 255, 0.9)';
    } else {
        navbar.style.backgroundColor = 'rgba(255, 255, 255, 0.8)';
    }
});
