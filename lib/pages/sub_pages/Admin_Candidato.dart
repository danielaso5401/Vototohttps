import 'dart:io';
import 'package:flutter/material.dart';
import 'package:flutter/cupertino.dart';
import 'package:http/http.dart' as http;
import 'dart:async';
import 'dart:convert';
import 'package:image_picker/image_picker.dart';
import 'package:path/path.dart';
import 'package:path_provider/path_provider.dart';

final f_nombre = TextEditingController();
final f_partido = TextEditingController();
final f_dni = TextEditingController();
String fotocand;
String fotopart;
File imagen;
final picker = ImagePicker();
File imagen2;
final picker2 = ImagePicker();

class Admin_Candidato extends StatefulWidget {
  @override
  _Admin_Candidato createState() => _Admin_Candidato();
}

class _Admin_Candidato extends State<Admin_Candidato> {
  Future selImagen(op, context) async {
    var pickedFile;
    if (op == 1) {
      pickedFile = await picker.getImage(source: ImageSource.camera);
    } else {
      pickedFile = await picker.getImage(source: ImageSource.gallery);
    }
    setState(() {
      if (pickedFile != null) {
        imagen = File(pickedFile.path);
        print(imagen);
      } else {
        print('No selecciono ninguna imagen');
      }
    });

    Navigator.of(context).pop();
  }

  Future selImagen2(op, context) async {
    var pickedFile;
    if (op == 1) {
      pickedFile = await picker2.getImage(source: ImageSource.camera);
    } else {
      pickedFile = await picker2.getImage(source: ImageSource.gallery);
    }
    setState(() {
      if (pickedFile != null) {
        imagen2 = File(pickedFile.path);
        print(imagen2);
      } else {
        print('No selecciono ninguna imagen');
      }
    });

    Navigator.of(context).pop();
  }

  opciones(context) {
    showDialog(
        context: context,
        builder: (BuildContext context) {
          return AlertDialog(
            contentPadding: EdgeInsets.all(0),
            content: SingleChildScrollView(
              child: Column(
                children: [
                  InkWell(
                    onTap: () {
                      selImagen(1, context);
                    },
                    child: Container(
                      padding: EdgeInsets.all(20),
                      decoration: BoxDecoration(
                          border: Border(
                              bottom:
                                  BorderSide(width: 1, color: Colors.grey))),
                      child: Row(
                        children: [
                          Expanded(
                              child: Text(
                            'Tomar una foto',
                            style: TextStyle(fontSize: 16),
                          )),
                          Icon(Icons.camera_alt, color: Colors.blue)
                        ],
                      ),
                    ),
                  ),
                  InkWell(
                    onTap: () {
                      selImagen(2, context);
                    },
                    child: Container(
                      padding: EdgeInsets.all(20),
                      child: Row(
                        children: [
                          Expanded(
                              child: Text(
                            'Seleccionar una foto',
                            style: TextStyle(fontSize: 16),
                          )),
                          Icon(Icons.image, color: Colors.blue)
                        ],
                      ),
                    ),
                  ),
                ],
              ),
            ),
          );
        });
  }

  opciones2(context) {
    showDialog(
        context: context,
        builder: (BuildContext context) {
          return AlertDialog(
            contentPadding: EdgeInsets.all(0),
            content: SingleChildScrollView(
              child: Column(
                children: [
                  InkWell(
                    onTap: () {
                      selImagen2(1, context);
                    },
                    child: Container(
                      padding: EdgeInsets.all(20),
                      decoration: BoxDecoration(
                          border: Border(
                              bottom:
                                  BorderSide(width: 1, color: Colors.grey))),
                      child: Row(
                        children: [
                          Expanded(
                              child: Text(
                            'Tomar una foto',
                            style: TextStyle(fontSize: 16),
                          )),
                          Icon(Icons.camera_alt, color: Colors.blue)
                        ],
                      ),
                    ),
                  ),
                  InkWell(
                    onTap: () {
                      selImagen2(2, context);
                    },
                    child: Container(
                      padding: EdgeInsets.all(20),
                      child: Row(
                        children: [
                          Expanded(
                              child: Text(
                            'Seleccionar una foto',
                            style: TextStyle(fontSize: 16),
                          )),
                          Icon(Icons.image, color: Colors.blue)
                        ],
                      ),
                    ),
                  ),
                ],
              ),
            ),
          );
        });
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        backgroundColor: Colors.blueGrey[300],
        title: const Text('Registro de Candidatos',
            style: TextStyle(color: Colors.white)),
      ),
      body: ListView(
        children: [
          Image.network(
            "https://cdn.icon-icons.com/icons2/624/PNG/512/Add_User-80_icon-icons.com_57380.png",
            height: 140,
          ),
          Padding(
            padding: EdgeInsets.all(20),
            child: Column(
              children: [
                registro_candidato(),
                FlatButton(
                    shape: StadiumBorder(),
                    color: Colors.blueGrey[600],
                    onPressed: () {
                      opciones(context);
                    },
                    child: Text('Foto del Candidato',
                        style: TextStyle(fontSize: 17, color: Colors.white))),
                imagen == null
                    ? Center()
                    : Image.file(imagen, width: 220, height: 220),
                SizedBox(height: 30),
                FlatButton(
                    shape: StadiumBorder(),
                    color: Colors.blueGrey[600],
                    onPressed: () {
                      opciones2(context);
                    },
                    child: Text('Foto del Partido',
                        style: TextStyle(fontSize: 17, color: Colors.white))),
                imagen2 == null
                    ? Center()
                    : Image.file(imagen2, width: 220, height: 220),
                SizedBox(height: 30),
                //guardar(),
                //SizedBox(height: 10),
                //enviar(imagen, imagen2),
                Row(
                  children: [
                    Padding(
                      padding: EdgeInsets.only(
                        top: 5,
                        left: 60,
                        right: 10,
                      ),
                    ),
                    Center(
                      child: guardar(),
                    ),
                    Center(
                      child: enviar(imagen, imagen2),
                    )
                  ],
                ),
              ],
            ),
          ),
        ],
      ),
    );
  }
}

Widget registro_candidato() {
  return Container(
    child: Center(
      child: Column(
        mainAxisAlignment: MainAxisAlignment.center,
        children: <Widget>[
          nom_cand(),
          nom_part_pol(),
          num_dni(),
          SizedBox(
            height: 10,
          ),
        ],
      ),
    ),
  );
}

Widget nom_cand() {
  return Container(
    padding: EdgeInsets.symmetric(horizontal: 50, vertical: 10),
    child: TextField(
      style: TextStyle(color: Colors.white),
      controller: f_nombre,
      decoration: InputDecoration(
        hintText: "Nombre del candidato",
        fillColor: Colors.blueGrey[600],
        filled: true,
        hintStyle: TextStyle(color: Colors.white),
      ),
    ),
  );
}

Widget nom_part_pol() {
  return Container(
    padding: EdgeInsets.symmetric(horizontal: 50, vertical: 10),
    child: TextField(
      style: TextStyle(color: Colors.white),
      controller: f_partido,
      decoration: InputDecoration(
        hintText: "Nombre del Partido",
        fillColor: Colors.blueGrey[600],
        filled: true,
        hintStyle: TextStyle(color: Colors.white),
      ),
    ),
  );
}

Widget num_dni() {
  return Container(
    padding: EdgeInsets.symmetric(horizontal: 50, vertical: 10),
    child: TextField(
      style: TextStyle(color: Colors.white),
      controller: f_dni,
      decoration: InputDecoration(
        hintText: "DNI",
        fillColor: Colors.blueGrey[600],
        filled: true,
        hintStyle: TextStyle(color: Colors.white),
      ),
    ),
  );
}

Widget guardar() {
  return RaisedButton(
      shape: StadiumBorder(),
      color: Colors.blueGrey[600],
      padding: EdgeInsets.symmetric(horizontal: 10, vertical: 10),
      onPressed: () {
        uploadImage();
        uploadImage2();
      },
      child: Text(
        "Cargar",
        style: TextStyle(fontSize: 17, color: Colors.white),
      ));
}

Widget enviar(imagen, imagen2) {
  return RaisedButton(
      shape: StadiumBorder(),
      color: Colors.blueGrey[600],
      padding: EdgeInsets.symmetric(horizontal: 10, vertical: 10),
      onPressed: () {
        String c_nombre = f_nombre.text;
        String c_partido = f_partido.text;
        String c_dni = f_dni.text;
        ingresar_candidato(c_nombre, c_partido, fotocand, fotopart, c_dni);
      },
      child: Text(
        "Guardar",
        style: TextStyle(fontSize: 17, color: Colors.white),
      ));
}

void ingresar_candidato(nombre, partido, fotocan, fotopar, dnipar) async {
  //var url = Uri.parse('http://127.0.0.1:8002/create_usuario');
  //var url = Uri.parse('http://192.168.0.14:8002/create_usuario');
  var url = Uri.parse('http://192.168.0.14:8002/create_candidato');

  var response = await http.post(url,
      headers: {
        "content-type": "application/json",
      },
      body: jsonEncode({
        "candidato_name": nombre,
        "candidato_dni": dnipar,
        "candidato_partpol": partido,
        "candidato_fotocant": fotocan,
        "candidato_fotopart": fotopar
      }));
}

Future uploadImage() async {
  final uri = Uri.parse("http://192.168.0.14:8002/upload");

  var request = http.MultipartRequest('POST', uri);
  var pic = await http.MultipartFile.fromPath("file", imagen.path);
  request.files.add(pic);
  var response = await request.send();

  if (response.statusCode == 200) {
    response.stream.transform(utf8.decoder).listen((event) {
      fotocand = event;
    });
    print("imagen cargad");
  } else {
    print("error");
  }
}

Future uploadImage2() async {
  final uri = Uri.parse("http://192.168.0.14:8002/upload");

  var request = http.MultipartRequest('POST', uri);
  var pic = await http.MultipartFile.fromPath("file", imagen2.path);
  request.files.add(pic);
  var response = await request.send();

  if (response.statusCode == 200) {
    response.stream.transform(utf8.decoder).listen((event) {
      fotopart = event;
    });
    print("imagen cargad");
  } else {
    print("error");
  }
}
