// Mostrar un mensaje de confirmación al ejecutar una acción personalizada
document.addEventListener("DOMContentLoaded", function () {
    const actionButtons = document.querySelectorAll(".action-select");

    actionButtons.forEach(function (button) {
        button.addEventListener("click", function (event) {
            const confirmMessage = "¿Estás seguro de ejecutar esta acción?";
            if (!confirm(confirmMessage)) {
                event.preventDefault(); // Cancela la acción si el usuario selecciona "Cancelar"
            }
        });
    });
});

// Resaltar filas en la lista de objetos al pasar el mouse
document.addEventListener("mouseover", function (event) {
    const target = event.target.closest("tr");
    if (target && target.classList.contains("row1")) {
        target.style.backgroundColor = "#f9f9f9";
    }
});

document.addEventListener("mouseout", function (event) {
    const target = event.target.closest("tr");
    if (target && target.classList.contains("row1")) {
        target.style.backgroundColor = "";
    }
});
