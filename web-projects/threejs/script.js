let scene, camera, renderer, cube

function init(){

    // create a scene with THREE library
    scene = new THREE.Scene();

    //create camera variable, using angle and perspective
    camera = new THREE.PerspectiveCamera(75, 
    window.innerWidth / window.innerHeight, 0.1, 1000);

    //initialize renderer (Web Graphics Library) (later add anti-aliasing)
    renderer = new THREE.WebGLRenderer({antialias: true});

    //set size of renderer to be entire size of screen
    renderer.setSize(window.innerWidth, window.innerHeight);

    //render into html
    document.body.appendChild(renderer.domElement);

    //add first object into scene:
    const geometry = new THREE.BoxGeometry(2, 2, 2)
    //create texture after functions are done

    //
    const texture = new THREE.TextureLoader().load('textures/crate.gif')
    //const material = new THREE.MeshBasicMaterial({color : 0x0000ff });
    cube = new THREE.Mesh(geometry, texture);

    //add into scene
    scene.add(cube);

    //change camera's z-index to see the cube
    camera.position.z = 5;

}




function animate() {
    requestAnimationFrame(animate);

    cube.rotation.x += 0.01;
    cube.rotation.y += 0.01;

    cube.position.x += 0.05;

    if (cube.position.x > 5){
        cube.position.x = -5;
    }

    renderer.render(scene, camera);
}

function onWindowResize(){
    camera.aspect = window.innerWidth / window.innerHeight;
    camera.updateProjectionMatrix();
    renderer.setSize(window.innerWidth, window.innerHeight);

}

window.addEventListener('resize', onWindowResize, false);

//call our animate function to actually render into the screen
init();
animate();


