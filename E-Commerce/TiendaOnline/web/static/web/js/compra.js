const opcionMedioDePago = document.getElementById('medio_de_pago')
const efectivo = document.getElementById('pago_efectivo')
const transferencia = document.getElementById('pago_transferencia')

const mostrar_efectivo = function(){
    if (opcionMedioDePago.value === 'Efectivo'){
        efectivo.hidden = false
    }
    else{
        efectivo.hidden = true
    }
}

const mostrar_transferencia = function(){
    if (opcionMedioDePago.value === 'Transferencia'){
        transferencia.hidden = false
    }
    else{
        transferencia.hidden = true
    }
}

opcionMedioDePago.addEventListener('change', mostrar_efectivo)
opcionMedioDePago.addEventListener('change', mostrar_transferencia)