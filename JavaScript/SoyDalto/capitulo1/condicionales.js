// CONDICIONALES

// En JavaScript, una condicional evalua si una expresion es true o false

// IF

nombre = "Javi"

if (nombre == "lucas") {
    alert("tu nombre es malardo")
}


// ELSE IF

// Podemos usar los que querramos

else if (nombre == "dalto") {
    alert("tu nombre es " + nombre)
}

// ELSE

// Esto sirve para realizar algo si ninguna condicion creada anteriormente se cumple

else {
    alert("tu nombre es otro")
}


// TERNARIO

// Es una forma abreviada de hacer condicionales

let edad = 10;
let mensaje = (edad >= 18) ? "Entras al club" : "A dormir temprano";
console.log(mensaje)

// SWITCH

// Se usa cuando se tiene muchas opciones posibles para una sola variable. Es mas organizado que tener varios else if
// seguidos.

let puestoEnLiga = "primero";

switch (puestoEnLiga) {
    case "primero":
        console.log("Ganamos la copa");
        break; // Esto sirve para que no se siga ejecutando el codigo si ya se cumplio con la condicion que lo antecede
    case "segundo":
        console.log("Subcampeones");
        break;
    default:
        console.log("A seguir practicando");
}



























































































