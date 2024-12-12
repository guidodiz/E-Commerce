const procesarCompra = document.getElementById('procesar_compra')
const resumenCompra = document.getElementById('resumen_compra')
const botonCompra = document.getElementById('boton_compra')

const siguiente = document.getElementById('siguiente')

const medioDePagoInput = document.getElementById('medio_de_pago')
const envioInput = document.getElementById('envio')
const nombreInput = document.getElementById('nombre')
const emailInput = document.getElementById('email')
const wpInput = document.getElementById('wp')

const resumenMedioDePago = document.querySelector('input[name="resumenMedioDePago"]')
const resumenEnvio = document.querySelector('input[name="resumenEnvio"]')
const resumenNombre = document.querySelector('input[name="resumenNombre"]')
const resumenEmail = document.querySelector('input[name="resumenEmail"]')
const resumenWp = document.querySelector('input[name="resumenWp"]')

siguiente.addEventListener('click', function(event){
    event.preventDefault();
    
    if(medioDePagoInput.value === '' || envioInput.value === '' || nombreInput.value === '' || emailInput.value === '' || wpInput.value === ''){
        alert('Los campos deben estar completos')
        return
    }

    procesarCompra.hidden = true;
    resumenCompra.hidden = false;
    botonCompra.hidden = false;
    resumenMedioDePago.value = medioDePagoInput.value;
    resumenEnvio.value = envioInput.value;
    resumenNombre.value = nombreInput.value;
    resumenEmail.value = emailInput.value;
    resumenWp.value = wpInput.value;
})