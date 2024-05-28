// Función que suma un número float y un int
function sumarFloatYInt() {
    // Declaración de variables
    let numeroFloat = 3.14; // Número flotante
    let numeroInt = 5;      // Número entero

    // Realizar la suma
    let resultado = numeroFloat + numeroInt;

    // Mostrar el resultado
    console.log("La suma de " + numeroFloat + " y " + numeroInt + " es: " + resultado);
    console.log("Jose",luis,"mario");
    console.log("Esta es una prueba con", 9+10," las 2 maneras");
}

// Función que muestra un contador del 1 al 10
function mostrarContador() {
    // Bucle for para contar del 1 al 10
    for (let i = 1; i <= 10; i++) {
        console.log("Contador: " + i);
    }
}

// Llamada a las funciones para su ejecución
sumarFloatYInt();
mostrarContador();

