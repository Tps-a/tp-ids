function login(event) {
    event.preventDefault()
    let usuario_nuevo = document.getElementById("usuario").value;
    let password_nuevo = document.getElementById("password").value;
    fetch("http://localhost:5000/loguearse", 
        {method: "POST" , 
        headers: {'Content-Type': 'application/json'},
        body: JSON.stringify( {
            usuario: usuario_nuevo,
            password: password_nuevo,
            } )
        } )

        .then(response => response.json())
        .then(data => {
            console.log("respuesta: ",data.mensaje);
        })
}