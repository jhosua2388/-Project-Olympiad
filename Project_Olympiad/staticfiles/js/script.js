/* Menu Experiencia */
const menu1 = document.getElementById('menu-back-1');
const menuA = document.getElementById('sub-menu-back-1');
menu1.addEventListener('click', function () {
    menuA.classList.toggle('active2');
    menuB.classList.remove('active2');
    menuC.classList.remove('active2');
});
const menu2 = document.getElementById('menu-back-2');
const menuB = document.getElementById('sub-menu-back-2');
menu2.addEventListener('click', function () {
    menuB.classList.toggle('active2');
    menuA.classList.remove('active2');
    menuC.classList.remove('active2');
});
const menu3 = document.getElementById('menu-back-3');
const menuC = document.getElementById('sub-menu-back-3');
menu3.addEventListener('click', function () {
    menuC.classList.toggle('active2');
    menuA.classList.remove('active2');
    menuB.classList.remove('active2');
});