const uploadInput = document.getElementById("file-upload");
const submitButton = document.getElementById("submit-button");
const main = document.getElementById("main");
const loaderArea = document.getElementById("loader-area");
const resultArea = document.getElementById("result-area");
const resultText = document.getElementById("result-text");
const backButton = document.getElementById("back-button");

const API_URL = "http://127.0.0.1:5000/api/books/upload";

submitButton.addEventListener("click", async () => {
  const file = uploadInput.files[0];
  if (!file) {
    alert("Por favor, selecione um arquivo PDF antes de enviar.");
    return;
  }

  main.style.opacity = 0;
  loaderArea.style.opacity = 1;
  loaderArea.style.pointerEvents = "auto";

  const formData = new FormData();
  formData.append("file", file);

  try {
    const response = await fetch(API_URL, {
      method: "POST",
      body: formData,
    });

    const data = await response.json();

    loaderArea.style.opacity = 0;
    loaderArea.style.pointerEvents = "none";

    if (!response.ok) {
      throw new Error(data.error || "Erro ao processar o arquivo.");
    }

    resultText.textContent = data.summary;
    resultArea.style.display = "flex";
    main.style.opacity = 0;

  } catch (error) {
    loaderArea.style.opacity = 0;
    loaderArea.style.pointerEvents = "none";
    main.style.opacity = 1;
    alert(`Falha: ${error.message}`);
  }
});

backButton.addEventListener("click", () => {
  resultArea.style.display = "none";
  main.style.opacity = 1;
  uploadInput.value = "";
});