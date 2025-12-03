const menuBtn = document.querySelector(".menu-btn");
const navDrawer = document.querySelector(".nav-drawer");
const backdrop = document.querySelector(".backdrop");

// 1. Select all links inside the drawer
const navLinks = document.querySelectorAll(".nav-drawer a");

function toggleMenu() {
  menuBtn.classList.toggle("open");
  navDrawer.classList.toggle("active");
  backdrop.classList.toggle("active");
  document.body.classList.toggle("no-scroll");
}

// 2. Click Button -> Toggle Menu
menuBtn.addEventListener("click", (e) => {
  e.stopPropagation();
  toggleMenu();
});

// 3. Click Backdrop -> Close Menu
backdrop.addEventListener("click", () => {
  toggleMenu();
});

// 4. Click Any Link inside Drawer -> Close Menu
navLinks.forEach((link) => {
  link.addEventListener("click", () => {
    // We only want to close it, so we simply call toggleMenu
    // provided the menu is currently open.
    if (navDrawer.classList.contains("active")) {
      toggleMenu();
    }
  });
});
