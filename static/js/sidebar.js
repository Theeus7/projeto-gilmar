document.addEventListener("DOMContentLoaded", () => {
  const mainBtn = document.getElementById("main-button");
  const historyBtn = document.getElementById("history-button");
  const aboutBtn = document.getElementById("about-button");

  const path = window.location.pathname;
  if (path.includes("history")) {
    historyBtn.classList.add("active");
  } else {
    mainBtn.classList.add("active");
  }

  if (mainBtn) {
    mainBtn.addEventListener("click", () => {
      window.location.href = "/";
    });
  }

  if (historyBtn) {
    historyBtn.addEventListener("click", () => {
      window.location.href = "/history";
    });
  }

  if (aboutBtn) {
    aboutBtn.addEventListener("click", () => {
      window.open("https://github.com/Theeus7/projeto-gilmar", "_blank");
    });
  }
});

document.addEventListener("DOMContentLoaded", () => {
  const sidebar = document.querySelector(".sidebar");
  const toggleBtn = document.getElementById("sidebar-toggle");

  toggleBtn.addEventListener("click", () => {
    sidebar.classList.toggle("sidebar--collapsed");
  });
});
