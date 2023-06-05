// ignore_for_file: library_private_types_in_public_api

import 'package:flutter/material.dart';
import 'package:http/http.dart' as http;
import 'dart:convert';
import 'menu.dart';

class SavedDataCustomerPage extends StatefulWidget {
  const SavedDataCustomerPage({super.key});

  @override
  _SavedDataCustomerPageState createState() => _SavedDataCustomerPageState();
}

class _SavedDataCustomerPageState extends State<SavedDataCustomerPage> {
  List<dynamic> savedData = [];

  @override
  void initState() {
    super.initState();
    fetchSavedData();
  }

  Future<void> fetchSavedData() async {
    const url =
        'http://127.0.0.1:8000/customer-profiles'; // Замініть на вірну URL-адресу сервера Python
    final response = await http.get(Uri.parse(url));

    if (response.statusCode == 200) {
      setState(() {
        savedData = json.decode(response.body);
      });
    }
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: const Text('Збережені дані клієнтів'),
      ),
      body: ListView.builder(
        itemCount: savedData.length,
        itemBuilder: (context, index) {
          final data = savedData[index];
          return ListTile(
            title: Text('Ім\'я: ${data['name']}'),
            subtitle: Column(
              crossAxisAlignment: CrossAxisAlignment.start,
              children: [
                Text('Контактна інформація: ${data['contact']}'),
                Text('Проекти: ${data['projects']}'),
                Text('Сертифікати: ${data['certifications']}'),
                Text('Зарплатня: ${data['salary']}'),
                Text('Опис: ${data['description']}'),
                Text('Умови: ${data['conditions']}'),
              ],
            ),
          );
        },
      ),
            drawer: Drawer(
        child: MenuWidget(), // Вставте ваш MenuWidget тут
      ),
    );
  }
}
