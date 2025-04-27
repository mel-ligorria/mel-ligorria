// 1. Escribir un programa: 
let Nombre = Ana 
let Edad = 22 
console.log("Hola, me llamo " + nombre + " y tengo " + edad + " años.");

//2. Dado el siguiente array:

// Números al cuadrado usando map
const numeros = [3, 7, 12, 5, 2];
const alcuadrado = numeros.map (x => x **2)
console.log(alcuadrado)

// Números mayores a 5 usando filter
const mayores = numeros.filter (x => x > 5)
console.log(mayores)

// Par o impar
function verificarParOImpar(numero) {
const resultado = numero % 2 === 0 ? "par":"impar";    
return resultado; }

console.log(verificarParOImpar(4));


//Actividad 2: Desestructuración y objetos
//Guía de Actividades Diagnósticas 1
//1. Mostrar en consola un mensaje que diga: "Lucía tiene 28 años y trabaja
//como Diseñadora." usando desestructuración.
//b2. Agregar una nueva propiedad al objeto llamada ciudad con el valor "Rosario" .

//Respuestas

//1. Mostrar en consola un mensaje que diga: "Lucía tiene 28 años y trabaja como Diseñadora." usando desestructuración. 

const persona = {
nombre: "Lucía",
edad: 28,
profesion: "Diseñadora",
};

const  { nombre, edad, profesion } = persona;
console.log(`${nombre} tiene ${edad} años y trabaja como ${profesion}.`);

//2. Agregar una nueva propiedad al objeto llamada ciudad con el valor "Rosario" 

persona.ciudad= "Rosario";
console.log(persona); 


//Actividad 3: Funciones y callbacks
// Instrucciones:
// 1. Escribir una función que reciba un array y una función callback. La función
//debe aplicar el callback a cada elemento del array y retornar el nuevo array.
//Ejemplo de uso:

procesar([1, 2, 3], x => x * 2); // [2, 4, 6]

function procesar (array, callback) {
const agregarArray =  array.map(callback)
return agregarArray;
}

const resultado = procesar([4, 8, 10], x => x * 2);
console.log(resultado);


//Ejercicio numero 6
const productos = [
    { nombre: "Notebook", precio: 1200 },
    { nombre: "Mouse", precio: 20 },
    { nombre: "Teclado", precio: 50 },
    { nombre: "Monitor", precio: 300 },
    { nombre: "Auriculares", precio: 80 },
  ];
  //Filter
  const productosCaros = productos.filter(producto => producto.precio > 100);
  console.log("Productos caros:", productosCaros);  

  //Map
  const ProductosString = productos.map (producto => `${producto.nombre} - $${producto.precio}`);
  console.log("Productos en string:", ProductosString);

  //Reduce
  const TotalPrecio = productos.reduce((total, producto) => total + producto.precio, 0);
  console.log("Total precio:", TotalPrecio);

  //Filter + Map
const productosMenos = productos.filter(producto => producto.precio <100)
.map(producto => producto.nombre.toLocaleLowerCase())
console.log("Productos menos de 100 y en minuscula:", productosMenos);


