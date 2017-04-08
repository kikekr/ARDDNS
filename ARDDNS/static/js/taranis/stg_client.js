/*
  Obtiene la fecha en formato iberdrola
*/
function getIbeDate(normal_date){
  if (normal_date == null){
    date = new Date();
  }else{
    date = new Date(normal_date);
  }
  //Obtenemos el año
  ibedate= date.getFullYear().toString();
  //El mes
  ibedate += ("0" + (date.getUTCMonth() + 1)).slice(-2);
  //El día
  ibedate += ("0" + (date.getUTCDate())).slice(-2);
  //Hora
  ibedate += ("0" + (date.getHours())).slice(-2);
  //Minutos
  ibedate += ("0" + (date.getUTCMinutes())).slice(-2);
  //Segundos
  ibedate += ("0" + (date.getUTCSeconds())).slice(-2);
  //Millisegundos
  ibedate += ("0" + (date.getUTCMilliseconds())).slice(-2);
  ibedate += '0';
  if (date.getTimezoneOffset() == -60 ){
    ibedate += 'W';
  }else{
    ibedate += 'S';
  }
  return ibedate
}

/*
  Obtiene la fecha en formato estandar
*/
function getIbeToDate(ibe_date){
  yyyy = ibe_date.substring(0,4);
  MM = ibe_date.substring(4,6);
  dd = ibe_date.substring(6,8);
  hh = ibe_date.substring(8,10);
  mm = ibe_date.substring(10,12);
  ss = ibe_date.substring(12,14);
  normal_date = yyyy+"/"+MM+"/"+dd+" "+hh+":"+mm+":"+ss;
  date = new Date(normal_date);
  return date;
}

function getLastWeek(){
    var today = new Date();
    var lastWeek = new Date(today.getFullYear(), today.getMonth(), today.getDate() - 7);
    return lastWeek ;
}
function getLastMonth(){
    var today = new Date();
    var lastWeek = new Date(today.getFullYear(), today.getMonth()-1, today.getDate());
    return lastWeek ;
}
/*
  get_report: devuelve json con info de request
*/
function get_report(report_type,json,callback){
    $.post("/reports/make/"+report_type+"/",JSON.stringify(json),callback)
    .fail(function(xhr, status, error) {
        console.log(error);
    });;
}
/*
  send_order: devuelve json con info de request
*/
function send_order(order_type,json,callback){
    $.post("/orders/make/"+order_type+"/",JSON.stringify(json),callback)
    .fail(function(xhr, status, error) {
        console.log(error);
    });;
}

/*
  get_request: devuelve información de request con id_request
*/
function get_request(id_request,callback){
  $.get("/request/"+id_request+"/",callback);
}

/*
  get_events: devuelve información de los eventos del usuario
*/
function get_events(id_request,callback){
  $.get("/events/",callback);
}

/*
  get_last_request: devuelve información de la última request con id_request
*/
function get_last_request(nada,callback){
  $.get("/request/last",callback);
}

/*
  Petición S01
*/
function getS01(dc_sn,id_meter,priority,callback){
  if (dc_sn != null){
    status = -1;
    json = { "priority":priority,
    "dc_sn":dc_sn}
  }else{
    status = -1;
    json = { "priority":priority,
    "pk_list":[id_meter]}
  }
  get_report("S01",json,callback);
}
/*
  Petición S02
*/
function getS02(dc_sn,priority,tfStart,tfEnd,callback){
  status = -1;
  fh_start = getIbeDate(tfStart);
  fh_end = getIbeDate(tfEnd);
  json = { "priority":priority,
  "dc_sn":dc_sn,
  "tfStart" : fh_start,
  "tfEnd": fh_end}
  get_report("S02",json,callback);
}
/*
  Petición S03
*/
function getS03(dc_sn,priority,tfStart,tfEnd,callback){
  status = -1;
  fh_start = getIbeDate(tfStart);
  fh_end = getIbeDate(tfEnd);
  json = { "priority":priority,
  "dc_sn":dc_sn,
  "tfStart" : fh_start,
  "tfEnd": fh_end}
  get_report("S03",json,callback);
}
/*
  Petición S04
*/
function getS04(dc_sn,priority,tfStart,tfEnd,callback){
  status = -1;
  fh_start = getIbeDate(tfStart);
  fh_end = getIbeDate(tfEnd);
  json = { "priority":priority,
  "dc_sn":dc_sn,
  "tfStart" : fh_start,
  "tfEnd": fh_end}
  get_report("S04",json,callback);
}
/*
  Petición S05
*/
function getS05(dc_sn,priority,tfStart,tfEnd,callback){
  status = -1;
  fh_start = getIbeDate(tfStart);
  fh_end = getIbeDate(tfEnd);
  json = { "priority":priority,
  "dc_sn":dc_sn,
  "tfStart" : fh_start,
  "tfEnd": fh_end}
  get_report("S05",json,callback);
}
/*
  Petición S06
*/
function getS06(dc_sn,id_meter,priority,callback){
  if (dc_sn != null){
    status = -1;
    json = { "priority":priority,
    "dc_sn":dc_sn}
  }else{
    status = -1;
    json = { "priority":priority,
    "pk_list":[id_meter]}
  }
  get_report("S06",json,callback);
}

/*
  Petición S07
*/
function getS07(dc_sn,priority,tfStart,tfEnd,callback){
  status = -1;
  fh_start = getIbeDate(tfStart);
  fh_end = getIbeDate(tfEnd);
  json = { "priority":priority,
  "dc_sn":dc_sn,
  "tfStart" : fh_start,
  "tfEnd": fh_end}
  get_report("S02",json,callback);
}
/*
  Petición S08
*/
function getS08(dc_sn,priority,tfStart,tfEnd,callback){
  status = -1;
  fh_start = getIbeDate(tfStart);
  fh_end = getIbeDate(tfEnd);
  json = { "priority":priority,
  "dc_sn":dc_sn,
  "tfStart" : fh_start,
  "tfEnd": fh_end}
  get_report("S02",json,callback);
}
/*
  Petición S09
*/
function getS09(id_meter,priority,tfStart,tfEnd,queryID,Parameters,callback){
  status = -1;
  fh_start = getIbeDate(tfStart);
  fh_end = getIbeDate(tfEnd);
  json = { "priority":priority,
  "pk_list":[id_meter],
  "tfStart" : fh_start,
  "tfEnd": fh_end,
  "QueryID": queryID,
  "Parameters": parameters}
  get_report("S09",json,callback);
}
/*
  Petición S17
*/
function getS17(id_meter,priority,tfStart,tfEnd,queryID,Parameters,callback){
  status = -1;
  fh_start = getIbeDate(tfStart);
  fh_end = getIbeDate(tfEnd);
  json = { "priority":priority,
  "dc_sn":dc_sn,
  "tfStart" : fh_start,
  "tfEnd": fh_end,
  "QueryID": queryID,
  "Parameters": parameters}
  get_report("S17",json,callback);
}
/*
  Petición S18
*/
function getS18(dc_sn,id_meter,priority,callback){
  if (dc_sn != null){
    status = -1;
    json = { "priority":priority,
    "dc_sn":dc_sn}
  }else{
    status = -1;
    json = { "priority":priority,
    "pk_list":[id_meter]}
  }
  get_report("S18",json,callback);
}
/*
  Petición S06
*/
function getS23(id_meter,priority,callback){
  status = -1;
  json = { "priority":priority,
  "pk_list":[id_meter]}
  get_report("S23",json,callback);
}

/*
  Corte/Reconexión B03
*/
function sendB03(meter_sn,priority,Fini,Ffin,state,callback){
  json = {
    "priority": priority,
    "meters":[
        meter_sn
    ],
    "Fini": Fini,
    "Ffin": Ffin,
    "Order": state
  }
  send_order("B03",json,callback);
}
