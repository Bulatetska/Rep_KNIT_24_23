// ignore_for_file: use_build_context_synchronously

import 'package:flutter/material.dart';
import '../services/api_service.dart';

class LoginPage extends StatelessWidget {
  final TextEditingController usernameController = TextEditingController();
  final TextEditingController passwordController = TextEditingController();

  Future<void> loginUser(BuildContext context) async {
    final data = {
      'username': usernameController.text,
      'password': passwordController.text,
    };

    final response = await ApiService.login(data);

    if (response.statusCode == 200) {
      // Успішний вхід
      showDialog(
        context: context,
        builder: (context) => AlertDialog(
          title: const Text('Успішний вхід'),
          content: const Text('Ви успішно увійшли.'),
          actions: [
            TextButton(
              onPressed: () => Navigator.of(context).pop(),
              child: const Text('OK'),
            ),
          ],
        ),
      );
    } else {
      // Помилка при вході
      showDialog(
        context: context,
        builder: (context) => AlertDialog(
          title: const Text('Помилка входу'),
          content: const Text('Невірне ім\'я користувача або пароль.'),
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
        title: const Text('Вхід'),
      ),
      body: Padding(
        padding: const EdgeInsets.all(16.0),
        child: Column(
          children: [
            TextFormField(
              controller: usernameController,
              decoration: const InputDecoration(labelText: 'Ім\'я користувача'),
            ),
            TextFormField(
              controller: passwordController,
              decoration: const InputDecoration(labelText: 'Пароль'),
              obscureText: true,
            ),
            ElevatedButton(
              onPressed: () => loginUser(context),
              child: const Text('Увійти'),
            ),
          ],
        ),
      ),
    );
  }
}
