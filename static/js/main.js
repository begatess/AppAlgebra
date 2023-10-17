// Sidebar Hide
function openNav() {
    document.getElementById("overlay").style.display = "block";
    document.getElementById("sideNavigation").style.width = "250px";
    document.getElementById("main").style.marginLeft = "250px";
    
}
function closeNav() {
    document.getElementById("overlay").style.display = "none";
    document.getElementById("sideNavigation").style.width = "0";
    document.getElementById("main").style.marginLeft = "0";
    document.getElementById("sidebar_inner").style.display = "none";
}

//Incripcion de Materias
// Selecciona todos los elementos <a> con la clase "materias-link" que tienen el atributo data-materia-id
