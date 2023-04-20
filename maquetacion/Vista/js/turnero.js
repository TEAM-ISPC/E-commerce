//Configuramos moment.js
moment.lang("es-mx");
// Cargamos datos de semana seleccionado
let fecha = document.getElementById("fecha");
fecha.setAttribute("value", moment().format("YYYY-MM-DD"));

//Obtenemos objeto de HTML (Table)
let tabla = document.getElementById("turnos");

// Generamos Datos de emprendimiento
let emprendimiento = {
  idEmprendedor: 1,
  diastrabajar: "L M Mi J V Se",
  horarioDiaNormalInicio: "08:00",
  horarioDiaNormalFinal: "20:00",
  horarioDiaEspecialInicio: "10:00",
  horarioDiaEspecialFinal: "16:00",
  tiempoTurno: 1,
  descripcion: "fdsfsdf",
  idCategoriasTrabajo: "Zapatería",
  redSocial1: "Insta/fsda",
  redSocial: "face.com",
  usuarioId: 1,
};

let turno = {
  idTurnos: 1,
  fecha: "29-10-2022",
  horaTurno: "15:00",
  clienteId: 1,
  trabajo: "Tatuaje",
  emprendedorId: 1,
  comentario: "jaja",
};

let turno2 = {
  idTurnos: 1,
  fecha: "29-10-2022",
  horaTurno: "19:00",
  clienteId: 1,
  trabajo: "Tatuaje",
  emprendedorId: 1,
  comentario: "jaja",
};

let ListaTurnosOcu = [];
ListaTurnosOcu.push(turno);
ListaTurnosOcu.push(turno2);

//Hilo

//generarTabla2();
setSemanas();

function generarTabla2(principio, fin) {
  var tblBody = document.createElement("tbody");
  //Generar Lista
  principio = moment(principio, "DD-MM-YYYY").format("YYYY-MM-DD H:mm");
  fin = moment(fin, "DD-MM-YYYY").add(1, "days").format("YYYY-MM-DD H:mm");
  var PATTERN = moment(principio, "YYYY-MM-DD").format("YYYY-MM-DD");
  ListaTurnos = [];

  while (moment(principio).isBefore(fin)) {
    ListaTurnos.push(principio);
    principio = moment(principio, "YYYY-MM-DD H:mm")
      .add(emprendimiento.tiempoTurno, "hours")
      .format("YYYY-MM-DD H:mm");
  }
  //Obtenemos horas para campo horas
  horas = ListaTurnos.filter(function (str) {
    return str.indexOf(PATTERN) === 0;
  });
  let horasFormateadas = horas.map(function (element) {
    return (element = moment(element, "YYYY-MM-DD H:mm").format("H:mm"));
  });

  //empezamos a armar la estructura de la tabla
  let x = 0;
  let temp = 24 / emprendimiento.tiempoTurno;
  // Crea las celdas
  for (var i = 0; i < temp; i++) {
    // Crea las hileras de la tabla
    var hilera = document.createElement("tr");
    for (var j = 0; j < 8; j++) {
      var celda = document.createElement("td");
      if (j == 0) {
        var textoCelda = document.createTextNode(horasFormateadas[i]);
      } else {
        var textoCelda = document.createTextNode("");
        celda.setAttribute("id", ListaTurnos[x]);
        x = x + temp;
      }
      celda.appendChild(textoCelda);
      hilera.appendChild(celda);
    }
    x = x - (temp * 7 - 1);
    // agrega la hilera al final de la tabla (al final del elemento tblbody)
    tblBody.appendChild(hilera);
  }
  tabla.appendChild(tblBody);
  tblBody.setAttribute("id", "tableBody");
}

function setSemanas() {
  //Eliminamos tabla si existe
  let tableCuerpo = document.getElementById("tableBody");
  if (tableCuerpo != null) {
    padre = tableCuerpo.parentNode;
    padre.removeChild(tableCuerpo);
  }
  //traemos valor de input date
  let fechaSel = fecha.value;
  fechaSel = moment(fechaSel, "YYYY-MM-DD").format("YYYY-MM-DD H:mm");
  //traemos titulos
  let desde = document.getElementById("desde");
  let hasta = document.getElementById("hasta");
  //calcular dias de semana para restar o sumar
  let diaSelec = moment(fechaSel, "YYYY-MM-DD").day(); // 1 - 7 dependiendo el día
  let desdeDifDias = 1 - diaSelec;
  let hastaDifDias = 7 - diaSelec;
  //Colocamos valores a campos desde y hasta

  let principio = moment(fechaSel, "YYYY-MM-DD")
    .add(desdeDifDias, "days")
    .calendar("DD-MM-YYYY H:mm");
  let fin = moment(fechaSel, "YYYY-MM-DD")
    .add(hastaDifDias, "days")
    .calendar("DD-MM-YYYY H:mm");
  desde.innerHTML = "Desde: " + principio;
  hasta.innerHTML = "Hasta: " + fin;
  generarTabla2(principio, fin);
  bloquerTurnos();
  cargarTurnos(ListaTurnosOcu);
}

function bloquerTurnos() {
  cuerpoTabla = document.getElementById("tableBody");
  if (cuerpoTabla.hasChildNodes()) {
    var children = cuerpoTabla.childNodes;
    for (var i = 0; i < children.length; i++) {
      if (children[i].hasChildNodes()) {
        var children2 = children[i].childNodes;
        for (var j = 0; j < children2.length; j++) {
          //SI id es menor a la hora de inicio y mayor a la hora de cerrar, pintar gris
          hora = moment(children2[j].id, "YYYY-MM-DD H:mm").format("H:mm");
          if (
            moment(hora, "H:mm").isSameOrAfter(
              moment(emprendimiento.horarioDiaNormalFinal, "H:mm")
            ) ||
            moment(hora, "H:mm").isSameOrBefore(
              moment(emprendimiento.horarioDiaNormalInicio, "H:mm")
            )
          ) {
            let celda = document.getElementById(children2[j].id);
            celda.style.backgroundColor = "grey";
            celda.innerHTML = "No disponible";
          }
          //si es domingo no se trabaja
          if (moment(children2[j].id, "YYYY-MM-DD H:mm").day() == 0) {
            let celda = document.getElementById(children2[j].id);
            celda.style.backgroundColor = "grey";
            celda.innerHTML = "No disponible";
          }
        }
      }
    }
  }
}

function cargarTurnos(ListaTurnosOcu) {
  cuerpoTabla = document.getElementById("tableBody");
  console.log(ListaTurnosOcu);
  for (let index = 0; index < ListaTurnosOcu.length; index++) {
    let armarFecha =
      ListaTurnosOcu[index].fecha + " " + ListaTurnosOcu[index].horaTurno;
    let turnoArmado = moment(armarFecha, "DD-MM-YYYY H:mm").format(
      "YYYY-MM-DD H:mm"
    );
    console.log(turnoArmado);

    if (cuerpoTabla.hasChildNodes()) {
      var children = cuerpoTabla.childNodes;
      for (var i = 0; i < children.length; i++) {
        if (children[i].hasChildNodes()) {
          var children2 = children[i].childNodes;
          for (var j = 0; j < children2.length; j++) {
            if (
              moment(children2[j].id, "DD-MM-YYYY H:mm").isSame(
                moment(turnoArmado, "DD-MM-YYYY H:mm")
              )
            ) {
              let celda = document.getElementById(children2[j].id);
              celda.style.backgroundColor = "lightgreen";
              celda.innerHTML = ListaTurnosOcu[index].clienteId;
            }
          }
        }
      }
    }
  }
}
