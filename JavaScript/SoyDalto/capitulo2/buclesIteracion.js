// WHILE

// Primero se pregunta la condición y luego se ejecuta

let numeroParaSumar = 0;

while (numeroParaSumar < 5) {
    numeroParaSumar++; //Primero suma y luego imprime, es decir 0 + 1, 1,2,3,4,5
    document.write(numeroParaSumar + "<br>");
}



//DO WHILE

// Primero se ejecuta y luego se pregunta la condición, y siempre va acompañado de un while al final
// Este siempre se va a ejecutar una vez aunque la condición sea falsa

let numero = 0;

do {
    document.write(numero + "<br>"); // Primero imprime y luego suma, por eso se muestra solo del 0 al 4 porque
                                     // inicia en 0
    numero++;
} while (numero < 5) // Esto no mostrará nunca el 5, solo llegará al 4



let edad;

do {
    edad = parseInt(prompt("Ingresa tu edad: "));
} while (edad < 0 || isNaN(edad)); // En este caso si es negativo o si no es un numero se va a repetir

console.log(`Tu edad es ${edad}`);


let retoCloude;

do {
    retoCloude = parseInt(prompt("Ingresa un número válido "));
} while (retoCloude < 0 || isNaN(retoCloude));
document.write(`El numero es ${retoCloude * 2}`);




















































































