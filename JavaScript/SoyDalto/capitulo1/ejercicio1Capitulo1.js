
dineroCofla = prompt("Cuanto dinero tienes Cofla?");
dineroRoberto = prompt("Cuanto dinero tienes Roberto?");
dineroJavi = prompt("Cuanto dinero tienes Javi?");

// Cofla

if (dineroCofla > 0.6 && dineroCofla < 1) {
    alert("Cofla, comprate el helado de agua")
}

else if (dineroCofla > 1 && dineroCofla < 1.6) {
    alert("Cofla, comprate el helado de crema")
}

else if (dineroCofla > 1.6 && dineroCofla < 1.7) {
    alert("Cofla, comprate el helado de heladix")
}

else if (dineroCofla > 1.7 && dineroCofla < 1.8) {
    alert("Cofla, comprate el helado de heladovich")
}

else if (dineroCofla > 1.8 && dineroCofla < 2.9) {
    alert("Cofla, comprate el helado de helardo")
}

else if (dineroCofla >= 2.9) {
    alert("Cofla, comprate el helado con confites o el pote de 1/4 KG")
} else {
    alert("Cofla, lo siento pobre de mierda, no te alcanza pa na")
}

// Roberto
if (dineroRoberto > 0.6 && dineroRoberto < 1) {
    alert("Roberto, comprate el helado de agua")
}

else if (dineroRoberto > 1 && dineroRoberto < 1.6) {
    alert("Roberto, comprate el helado de crema")
}

else if (dineroRoberto > 1.6 && dineroRoberto < 1.7) {
    alert("Roberto, comprate el helado de heladix")
}

else if (dineroRoberto > 1.7 && dineroRoberto < 1.8) {
    alert("Roberto, comprate el helado de heladovich")
}

else if (dineroRoberto > 1.8 && dineroRoberto < 2.9) {
    alert("Roberto, comprate el helado de helardo")
}

else if (dineroRoberto >= 2.9) {
    alert("Roberto, comprate el helado con confites o el pote de 1/4 KG")
} else {
    alert("Roberto, lo siento pobre de mierda, no te alcanza pa na")
}


// Javi

if (dineroJavi > 0.6 && dineroJavi < 1) {
    alert("Javi, comprate el helado de agua")
}

else if (dineroJavi > 1 && dineroJavi < 1.6) {
    alert("Javi, comprate el helado de crema")
}

else if (dineroJavi > 1.6 && dineroJavi < 1.7) {
    alert("Javi, comprate el helado de heladix")
}

else if (dineroJavi > 1.7 && dineroJavi < 1.8) {
    alert("Javi, comprate el helado de heladovich")
}

else if (dineroJavi > 1.8 && dineroJavi < 2.9) {
    alert("Javi, comprate el helado de helardo")
}

else if (dineroJavi >= 2.9) {
    alert("Javi, comprate el helado con confites o el pote de 1/4 KG")
} else {
    alert("Javi, lo siento pobre de mierda, no te alcanza pa na")
}


// Lo que hicimos arriba, podemos hacerlo con el siguiente codigo que ademas, es y funciona mejor

const definirCompra = (n)=> {
    let din = prompt(`Dinero de ${n}`);
    if (din >= 0.6 && din < 1) return (`${n}: helado de agua`);
    if (din >= 1 && din < 1.6) return (`${n}: helado de crema`);
    if (din >= 1.6 && din < 1.7) return (`${n}: helado de heladix`);
    if (din >= 1.7 && din < 1.8) return (`${n}: helado de heladovich`);
    if (din >= 1.8 && din < 2.9) return (`${n}: helado de helardo`);
    if (din >= 2.9) return (`${n}: helado de confites o pote de 1/4 KG`);
    else return (`${n}: No te alcanza para ningun helado pobre de mierda`);
}

console.log(definirCompra("Juan"));
console.log(definirCompra("Rodolfo"));
console.log(definirCompra("Alejandro"));





























































































