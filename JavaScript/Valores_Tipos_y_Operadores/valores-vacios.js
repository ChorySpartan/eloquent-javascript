//VALORES VACÍOS

//Estos son NULL y UNDEFINED

/*
    Cuando se aplica un operador al tipo de valor “incorrecto”, JavaScript convertirá
    silenciosamente ese valor al tipo que necesita, utilizando un conjunto de reglas
    que a menudo no son las que deseas o esperas. Esto se llama coerción de tipos.
*/


//JavaScript siempre tratará de ejecutar de la mejor forma posible lo que le asignemos
//pero esto no es bueno, ya que debemos de poner atención con lo que programamos.
console.log(8 * null)
// → 0
console.log("5" - 1)
// → 4
console.log("5" + 1)
// → 51
console.log("five" * 2)
// → NaN
console.log(false == 0)
// → true


/*
    El null en la primera expresión se convierte en 0 y el "5" en la segunda expresión se
    convierte en 5 (de cadena a número). Sin embargo, en la tercera expresión, + intenta
    la concatenación de cadenas antes que la suma numérica, por lo que el 1 se convierte
    en "1" (de número a cadena).
*/



//UTILIZANDO ==

/*
    Cuando null o undefined aparece en cualquiera de los lados del operador, produce
    verdadero solo si ambos lados son uno de null o undefined.
*/


console.log(null == undefined);
// → true
console.log(null == 0);
// → false


/*
    Operador de Igualdad Estricta (===)
    El operador === se conoce como el operador de igualdad estricta (o "strict equality operator").

    ¿Qué hace?
    Compara si dos valores son iguales en valor Y en tipo. Si ambos son idénticos tanto en el
    dato que representan como en el tipo de dato que tienen, devuelve true; de lo contrario,
    devuelve false.
*/


console.log(5 === 5);         // true (número es igual a número)
console.log(5 === "5");       // false (valor es igual, PERO tipo es diferente: number vs string)


/*
    Operador de Desigualdad Estricta (!==)
    El operador !== se conoce como el operador de desigualdad estricta (o "strict inequality
    operator").

    ¿Qué hace?
    Es el opuesto directo del operador ===. Compara si dos valores no son iguales en valor o
    en tipo. Devuelve true si los valores son diferentes en valor, o si son del mismo valor
    pero de tipos diferentes. Devuelve false si los valores son idénticos tanto en valor como
    en tipo.
*/

console.log(5 !== 10);        // true (diferente valor)
console.log(5 !== 5);         // false (son estrictamente iguales)























































































