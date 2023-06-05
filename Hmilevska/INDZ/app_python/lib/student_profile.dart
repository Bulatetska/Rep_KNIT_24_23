// ignore_for_file: use_build_context_synchronously

import 'package:app_python/profiles.dart';
import 'package:flutter/material.dart';
import 'package:http/http.dart' as http;
import 'dart:convert';
import 'menu.dart';

class StudentProfilePage extends StatelessWidget {
  final TextEditingController nameController = TextEditingController();
  final TextEditingController educationController = TextEditingController();
  final TextEditingController skillsController = TextEditingController();
  final TextEditingController experienceController = TextEditingController();
  final TextEditingController contactController = TextEditingController();
  final TextEditingController projectsController = TextEditingController();
  final TextEditingController achievementsController = TextEditingController();
  final TextEditingController certificationsController =
      TextEditingController();
  final TextEditingController ratingController = TextEditingController();
  final TextEditingController categoryController = TextEditingController();

  StudentProfilePage({super.key});

  Future<void> submitForm(BuildContext context) async {
    const url =
        'http://127.0.0.1:8000/profiles'; // Замініть на вірну URL-адресу сервера Python

    final data = {
      'name': nameController.text,
      'contact': contactController.text,
      'education': educationController.text,
      'skills': skillsController.text,
      'experience': experienceController.text,
      'projects': projectsController.text,
      'achievements': achievementsController.text,
      'certifications': certificationsController.text,
      'rating': int.parse(ratingController.text),
      'category': categoryController.text,
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
          content: const Text('Дані студента успішно збережені.'),
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
          builder: (context) => const SavedDataPage(),
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
        title: const Text('Студентський профіль'),
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
              controller: educationController,
              decoration: const InputDecoration(labelText: 'Освіта'),
            ),
            TextFormField(
              controller: skillsController,
              decoration: const InputDecoration(labelText: 'Навички'),
            ),
            TextFormField(
              controller: experienceController,
              decoration: const InputDecoration(labelText: 'Досвід'),
            ),
            TextFormField(
              controller: projectsController,
              decoration: const InputDecoration(labelText: 'Проекти'),
              maxLines: null, // Дозволяємо вводити багато рядків
            ),
            TextFormField(
              controller: achievementsController,
              decoration: const InputDecoration(labelText: 'Досягнення'),
              maxLines: null, // Дозволяємо вводити багато рядків
            ),
            TextFormField(
              controller: certificationsController,
              decoration: const InputDecoration(labelText: 'Сертифікати'),
              maxLines: null, // Дозволяємо вводити багато рядків
            ),
            TextFormField(
              controller: ratingController,
              decoration: const InputDecoration(labelText: 'Рейтинг'),
            ),
            TextFormField(
              controller: categoryController,
              decoration: const InputDecoration(labelText: 'Категорія'),
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
