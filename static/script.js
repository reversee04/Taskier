function toggleForm() {
    const loginForm = document.getElementById("login-form");
    const signupForm = document.getElementById("signup-form");

    loginForm.classList.toggle("active-form");
    signupForm.classList.toggle("active-form");
}

document.addEventListener('DOMContentLoaded', function () {
    const menuBtn = document.getElementById('menu-btn');
    const navbar = document.getElementById('navbar');

    menuBtn.addEventListener('click', function () {
        navbar.classList.toggle('show');

        const isMenuVisible = navbar.classList.contains('show');
        menuBtn.innerHTML = isMenuVisible ? '<span class="material-icons-outlined">clear</span>' : '<span class="material-icons-outlined">menu</span>';
    });
});

  