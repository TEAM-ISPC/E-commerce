export class Producto{

    constructor(id:string, descripcion:string, nombre:string, imagen:string, precio:number, suspendida:boolean){

    this.id=id;
    this.descripcion=descripcion;
    this.nombre=nombre;
    this.imagen=imagen;
    this.precio=precio;
    this.suspendida=suspendida;



    }


    id:string;
    descripcion:string;
    nombre:string;
    imagen:string;
    precio:number;
    suspendida:boolean;
}
