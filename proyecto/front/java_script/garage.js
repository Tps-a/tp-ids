let scene, camera, renderer, carModel, controls;
let modelPaths = [
    '../modelos/low_poly_small_car/scene.gltf',
    '../modelos/lowpoly_car_pack/scene.gltf',
    '../modelos/generic_lowpoly_sedan/scene.gltf'
];

let currentModelIndex = 0;
let autos_usuario;
let cantidad_autos;
let auto;

fetch(window.location.href + "/autos")
    .then(response => {
        if (!response.ok) {
            console.log("Error de respuesta");
        }
        return response.json();
    })
    .then(data => {
        if(data.error){
            alert(data.error)
        }else{
            autos_usuario = data;
            cantidad_autos = data.length;
            auto = autos_usuario[0];
            init();
        }
    });

function init() {
    const canvas = document.getElementById('car-canvas');
    const container = document.getElementById('car-container');

    canvas.style.width = '100%';
    canvas.style.height = '100%';

    // Crear la escena
    scene = new THREE.Scene();

    // Crear la cámara
    camera = new THREE.PerspectiveCamera(75, container.clientWidth / container.clientHeight, 0.1, 1000);

    // Crear el renderizador
    renderer = new THREE.WebGLRenderer({ canvas: canvas, antialias: true, alpha: true });
    renderer.setSize(container.clientWidth, container.clientHeight);

    // Establecer el color de fondo del renderizador como transparente
    renderer.setClearColor(0x000000, 0);

    // Crear los controles de órbita
    controls = new THREE.OrbitControls(camera, renderer.domElement);
    controls.enableDamping = true;
    controls.dampingFactor = 0.25;
    controls.enableZoom = false;

    // Ajustar el tamaño del renderizador cuando la ventana cambia de tamaño
    window.addEventListener('resize', () => {
        renderer.setSize(container.clientWidth, container.clientHeight);
        camera.aspect = container.clientWidth / container.clientHeight;
        camera.updateProjectionMatrix();
    });

    // Añadir luz ambiental
    const ambientLight = new THREE.AmbientLight(0xffffff, 0.5);
    scene.add(ambientLight);

    // Añadir luz direccional
    const directionalLight = new THREE.DirectionalLight(0xffffff, 1);
    directionalLight.position.set(5, 5, 5);
    scene.add(directionalLight);

    // Cargar el modelo 3D inicial del auto
    changeCarModel("iniciar");

    // Manejar cambio de modelo con las flechas
    document.querySelector('.left-arrow').addEventListener('click', () => changeCarModel('left'));
    document.querySelector('.right-arrow').addEventListener('click', () => changeCarModel('right'));
}

function loadCarModel(modelPath, cameraPosition, controlsTarget) {
    const loader = new THREE.GLTFLoader();
    loader.load(modelPath, function(gltf) {
        if (carModel) {
            scene.remove(carModel);
        }
        carModel = gltf.scene;

        centerModel(carModel);
        scaleModel(carModel, 1);

        scene.add(carModel);
        resetCameraAndControls(cameraPosition, controlsTarget);
        animate();
    }, undefined, function(error) {
        console.error('An error happened', error);
    });
}

function changeCarColor(color) {
    if (carModel) {
        carModel.traverse((child) => {
            if (child.isMesh) {
                // Cambiar el color solo si el nombre coincide con la parte de la carrocería
                // COLOR 1ER AUTO
                if (child.name.includes('Chassis_Chassis_0')) {
                    child.material.color.set(color);
                }
                // COLOR 2ER AUTO
                if (child.name.includes('Body_CarTex_1_0')) {
                    child.material.color.set(color);
                }
                // COLOR 3ER AUTO
                if (child.name.includes('Body_Color1_0')) {
                    child.material.color.set(color);
                }
                if (child.name.includes('Body_Color2_0')) {
                    child.material.color.set(color);
                }
            }
        });
    }
}

function changeCarModel(direction) {
    if (direction === 'left') {
        currentModelIndex = (currentModelIndex - 1 + cantidad_autos) % cantidad_autos;
    } else if (direction === 'right') {
        currentModelIndex = (currentModelIndex + 1) % cantidad_autos;
    }
    auto = autos_usuario[currentModelIndex]
    if (auto.modelo === modelPaths[0]) {
        loadCarModel(modelPaths[0], new THREE.Vector3(0.5, -2, 1), new THREE.Vector3(0, -2.3, 0));
    } else if (auto.modelo === modelPaths[1]) {
        loadCarModel(modelPaths[1], new THREE.Vector3(1, 0, 0), new THREE.Vector3(0, 0, 0));
    } else if (auto.modelo === modelPaths[2]) {
        loadCarModel(modelPaths[2], new THREE.Vector3(1, -0.7, 0), new THREE.Vector3(0, -0.7, 0));
    }
    setTimeout(() => {
        changeCarColor(auto.color);
    }, 70)

    cambiar_nombre_auto();
}

function cambiar_nombre_auto() {
    const recuadro_nombre_auto = document.getElementById('car-name');
    recuadro_nombre_auto.textContent = auto.nombre;
}

function animate() {
    requestAnimationFrame(animate);
    controls.update();
    renderer.render(scene, camera);
}

function centerModel(model) {
    const box = new THREE.Box3().setFromObject(model);
    const center = box.getCenter(new THREE.Vector3());
    model.position.sub(center);
}

function scaleModel(model, targetScale) {
    const box = new THREE.Box3().setFromObject(model);
    const size = box.getSize(new THREE.Vector3());
    const maxDim = Math.max(size.x, size.y, size.z);
    const scale = targetScale / maxDim;
    model.scale.set(scale, scale, scale);
}

function resetCameraAndControls(position, target) {
    camera.position.copy(position);
    controls.target.copy(target);
    controls.update();
}

function borrar_auto(){
    fetch(window.location.href + auto.nombre,
        {method: "DELETE" , 
        headers: {'Content-Type': 'application/json'},
        body: JSON.stringify( {
            nombre: auto.nombre
            } )
        })
        .then(response => response.json())
        .then(data => {
            if (data.error){
                alert(data.error);
            }else{
                alert(data.mensaje);
            }
        })
}