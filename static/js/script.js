document.getElementById("ai-form").addEventListener("submit", async (event) => {
  event.preventDefault();
  const formData = new FormData(event.target);
  const response = await fetch(event.target.action, {
    method: "POST",
    body: formData,
  });
  const data = await response.json();
  const resultDiv = document.getElementById("recommendation-result");
  resultDiv.innerHTML = `
        <h3>Recommended Project</h3>
        <p><strong>${data.project_name}</strong>: ${data.project_description}</p>
    `;
});
