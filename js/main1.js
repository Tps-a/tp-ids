const sidebar = document.getElementById('sidebar');

document.addEventListener('mousemove', (event) => {
    if (event.clientX > window.innerWidth - 200) {
        sidebar.classList.remove('hidden');
        sidebar.classList.add('show');
    } else {
        sidebar.classList.remove('show');
        sidebar.classList.add('hidden');
    }
});
