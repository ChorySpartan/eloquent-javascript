saludo = "Hola Pepe";
pregunta = " Como estas";

frase = saludo + pregunta;

document.write(frase)

// Concatenacion de Numeros

numero1 = 5;
numero2 = 9;
// Podemos simplemente agregar un texto vacio y despues las variables con numeros
frase2 = " " + numero1 + numero2;

document.write(frase2)


// Concatenacion con CONCAT

numero3 = " 3";
numero4 = 7;

// CONCAT sirve para lo mismo, pero la variable que llama al metodo tiene que ser un string obligatoriamente
frase3 = numero3.concat(numero4);

document.write(frase3)

// Concatenacion con backticks `` y ${}

nombre = "Rodolfo Laynez";

frase4 = ` Soy ${nombre} y estoy caminando`;

document.write(frase4)



























































































