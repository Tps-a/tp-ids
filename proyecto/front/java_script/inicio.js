function register(event) {
    event.preventDefault();
    let usuario_nuevo = document.getElementById("usuario").value
    let password_nuevo = document.getElementById("password").value
    
    fetch(window.location.href + "/registrarse", 
        {
            method: "POST",
            headers: {'Content-Type': 'application/json'},
            body: JSON.stringify({
                usuario: usuario_nuevo,
                password: password_nuevo
            })
        }
    )
    .then(response => {
        if (!response.ok) {
            return response.json().then(data => {
                alert(data.error);
                throw new Error(data.error);
            });
        }
        return response.json()
    })
    .then(data => {
        alert(data.mensaje);
        window.location.href = '/login_page'
    })
}

function login(event) {
    event.preventDefault()
    let usuario = document.getElementById("usuario").value
    let password = document.getElementById("password").value

    fetch(window.location.href + "/login", 
        {
            method: "POST",
            headers: {'Content-Type': 'application/json'},
            body: JSON.stringify({
                usuario: usuario,
                password: password
            })
        }
    )
    .then(response => {
        if (!response.ok) {
            return response.json().then(data => {
                alert(data.error)
                throw new Error(data.error)
            });
        }
        return response.json()
    })
    .then(data => {
        window.location.href = `/${data.usuario_id}`
    })
    .catch(error => {
        console.error('Error:', error)
    })
}