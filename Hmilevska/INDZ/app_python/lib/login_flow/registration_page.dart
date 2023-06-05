// ignore_for_file: use_build_context_synchronously

import 'package:flutter/material.dart';
import '../services/api_service.dart';

class RegistrationPage extends StatelessWidget {
  final TextEditingController emailController = TextEditingController();
  final TextEditingController usernameController = TextEditingController();
  final TextEditingController passwordController = TextEditingController();
  final List<String> roles = ['Student', 'Employer'];
  String selectedRole = 'Student';

  RegistrationPage({Key? key}) : super(key: key);

  Future<void> registerUser(BuildContext context) async {
    final data = {
      'email': emailController.text,
      'username': usernameController.text,
      'password': passwordController.text,
      'role': selectedRole,
    };

    final response = await ApiService.register(data);

    if (response.statusCode == 200) {
      // Успішна реєстрація
      showDialog(
        context: context,
        builder: (context) => AlertDialog(
          title: const Text('Успішна реєстрація'),
          content: const Text('Ви успішно зареєстровані.'),
          actions: [
            TextButton(
              onPressed: () => Navigator.of(context).pop(),
              child: const Text('OK'),
            ),
          ],
        ),
      );
    } else {
      // Помилка при реєстрації
      showDialog(
        context: context,
        builder: (context) => AlertDialog(
          title: const Text('Помилка реєстрації'),
          content: const Text('Виникла помилка при реєстрації.'),
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
        title: const Text('Реєстрація'),
      ),
      body: Padding(
        padding: const EdgeInsets.all(16.0),
        child: Column(
          children: [
            TextFormField(
              controller: emailController,
              decoration: const InputDecoration(labelText: 'Електронна пошта'),
            ),
            TextFormField(
              controller: usernameController,
              decoration: const InputDecoration(labelText: 'Ім\'я користувача'),
            ),
            TextFormField(
              controller: passwordController,
              decoration: const InputDecoration(labelText: 'Пароль'),
              obscureText: true,
            ),
            DropdownButtonFormField<String>(
              value: selectedRole,
              items: roles.map((role) {
                return DropdownMenuItem<String>(
                  value: role,
                  child: Text(role),
                );
              }).toList(),
              onChanged: (value) {
                selectedRole = value!;
              },
              decoration: const InputDecoration(labelText: 'Роль'),
            ),
            ElevatedButton(
              onPressed: () => registerUser(context),
              child: const Text('Зареєструватися'),
            ),
          ],
        ),
      ),
    );
  }
}
