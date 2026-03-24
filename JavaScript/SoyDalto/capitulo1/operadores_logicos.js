// Operadores Logicos

/*
    Los operadores logicos nos devuelven un resultado a partir de que se cumpla (o no) una condicion,
    su resultado es booleano, y sus operandos son valores logicos o asimilables a ellos
*/


// Equality

let numero = 23;
let numero2 = 23;
let numero3 = "23";

// Debemos de usar siempre doble signo == porque si se usa solo uno, estamos asignando un valor y no comparando
document.write(numero == numero2)

// Con doble igual compara si son iguales, incluso si no son del mismo tipo como un numero y un string

// El triple igual es para saber si estrictamente son iguales, es decir en tipo y valor

document.write(numero === numero3)


// Inequality

// Es lo mismo pero con la negacion, y se usa un simbolo = menos

document.write(numero != numero2)


let valor = false;
let valor2 = true;

// Ambas deben de ser TRUE para que devuelva TRUE
let resultado = valor && valor2;

// En esta variable, cualquiera de las opciones debe de ser TRUE para devolver TRUE, y si ambas son FALSE devolvera
// FALSE
let resultado2 = valor || valor2;

// La negacion NOT devuelve lo contrario que asignamos en la variable y solo funciona con TRUE y FALSE
let resultado3 = !valor;

document.write(`<br> ${resultado} <br>`)
document.write(`${resultado2} <br>`)
document.write(`${resultado3} <br>`)


// Es posible mezclar los operadores logicos

num1 = 12;
num2 = 24;
num3 = 25;
num4 = 92;
num5 = 91;

loop = (num1 < num2 || num2 < num3) && (!(num1 != num2) && num5 != num3);




























































































