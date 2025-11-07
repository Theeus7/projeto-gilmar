const API_HISTORY_URL = "http://127.0.0.1:5000/api/books/history";
const container = document.getElementById("history-container");

function setupToggleListener() {
  container.addEventListener("click", (event) => {
    if (event.target.classList.contains("toggle-summary")) {
      const card = event.target.closest(".history-card");
      const summary = card.querySelector(".summary");
      summary.classList.toggle("expanded");
      card.classList.toggle("expanded");
      event.target.textContent = summary.classList.contains("expanded")
        ? "Recolher Resumo"
        : "Expandir Resumo";
    }
  });
}

async function loadHistory() {
  try {
    const response = await fetch(API_HISTORY_URL);
    const data = await response.json();
    if (!response.ok) throw new Error(data.error || "Erro ao carregar histórico");

    const livros = data.data;
    if (livros.length === 0) {
      container.innerHTML = "<p>Nenhum resumo encontrado.</p>";
      return;
    }

    container.innerHTML = livros
      .map(
        (item) => `
        <div class="history-card">
          <div class="card-header">
            <h3>${item.titulo}</h3>
            <span class="date">${new Date(item.criado_em).toLocaleString("pt-BR")}</span>
          </div>
          <p class="summary">${item.resumo}</p>
          <button class="toggle-summary">Expandir Resumo</button>
        </div>
      `
      )
      .join("");

    setupToggleListener();
  } catch (error) {
    container.classList.add("empty");
    container.innerHTML = "<p>Não foi possível carregar o histórico.</p>";
    console.error(error);
  }
}

window.addEventListener("DOMContentLoaded", loadHistory);
