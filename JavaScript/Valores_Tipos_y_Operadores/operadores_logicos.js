// OPERADORES LÓGICOS

/*
    En JavaScript podemos utilizar tres operadores, AND (&&) OR (||) y NOT (!)
*/


//Con AND && ambas condiciones deben de ser iguales para que devuelva True, de lo contrario
//devolverá False

console.log(true && false)
// → false
console.log(true && true)
// → true



//Con OR || si alguna de las condiciones es verdadera, el resultado mostrará True

console.log(false || true)
// → true
console.log(false || false)
// → false



//Con NOT ! podemos invertir el valor que estamos asignando, True será False y viceversa

// Definimos una variable booleana
let estaLloviendo = true;

// Usamos el operador de negación (!) para invertir su valor
let noEstaLloviendo = !estaLloviendo;

console.log("¿Está lloviendo?", estaLloviendo);       // Salida: ¿Está lloviendo? true
console.log("¿NO está lloviendo?", noEstaLloviendo); // Salida: ¿NO está lloviendo? false


/*
    Operador Condicional (Ternario): condicion ? expresion1 : expresion2

    Este es un operador ternario porque toma tres operandos: una condición, una expresión
    para cuando la condición es verdadera, y una expresión para cuando la condición es falsa.
    Es una forma concisa de escribir una sentencia if...else simple en una sola línea.

    En este caso, nos devolverá la primera expresión True y la segunda False

    Sintaxis:

    condicion ? valorSiVerdadero : valorSiFalso;

*/


let edad = 18;
let mensaje = (edad >= 18) ? "Eres mayor de edad" : "Eres menor de edad";
console.log(mensaje); // Salida: "Eres mayor de edad"

edad = 16;
mensaje = (edad >= 18) ? "Eres mayor de edad" : "Eres menor de edad";
console.log(mensaje); // Salida: "Eres menor de edad"



































































































