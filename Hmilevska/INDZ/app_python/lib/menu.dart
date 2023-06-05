// ignore_for_file: library_private_types_in_public_api

import 'package:flutter/material.dart';
import 'package:http/http.dart' as http;
import 'dart:convert';

class MenuItem {
  final String title;
  final String link;

  MenuItem({required this.title, required this.link});
}

class MenuWidget extends StatefulWidget {
  @override
  _MenuWidgetState createState() => _MenuWidgetState();
}

class _MenuWidgetState extends State<MenuWidget> {
  List<MenuItem> menuItems = [];

  @override
  void initState() {
    super.initState();
    fetchData();
  }

  void fetchData() async {
    var url = 'http://127.0.0.1:8000/menu'; // Вставте свій URL сервера Python
    var response = await http.get(Uri.parse(url));

    if (response.statusCode == 200) {
      var data = jsonDecode(response.body);
      List<MenuItem> items = [];

      for (var item in data) {
        var menuItem = MenuItem(
          title: item['title'],
          link: item['link'],
        );
        items.add(menuItem);
      }

      setState(() {
        menuItems = items;
      });
    }
  }

  @override
  Widget build(BuildContext context) {
    return ListView.builder(
      itemCount: menuItems.length,
      itemBuilder: (context, index) {
        var menuItem = menuItems[index];
        return ListTile(
          title: Text(menuItem.title),
          onTap: () {
        Navigator.pushNamed(context, menuItem.link);

          },
        );
      },
    );
  }
}
