const body = document.body;
const themeToggle = document.getElementById("theme-toggle");
const themeLabel = document.querySelector(".theme-switch__info label");

function updateIcons(isDark) {
  const icons = document.querySelectorAll("[data-icon-dark][data-icon-light]");
  icons.forEach(icon => {
    icon.src = isDark ? icon.dataset.iconDark : icon.dataset.iconLight;
  });
}

function setTheme(isDark) {
  if (isDark) {
    body.classList.add("theme--dark");
    themeToggle.classList.add("active");
    themeLabel.textContent = "Modo Escuro";
    localStorage.setItem("theme", "dark");
  } else {
    body.classList.remove("theme--dark");
    themeToggle.classList.remove("active");
    themeLabel.textContent = "Modo Claro";
    localStorage.setItem("theme", "light");
  }

  updateIcons(isDark);
}

themeToggle.addEventListener("click", () => {
  const isDark = !body.classList.contains("theme--dark");
  setTheme(isDark);
});

window.addEventListener("DOMContentLoaded", () => {
  const savedTheme = localStorage.getItem("theme");
  if (savedTheme === "dark") {
    setTheme(true);
  } else if (savedTheme === "light") {
    setTheme(false);
  } else {
    const prefersDark = window.matchMedia("(prefers-color-scheme: dark)").matches;
    setTheme(prefersDark);
  }
});