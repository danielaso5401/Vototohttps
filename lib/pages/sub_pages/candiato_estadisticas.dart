import 'dart:convert';
import 'package:flutter/material.dart';
import 'package:http/http.dart' as http;

import 'candidato.dart';

class Lista_estadisticas extends StatefulWidget {
  @override
  _Lista_estadisticas createState() => _Lista_estadisticas();
}

class _Lista_estadisticas extends State<Lista_estadisticas> {
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
      ])));
    }
    return candi;
  }
}
