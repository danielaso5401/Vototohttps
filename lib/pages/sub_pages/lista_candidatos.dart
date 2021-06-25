import 'dart:convert';

import 'package:flutter/material.dart';
import 'package:flutter_application_1/pages/sub_pages/Listvotocandidato.dart';
import 'package:flutter_application_1/pages/sub_pages/candidato.dart';
import 'package:flutter_application_1/pages/sub_pages/sub_sub_pages/Confirmarvoto.dart';
import 'package:http/http.dart' as http;

class Lista_Candidatos extends StatefulWidget {
  @override
  _Lista_Candidatos createState() => _Lista_Candidatos();
}

class _Lista_Candidatos extends State<Lista_Candidatos> {
  Future<List<Candidato>> _listadoCandidato;
  Future<List<Candidato>> _getCandidatos() async {
    var url = Uri.parse("http://192.168.0.14:8002/get_candidato");
    final respuesta = await http.get(url);
    List<Candidato> cand = [];
    if (respuesta.statusCode == 200) {
      String cuerpo = utf8.decode(respuesta.bodyBytes);
      final jasodata = jsonDecode(cuerpo);
      for (var i in jasodata) {
        cand.add(Candidato(
            i["candidato_name"],
            i["candidato_dni"],
            i["candidato_partpol"],
            i["candidato_fotocant"],
            i["candidato_fotopart"],
            i["idCandidato"]));
      }
      return cand;
    } else {
      throw Exception("Fallo la conexion");
    }
  }

  @override
  void initState() {
    super.initState();
    _listadoCandidato = _getCandidatos();
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        backgroundColor: Colors.blueGrey[300],
        title: Text("Lista de candidatos"),
      ),
      body: FutureBuilder(
        future: _listadoCandidato,
        builder: (context, snapshot) {
          if (snapshot.hasData) {
            return ListView(
              children: lista(snapshot.data),
            );
          } else if (snapshot.hasError) {
            print(snapshot.error);
            return Text("error");
          }
          return Center(
            child: CircularProgressIndicator(),
          );
        },
      ),
    );
  }

  List<Widget> lista(List<Candidato> data) {
    List<Widget> candi = [];
    for (var i in data) {
      candi.add(Card(
          child: Column(children: [
        Row(mainAxisAlignment: MainAxisAlignment.spaceEvenly,
            //padding: EdgeInsets.all(20.0),
            children: [
              Expanded(
                child: Image.network(
                    "http://192.168.0.14:8002/uploads/" + i.fotocand,
                    height: 300,
                    width: 300),
              ),
              Expanded(
                child: Image.network(
                    "http://192.168.0.14:8002/uploads/" + i.fotopart,
                    height: 300,
                    width: 300),
              )
            ]),
        Padding(
          padding: const EdgeInsets.all(8.0),
          child: Text(
              "Candidato:  " + i.name + "\nPartido Politico: " + i.partido,
              style: TextStyle(
                  color: Colors.black,
                  fontSize: 20.0,
                  fontWeight: FontWeight.bold)),
        ),
        Column(
          children: [
            FlatButton(
                shape: StadiumBorder(),
                color: Colors.blueGrey[600],
                onPressed: () {
                  ingresar_voto(i.id);
                  Navigator.push(context,
                      MaterialPageRoute(builder: (context) => Confirmavoto()));
                },
                child: Text(
                  "Votar",
                  style: TextStyle(fontSize: 20, color: Colors.white),
                ))
          ],
        ),
      ])));
    }
    return candi;
  }
}

void ingresar_voto(id_elector) async {
  //var url = Uri.parse('http://127.0.0.1:8002/create_usuario');
  //var url = Uri.parse('http://192.168.0.14:8002/create_usuario');
  var url = Uri.parse('http://192.168.0.14:8002/create_voto');

  var response = await http.post(url,
      headers: {
        "content-type": "application/json",
      },
      body: jsonEncode({
        "elector_idElector": 1,
        "candidato_idCandidato": id_elector,
      }));
}
