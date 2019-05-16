// Select DOM items
const menuBtn = document.querySelector('.menu-btn');
const menu = document.querySelector('.sidebar');
const menuBranding = document.querySelector('.sidebar-branding');
const menuNav = document.querySelector('.sidebar-nav');
const navItems = document.querySelectorAll('.sidebar-nav-item');
const navText = document.querySelectorAll('.sidebar-text');

// Set initial state of menu
let showMenu = false;

menuBtn.addEventListener('click', toggleMenu);

function toggleMenu() {
  if(!showMenu) {
    menuBtn.classList.add('close');
    menu.classList.add('show');
    menuBranding.classList.add('show');
    menuNav.classList.add('show');
    navItems.forEach(item => item.classList.add('show'));
    navText.forEach(item => item.classList.add('show'));

    // Set menu state
    showMenu = true;
  } else {
    menuBtn.classList.remove('close');
    menu.classList.remove('show');
    menuBranding.classList.remove('show');
    menuNav.classList.remove('show');
    navText.forEach(item => item.classList.remove('show'));

    // Set menu state
    showMenu = false;
  }
}
