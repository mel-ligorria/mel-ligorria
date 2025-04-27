function Presentacion({ nombre, edad, profesion }) {
  return (
    <div className="presentacion">
      <h2>Presentación</h2>  
      <p> Hola, soy {nombre}, tengo {edad} años y soy {profesion}. </p>
    </div>
  );
}

export default Presentacion;