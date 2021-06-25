import 'package:flutter/material.dart';
import 'package:flutter_application_1/pages/sub_pages/lista_candidatos.dart';
import 'dart:io';
import 'package:flutter/cupertino.dart';
import 'package:http/http.dart' as http;
import 'dart:async';
import 'dart:convert';
import 'package:image_picker/image_picker.dart';
import 'package:path/path.dart';
import 'package:path_provider/path_provider.dart';

File imagen;
final picker = ImagePicker();

class Validar extends StatefulWidget {
  @override
  _Validar createState() => _Validar();
}

class _Validar extends State<Validar> {
  Future selImagen(context) async {
    var pickedFile;
    pickedFile = await picker.getImage(source: ImageSource.camera);
    setState(() {
      if (pickedFile != null) {
        imagen = File(pickedFile.path);
        print(imagen);
      } else {
        print('No selecciono ninguna imagen');
      }
    });
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
        body: Center(
      child: Column(
        children: <Widget>[
          SizedBox(height: 70.0),
          info(),
          SizedBox(height: 50.0),
          imagen == null
              ? Image.network(
                  "https://cdn.icon-icons.com/icons2/38/PNG/512/explorationoffacerecognition_facescanning_exploraciondereconocimientoderostro_4589.png",
                  height: 220,
                )
              : Image.file(imagen, width: 220, height: 220),
          SizedBox(height: 50.0),
          botonvotar(context),
          SizedBox(height: 20.0),
          comprobar(context),
          SizedBox(height: 150.0),
          retroceder(),
        ],
      ),
    ));
  }

  Widget retroceder() {
    return Align(
      alignment: Alignment.bottomRight,
      child: BackButton(),
    );
  }

  Widget info() {
    return Center(
        child: Text("Reconocimiento Facial",
            style: TextStyle(
                color: Colors.black,
                fontSize: 25.0,
                fontWeight: FontWeight.bold)));
  }

  Widget botonvotar(BuildContext context) {
    return MaterialButton(
        shape: StadiumBorder(),
        highlightColor: Colors.white,
        color: Colors.blueGrey[600],
        onPressed: () {
          selImagen(context);
          //Navigator.push(context,
          //MaterialPageRoute(builder: (context) => Lista_Candidatos()));
        },
        child: Text(
          "Tomar Foto",
          style: TextStyle(fontSize: 20, color: Colors.white),
        ));
  }
}

Widget comprobar(BuildContext context) {
  return MaterialButton(
      shape: StadiumBorder(),
      highlightColor: Colors.white,
      color: Colors.blueGrey[600],
      onPressed: () {
        uploadImage(imagen, context);
      },
      child: Text(
        "Validar",
        style: TextStyle(fontSize: 20, color: Colors.white),
      ));
}

Future uploadImage(doc, context) async {
  final uri = Uri.parse("http://192.168.0.14:8002/upload_reconocedor");
  var request = http.MultipartRequest('POST', uri);
  var pic = await http.MultipartFile.fromPath("file", doc.path);
  request.files.add(pic);
  var response = await request.send();
  if (response.statusCode == 200) {
    response.stream.transform(utf8.decoder).listen((event) {
      if (event == "True") {
        Navigator.push(context,
            MaterialPageRoute(builder: (context) => Lista_Candidatos()));
      }
    });
  } else {
    response.stream.transform(utf8.decoder).listen((event) {
      if (event == "True") {
        Navigator.push(context,
            MaterialPageRoute(builder: (context) => Lista_Candidatos()));
      }
    });
  }
}
