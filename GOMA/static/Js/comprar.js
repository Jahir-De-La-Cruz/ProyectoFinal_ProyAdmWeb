document.addEventListener('DOMContentLoaded', function() {
    const comprarButtons = document.querySelectorAll('.comprar-button');

    comprarButtons.forEach(button => {
        button.addEventListener('click', () => {
            const productId = button.dataset.productId;
            const productName = button.closest('.seccion__productos-producto').querySelector('.productos__titulo').textContent;
            const precioText = button.closest('.seccion__productos-producto').querySelector('.productos__precio').textContent;

            // Extraer solo los números del texto del precio
            const priceMatch = precioText.match(/(\d+(\.\d+)?)/);

            // Verificar si se encontró un precio válido en el texto
            if (priceMatch && priceMatch[1]) {
                // Convertir el precio a número
                const productPrice = parseFloat(priceMatch[1]);

                // Formatear el precio como pesos mexicanos
                const formattedPrice = productPrice.toLocaleString('es-MX', { style: 'currency', currency: 'MXN' });

                // Establecer la cantidad como 1
                const quantity = 1;

                // Construir la URL con los datos del producto y la cantidad
                const url = `/confirmar_compra/?productos=${encodeURIComponent(productName)}&precio_final=${productPrice}&cantidades=${quantity}&id=${productId}`;

                swal({
                    title: '¿Estás seguro de realizar la compra?',
                    text: `Estás a punto de comprar "${productName}" por ${formattedPrice}.`,
                    icon: "warning",
                    buttons: {
                        cancel: 'Cancelar',
                        confirm: 'Comprar'
                    },
                    dangerMode: true
                }).then((confirmed) => {
                    if (confirmed) {
                        window.location.href = url;
                    }
                });
            } else {
                // Mostrar mensaje de error si no se pudo extraer el precio del texto
                swal({
                    title: 'Error',
                    text: 'No se pudo obtener el precio del producto. Por favor, inténtelo de nuevo.',
                    icon: 'error',
                    button: 'Aceptar'
                });
            }
        });
    });
});
