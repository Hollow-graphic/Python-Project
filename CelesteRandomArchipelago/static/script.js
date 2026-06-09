document.addEventListener("click", async (e) => {
  const btn = e.target.closest("button");

  if (!btn) return;

  if (btn.textContent.includes("Clear")) {
    await fetch("./api/clear", { method: "POST" });
  }
});