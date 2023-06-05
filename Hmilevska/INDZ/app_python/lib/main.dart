import 'package:app_python/calculations.dart';
import 'package:app_python/customer_profile.dart';
import 'package:app_python/cutomer_profiles.dart';
import 'package:flutter/material.dart';
import 'package:http/http.dart' as http;
import 'menu.dart';
import 'student_profile.dart';
import 'profiles.dart';
import 'login_flow/login_page.dart';
import 'login_flow/registration_page.dart';
import 'utils/theme_switcher.dart';

class MyPage extends StatefulWidget {
  @override
  _MyPageState createState() => _MyPageState();
}

class _MyPageState extends State<MyPage> {
  String _response = '';

  void _fetchData() async {
    var url = 'http://127.0.0.1:8000/'; // Вставте свій URL сервера Python
    var response = await http.get(Uri.parse(url));

    setState(() {
      _response = response.body;
    });
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: const Text('Flutter + Python'),
        actions: [
          IconButton(
            icon: Icon(Icons.lightbulb),
            onPressed: () {
              // Викликаємо функцію для зміни теми
              ThemeSwitcher.of(context).switchTheme();
            },
          ),
          const SizedBox(width: 16),
        ],
      ),
      drawer: Drawer(
        child: MenuWidget(), // Вставте ваш MenuWidget тут
      ),
      body: Center(
        child: Column(
          mainAxisAlignment: MainAxisAlignment.center,
          children: [
            ElevatedButton(
              onPressed: _fetchData,
              child: const Text('Отримати текст з Python'),
            ),
            const SizedBox(height: 16),
            const Text('Відповідь від сервера:'),
            Text(_response),
          ],
        ),
      ),
    );
  }
}

void main() {
  runApp(
    ThemeSwitcher(
      child: MyApp(),
    ),
  );
}

class MyApp extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      home: MyPage(),
      theme: ThemeData.light(), // Light theme by default
      darkTheme: ThemeData.dark(), // Dark theme by default
      builder: (context, child) {
        return ThemeSwitcher.of(context).isDarkModeEnabled
            ? MaterialApp(
                theme: ThemeData.dark(),
                home: child,
              )
            : MaterialApp(
                theme: ThemeData.light(),
                home: child,
              );
      },
      routes: {
        '/menu': (context) => MenuWidget(),
        '/profile': (context) => StudentProfilePage(),
        '/profiles': (context) => SavedDataPage(),
        '/customer-profile': (context) => CustomerProfilePage(),
        '/customer-profiles': (context) => SavedDataCustomerPage(),
        '/calculations': (context) => CalculationsPage(), 
        '/login': (context) => LoginPage(),
        '/register': (context) => RegistrationPage(),
      },
    );
  }
}
