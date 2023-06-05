// ignore_for_file: use_build_context_synchronously

import 'package:flutter/material.dart';
import 'package:http/http.dart' as http;
import 'dart:convert';
import 'cutomer_profiles.dart';
import 'menu.dart';

class CustomerProfilePage extends StatelessWidget {
  final TextEditingController nameController = TextEditingController();
  final TextEditingController contactController = TextEditingController();
  final TextEditingController projectsController = TextEditingController();
  final TextEditingController certificationsController =
      TextEditingController();
  final TextEditingController salaryController = TextEditingController();
  final TextEditingController descriptionController = TextEditingController();
  final TextEditingController conditionsController = TextEditingController();

  CustomerProfilePage({super.key});

  Future<void> submitForm(BuildContext context) async {
    const url =
        'http://127.0.0.1:8000/customer-profiles'; // Замініть на вірну URL-адресу сервера Python
    final data = {
      'name': nameController.text,
      'contact': contactController.text,
      'projects': projectsController.text,
      'certifications': certificationsController.text,
      'salary': salaryController.text,
      'description': descriptionController.text,
      'conditions': conditionsController.text,
    };

    final response = await http.post(
      Uri.parse(url),
      headers: {
        'Content-Type': 'application/json'
      }, // Додайте заголовок Content-Type
      body: json.encode(data),
    );

    if (response.statusCode == 200) {
      // Успішно збережено
      showDialog(
        context: context,
        builder: (context) => AlertDialog(
          title: const Text('Успішно збережено'),
          content: const Text('Дані клієнта успішно збережені.'),
          actions: [
            TextButton(
              onPressed: () => Navigator.of(context).pop(),
              child: const Text('OK'),
            ),
          ],
        ),
      );
      Navigator.push(
        context,
        MaterialPageRoute(
          builder: (context) => const SavedDataCustomerPage(),
        ),
      );
    } else {
      // Помилка при збереженні
      showDialog(
        context: context,
        builder: (context) => AlertDialog(
          title: const Text('Помилка'),
          content: const Text('Виникла помилка при збереженні даних.'),
          actions: [
            TextButton(
              onPressed: () => Navigator.of(context).pop(),
              child: const Text('OK'),
            ),
          ],
        ),
      );
    }
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: const Text('Клієнтський профіль'),
      ),
      body: Padding(
        padding: const EdgeInsets.all(16.0),
        child: Column(
          children: [
            TextFormField(
              controller: nameController,
              decoration: const InputDecoration(labelText: 'Ім\'я'),
            ),
            TextFormField(
              controller: contactController,
              decoration:
                  const InputDecoration(labelText: 'Контактна інформація'),
            ),
            TextFormField(
              controller: descriptionController,
              decoration: const InputDecoration(labelText: 'Опис'),
            ),
            TextFormField(
              controller: conditionsController,
              decoration: const InputDecoration(labelText: 'Умови'),
            ),
            TextFormField(
              controller: projectsController,
              decoration: const InputDecoration(labelText: 'Проекти'),
              maxLines: null, // Дозволяємо вводити багато рядків
            ),
            TextFormField(
              controller: salaryController,
              decoration: const InputDecoration(labelText: 'Зарплата'),
              maxLines: null, // Дозволяємо вводити багато рядків
            ),
            TextFormField(
              controller: certificationsController,
              decoration: const InputDecoration(labelText: 'Сертифікати'),
              maxLines: null, // Дозволяємо вводити багато рядків
            ),
            ElevatedButton(
              onPressed: () => submitForm(context),
              child: const Text('Save'),
            ),
          ],
        ),
      ),
      drawer: Drawer(
        child: MenuWidget(), // Вставте ваш MenuWidget тут
      ),
    );
  }
}
