document.addEventListener('DOMContentLoaded', function() {
    const addToCartButtons = document.querySelectorAll('.añadir_al_carrito');
    const cartItemsContainer = document.querySelector('.cart-items tbody');
    const cartTotalPrice = document.getElementById('cart-total-price');
    const cartToggleButton = document.querySelector('.carrito');
    const cartContainer = document.querySelector('.cart-items-container');
    const cartCloseButton = document.querySelector('.cart-close-button');
    const buyButton = document.getElementById('cart-button-buy');
    const clearButton = document.getElementById('cart-button-clear');

    // Función para agregar un producto al carrito
    function addToCart(producto) {
        let existingCartItem = findCartItem(producto.id);

        if (existingCartItem) {
            // Si el producto ya está en el carrito, incrementa su cantidad
            const quantityElement = existingCartItem.querySelector('.item-quantity');
            quantityElement.value = parseInt(quantityElement.value) + 1;
        } else {
            // Si el producto no está en el carrito, agrégalo con cantidad 1
            const row = createCartItemRow(producto);
            cartItemsContainer.appendChild(row);
        }

        // Actualizar el precio total del carrito
        updateTotalPrice();

        // Mostrar el carrito
        cartContainer.classList.add('show');
    }

    // Función para buscar un elemento del carrito por el ID del producto
    function findCartItem(productId) {
        return cartItemsContainer.querySelector(`tr[data-product-id="${productId}"]`);
    }

    // Función para crear una fila de artículo en el carrito
    function createCartItemRow(producto) {
        const row = document.createElement('tr');
        row.dataset.productId = producto.id;
        row.innerHTML = `
            <td><img src="${producto.imagen}" alt="${producto.nombre}" style="width: 50px;"></td>
            <td>${producto.nombre}</td>
            <td>${producto.precio.toLocaleString('es-MX', { style: 'currency', currency: 'MXN' })}</td>
            <td><input type="number" class="item-quantity" value="1" min="1"></td>
            <td><button class="delete-button"><i class="fa-solid fa-times"></i></button></td>
        `;
        return row;
    }

    // Función para actualizar el precio total del carrito
    function updateTotalPrice() {
        let totalPrice = 0;
        cartItemsContainer.querySelectorAll('tr').forEach(row => {
            const priceText = row.querySelector('td:nth-child(3)').textContent; // Obtener el texto del precio
            const price = parseFloat(priceText.replace('$', '').replace(',', '')); // Convertir el texto del precio a número
            const quantity = parseInt(row.querySelector('.item-quantity').value); // Obtener la cantidad del producto
            totalPrice += price * quantity; // Calcular el precio total
        });
        cartTotalPrice.textContent = `Precio total: ${totalPrice.toLocaleString('es-MX', { style: 'currency', currency: 'MXN' })}`; // Mostrar el precio total formateado como pesos mexicanos
    }


    // Función para mostrar u ocultar el carrito
    function toggleCart() {
        console.log('Haciendo clic en el botón del carrito...');
        cartContainer.classList.toggle('show');
    }

    // Manejar clic en el botón del carrito
    cartToggleButton.addEventListener('click', toggleCart);

    // Manejar clic en el botón de cerrar el carrito
    cartCloseButton.addEventListener('click', toggleCart);

    // Manejar clic en botones de añadir al carrito
    addToCartButtons.forEach(button => {
        button.addEventListener('click', (event) => {
            const productId = event.currentTarget.dataset.productId;
            const productName = event.currentTarget.closest('.seccion__productos-producto').querySelector('.productos__titulo').textContent;
            const productPrice = parseFloat(event.currentTarget.dataset.productPrice); // Acceder al precio desde el atributo de datos

            const productImage = event.currentTarget.closest('.seccion__productos-producto').querySelector('.productos__img').src;

            const producto = {
                id: productId,
                nombre: productName,
                precio: productPrice,
                imagen: productImage
            };

            addToCart(producto);
        });
    });

    // Manejar clic en el botón de comprar
    buyButton.addEventListener('click', () => {
        const cartItems = cartItemsContainer.getElementsByTagName('tr');
        if (cartItems.length === 0) {
            swal({
                title: 'Carrito vacío',
                text: 'El carrito de compras está vacío. Agrega productos antes de realizar la compra.',
                icon: "error",
                button: "Aceptar"
            });
            return;
        }

        // Obtener los nombres, cantidades y precios de los productos del carrito
        const productDetails = [];
        const productPrices = [];
        const productQuantities = [];
        for (let i = 0; i < cartItems.length; i++) {
            const productName = cartItems[i].getElementsByTagName('td')[1].textContent;
            const productQuantity = cartItems[i].querySelector('.item-quantity').value;
            const productPrice = parseFloat(cartItems[i].getElementsByTagName('td')[2].textContent.replace('$', '').replace(',', ''));
            productDetails.push(encodeURIComponent(productName));
            productQuantities.push(productQuantity);
            productPrices.push(productPrice);
        }

        // Construir la URL con los datos del carrito
        const url = `/confirmar_compra/?productos=${productDetails.join(',')}&cantidades=${productQuantities.join(',')}&precio_final=${calculateTotalPrice(productPrices)}`;

        // Mostrar mensaje de confirmación con SweetAlert
        swal({
            title: '¿Estás seguro de realizar la compra?',
            text: `Resumen del pedido:\n\n${productDetails.map((detail, index) => `${decodeURIComponent(detail)} (Cantidad: ${productQuantities[index]}) - Precio: ${productPrices[index].toLocaleString('es-MX', { style: 'currency', currency: 'MXN' })}`).join('\n')}\nTotal: ${calculateTotalPrice(productPrices).toLocaleString('es-MX', { style: 'currency', currency: 'MXN' })}\n\nUna vez confirmada la compra, los productos serán enviados y no podrás deshacer esta acción.`,
            icon: 'warning',
            buttons: {
              cancel: 'Cancelar',
              confirm: 'Comprar'
            },
            dangerMode: true
          }).then((confirmed) => {
            if (confirmed) {
              window.location.href = url; // Redirige si el usuario confirma la compra
            }
          });          
    });

    // Función para calcular el precio total
    function calculateTotalPrice(prices) {
        return prices.reduce((total, price) => total + price, 0);
    }

    // Manejar clic en el botón de vaciar pedido
    clearButton.addEventListener('click', () => {
        // Vaciar el carrito
        cartItemsContainer.innerHTML = '';
        updateTotalPrice();
    });

    // Manejar clic en el botón de eliminar producto del carrito
    cartItemsContainer.addEventListener('click', (event) => {
        if (event.target.classList.contains('delete-button')) {
            const row = event.target.closest('tr');
            row.remove();
            updateTotalPrice();
        }
    });
});
