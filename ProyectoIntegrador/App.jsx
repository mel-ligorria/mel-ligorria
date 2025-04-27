import './App.css'
import Saludo from './Componentes/Saludo' 
import Presentacion from './Componentes/Presentacion'
import BotonTailwind from './Componentes/BotonTailwind'
import Contacto from './Componentes/Contacto'


function App() {

  return (
    <>
    <Saludo nombre = "Martín"/>
    <Presentacion nombre = "Martín" edad = {30} profesion = "Informatico"/>
    <BotonTailwind/>
    <Contacto/>
    </>
  )
}

export default App;

