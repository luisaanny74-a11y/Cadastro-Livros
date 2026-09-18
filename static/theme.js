const themeToggle = document.querySelector('.theme-toggle');

function updateThemeControl() {
    const darkThemeEnabled = document.documentElement.dataset.tema === 'escuro';
    themeToggle.setAttribute('aria-pressed', String(darkThemeEnabled));
    themeToggle.setAttribute('aria-label', darkThemeEnabled ? 'Ativar tema claro' : 'Ativar tema escuro');
}

themeToggle.addEventListener('click', () => {
    const nextTheme = document.documentElement.dataset.tema === 'escuro' ? 'claro' : 'escuro';
    if (nextTheme === 'escuro') document.documentElement.dataset.tema = nextTheme;
    else delete document.documentElement.dataset.tema;
    localStorage.setItem('tema', nextTheme);
    updateThemeControl();
});

updateThemeControl();
