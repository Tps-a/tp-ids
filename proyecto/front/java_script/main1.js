document.addEventListener('mousemove', (event) => {
    let distancia_borde;
    if(sidebar.classList.contains('hidden')){
        distancia_borde = 200;
    }else{
        distancia_borde = 340;
    }
    if (event.clientX > window.innerWidth - distancia_borde) {
        sidebar.classList.remove('hidden');
        sidebar.classList.add('show');
       
        document.getElementById('sidebarIndicator').style.display = 'none';
    } else {
        sidebar.classList.remove('show');
        sidebar.classList.add('hidden');
       
        document.getElementById('sidebarIndicator').style.display = 'block';
    }
});