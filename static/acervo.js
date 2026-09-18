const manageToggle = document.querySelector('.manage-toggle');

if (manageToggle) {
    manageToggle.addEventListener('click', () => {
        const isManaging = document.body.classList.toggle('is-managing');
        manageToggle.setAttribute('aria-pressed', String(isManaging));
        manageToggle.textContent = isManaging ? 'Concluir gerenciamento' : 'Gerenciar acervo';
    });
}
