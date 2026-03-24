// CADENAS

/*Puedes usar comillas simples, comillas dobles o acentos graves para marcar
las cadenas, siempre y cuando las comillas al principio y al final de la cadena
coincidan.

 */

let string = 'Rodolfo Laynez'

// Saltos de Línea
let string2 = "Esta es la primera línea\nY esta es la segunda"
console.log(string2)

// Texto Multilínea

let textoMultiLinea = `Esta es la primera línea.
Esta es la segunda línea.
                              Y esta es la tercera línea.`;
console.log(textoMultiLinea)




// CONCATENACIÓN


// Ejemplo 1: Uniendo dos cadenas literales

let saludo = "Hola";
let nombre = "Mundo";
let mensajeCompleto = saludo + " " + nombre + "!";
console.log(mensajeCompleto); // Salida: "Hola Mundo!"

// Ejemplo 2: Concatenando con variables y texto literal

let producto = "camiseta";
let precio = 25;
let mensajeCompra = "Compraste una " + producto + " por $" + precio + ".";
console.log(mensajeCompra); // Salida: "Compraste una camiseta por $25."

// Ejemplo 3: Uniendo solo texto literal
console.log("¡Qué " + "bonito " + "día!"); // Salida: "¡Qué bonito día!"


// TEMPLATE LITERALS

let nombreProducto = "Camisa";
let precio2 = 35.50;
let inventario = 10;

let descripcion = `La ${nombreProducto} cuesta $${precio2} y quedan ${inventario} unidades.`;
console.log(descripcion); // Salida: El Camisa cuesta $35.50 y quedan 10 unidades.

let suma = 5 + 3;
let resultado = `La suma es: ${suma}`;
console.log(resultado); // Salida: La suma es: 8



//OPERADORES UNARIOS

/*
    Los operadores que utilizan dos valores se llaman operadores binarios, mientras que
    aquellos que toman uno se llaman operadores unarios.
*/

console.log(typeof 4.5)
console.log(typeof "x")





























































































