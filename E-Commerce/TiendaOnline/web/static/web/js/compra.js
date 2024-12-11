const opcion = document.getElementById('medio_de_pago')

const efectivo = document.getElementById('pago_efectivo')
const datosTransferencia = document.getElementById('datos_transferencia')

const mostrar_efectivo = function(){
    if (opcion.value === 'Efectivo'){
        efectivo.hidden = false
    }
    else{
        efectivo.hidden = true
    }
}

const mostrar_transferencia = function(){
    if (opcion.value === 'Transferencia'){
        datosTransferencia.hidden = false
    }
    else{
        datosTransferencia.hidden = true
    }
}

opcion.addEventListener('change', mostrar_efectivo)
opcion.addEventListener('change', mostrar_transferencia)