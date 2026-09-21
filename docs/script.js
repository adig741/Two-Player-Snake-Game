const modeButtons = document.querySelectorAll('.mode-card[data-mode]');
const previewMode = document.getElementById('preview-mode');

modeButtons.forEach((button) => {
  button.addEventListener('click', () => {
    const mode = button.dataset.mode;
    document.documentElement.dataset.mode = mode;
    previewMode.textContent = `${mode.toUpperCase()} MODE`;
    modeButtons.forEach((item) => {
      const selected = item === button;
      item.classList.toggle('selected', selected);
      item.setAttribute('aria-pressed', String(selected));
    });
    document.getElementById('experience').scrollIntoView({ behavior: window.matchMedia('(prefers-reduced-motion: reduce)').matches ? 'instant' : 'smooth' });
  });
});
