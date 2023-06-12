import 'package:flutter/material.dart';
import 'package:http/http.dart' as http;
import 'dart:convert';

import '../env.sample.dart';
import '../models/user.dart';

class Home extends StatefulWidget {
  const Home({super.key});

  @override
  HomeState createState() => HomeState();
}

class HomeState extends State<Home> {
  late Future<List<User>> userList;
  final userListKey = GlobalKey<HomeState>();

  @override
  void initState() {
    super.initState();
    userList = getUserList();
  }

  Future<List<User>> getUserList() async {
    final url = '${Env.URL_PREFIX}/api/users/';
    final uri = Uri.parse(url);
    final response = await http.get(uri);

    final items = json.decode(response.body).cast<Map<String, dynamic>>();
    List<User> userList = items.map<User>((json) {
      return User.fromJson(json);
    }).toList();

    return userList;
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      key: userListKey,
      appBar: AppBar(
        title: Text('User List'),
      ),
      body: Center(
        child: FutureBuilder<List<User>>(
          future: userList,
          builder: (BuildContext context, AsyncSnapshot snapshot) {
            // By default, show a loading spinner.
            if (!snapshot.hasData) return CircularProgressIndicator();
            // Render user lists
            return ListView.builder(
              itemCount: snapshot.data.length,
              itemBuilder: (BuildContext context, int index) {
                var data = snapshot.data[index];
                return Card(
                  child: ListTile(
                    leading: Icon(Icons.person),
                    title: Text(
                      data.code,
                      style: TextStyle(fontSize: 20),
                    ),
                  ),
                );
              },
            );
          },
        ),
      ),
    );
  }
}