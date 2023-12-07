document.addEventListener('DOMContentLoaded', function() {
    const form = document.getElementById('person-form');
    const table = document.getElementById('person-table').getElementsByTagName('tbody')[0];

    form.addEventListener('submit', function(event) {
        event.preventDefault();

        const nombre = document.getElementById('nombre').value;
        const apellido = document.getElementById('apellido').value;

        if (nombre && apellido) {
        
            const newRow = table.insertRow();
            const cell1 = newRow.insertCell(0);
            const cell2 = newRow.insertCell(1);
            cell1.textContent = nombre;
            cell2.textContent = apellido;

            
            form.reset();
        } else {
            alert('Por favor, ingrese nombre y apellido.');
        }
    });
});
