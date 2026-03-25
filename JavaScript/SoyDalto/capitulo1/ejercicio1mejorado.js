

const definirCompra2 = (n)=> {
    let din = parseFloat(prompt(`Dinero de ${n}`));

    let helado, precio;

    if (din >= 0.6 && din < 1)        { helado = "helado de agua"; precio = 0.6; }
    else if (din >= 1 && din < 1.6)   { helado = "helado de crema"; precio = 1;   }
    else if (din >= 1.6 && din < 1.7) { helado = "helado de heladix"; precio = 1.6; }
    else if (din >= 1.7 && din < 1.8) { helado = "helado de heladovich"; precio = 1.7; }
    else if (din >= 1.8 && din < 2.9) { helado = "helado de helardo"; precio = 1.8; }
    else if (din >= 2.9)              { helado = "helado de confites o pote 1/4KG"; precio = 2.9; }
    else return `${n}: No te alcanza para ningún helado, pobre de mierda`;

    let sobrante = (din - precio).toFixed(2);
    return `${n}: ${helado} | Te sobran $${sobrante}`;
}

const resultadoJuan = definirCompra2("Juan")
const resultadoRodolfo = definirCompra2("Rodolfo")
const resultadoAlejandro = definirCompra2("Alejandro")



alert(resultadoJuan);
alert(resultadoRodolfo);
alert(resultadoAlejandro);


























