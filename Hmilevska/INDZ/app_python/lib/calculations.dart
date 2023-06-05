import 'package:flutter/material.dart';
import 'package:http/http.dart' as http;
import 'dart:convert';
import 'menu.dart';

class CalculationsPage extends StatefulWidget {
  @override
  _CalculationsPageState createState() => _CalculationsPageState();
}

class _CalculationsPageState extends State<CalculationsPage> {
  Map<String, dynamic>? calculations;

  Future<void> fetchCalculations() async {
    final url = Uri.parse('http://127.0.0.1:8000/calculations'); // Замініть на вірну URL-адресу сервера Python

    final response = await http.get(url);

    if (response.statusCode == 200) {
      final data = json.decode(response.body);
      setState(() {
        calculations = data;
      });
    } else {
      setState(() {
        calculations = null;
      });
    }
  }

  @override
  void initState() {
    super.initState();
    fetchCalculations();
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: const Text('Обрахунки'),
      ),
      body: calculations != null
          ? ListView(
              padding: const EdgeInsets.all(16.0),
              children: [
                ListTile(
                  title: const Text('Загальна кількість профілів'),
                  subtitle: Text('${calculations!['total_profiles']}'),
                ),
                ListTile(
                  title: const Text('Загальний рейтинг'),
                  subtitle: Text('${calculations!['total_rating']}'),
                ),
                ListTile(
                  title: const Text('Середній рейтинг'),
                  subtitle: Text('${calculations!['average_rating']}'),
                ),
                ListTile(
                  title: const Text('Мінімальний рейтинг'),
                  subtitle: Text('${calculations!['min_rating']}'),
                ),
                ListTile(
                  title: const Text('Максимальний рейтинг'),
                  subtitle: Text('${calculations!['max_rating']}'),
                ),
                ...calculations!['category_ratings'].entries.map((entry) => ListTile(
                  title: Text('Рейтинг категорії "${entry.key}"'),
                  subtitle: Text('${entry.value['total_rating']}'),
                )),
                ...calculations!['category_min_profiles'].entries.map((entry) => ListTile(
                  title: Text('Профіль з мінімальним рейтингом в категорії "${entry.key}"'),
                  subtitle: Text('${entry.value['name']}'),
                )),
                ...calculations!['category_max_profiles'].entries.map((entry) => ListTile(
                  title: Text('Профіль з максимальним рейтингом в категорії "${entry.key}"'),
                  subtitle: Text('${entry.value['name']}'),
                )),
              ],
            )
          : const Center(
              child: CircularProgressIndicator(),
            ),
      drawer: Drawer(
        child: MenuWidget(),
      ),
    );
  }
}
