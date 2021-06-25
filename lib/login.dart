import 'package:flutter/cupertino.dart';
import 'package:flutter/material.dart';
import 'package:flutter_application_1/pages/Admin.dart';
import 'package:flutter_application_1/pages/Visitante.dart';
import 'package:http/http.dart' as http;
import 'dart:async';
import 'dart:convert';

class Login extends StatelessWidget {
  //const Login({Key key}) : super(key: key);
  @override
  Widget build(BuildContext context) {
    return Scaffold();
  }

  Widget titulo() {
    return Image.network(
      'https://i.ibb.co/QX5cbMK/logo.png',
      width: 120,
      height: 120,
    );
  }

  Widget nombre() {
    return Text("Ingresar",
        style: TextStyle(
            color: Colors.black, fontSize: 35.0, fontWeight: FontWeight.bold));
  }

  Widget campousuario(usuario) {
    return Container(
      padding: EdgeInsets.symmetric(horizontal: 50, vertical: 10),
      child: TextField(
        style: TextStyle(color: Colors.white),
        controller: usuario,
        decoration: InputDecoration(
          hintText: "usuario",
          fillColor: Colors.blueGrey[600],
          filled: true,
          hintStyle: TextStyle(color: Colors.white),
        ),
      ),
    );
  }

  Widget campocontrasena(password) {
    return Container(
      padding: EdgeInsets.symmetric(horizontal: 50, vertical: 10),
      child: TextField(
        style: TextStyle(color: Colors.white),
        controller: password,
        obscureText: true,
        decoration: InputDecoration(
          hintText: "password",
          fillColor: Colors.blueGrey[600],
          filled: true,
          hintStyle: TextStyle(color: Colors.white),
        ),
      ),
    );
  }

  Widget botonentrar(usu, pas, usuario, password, BuildContext context) {
    return RaisedButton(
        shape: StadiumBorder(),
        highlightColor: Colors.white,
        color: Colors.blueGrey[600],
        padding: EdgeInsets.symmetric(horizontal: 10, vertical: 10),
        onPressed: () {
          usu = usuario.text;
          pas = password.text;
          print(usu);
          print(pas);
          login(usu, pas, context);
        },
        child: Text(
          "Ingresar",
          style: TextStyle(fontSize: 20, color: Colors.white),
        ));
  }
}

Future login(usu, pas, context) async {
  var url = Uri.parse("http://192.168.0.14:8002/login");
  var response = await http.post(url,
      headers: {
        "content-type": "application/json",
      },
      body: jsonEncode({"usuario": usu, "contraseña": pas}));
  Map<String, dynamic> json = jsonDecode(response.body);
  int rol = json['idRoldes'];
  if (rol == 1) {
    Navigator.push(context, MaterialPageRoute(builder: (context) => Admin()));
  } else if (rol == 4) {
    Navigator.push(
        context, MaterialPageRoute(builder: (context) => Visitante()));
  } else {
    print("error");
  }

  //Navigator.push(context, MaterialPageRoute(builder: (context) => Admin()));
}
