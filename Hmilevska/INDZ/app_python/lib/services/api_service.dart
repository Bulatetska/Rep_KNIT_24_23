import 'package:http/http.dart' as http;
import 'dart:convert';

class ApiService {
  static const String baseUrl = 'http://127.0.0.1:8000';

  static Future<http.Response> register(Map<String, dynamic> data) async {
    const url = '$baseUrl/register';
    final response = await http.post(
      Uri.parse(url),
      body: json.encode(data),
      headers: {'Content-Type': 'application/json'},
    );
    return response;
  }

  static Future<http.Response> login(Map<String, dynamic> data) async {
    const url = '$baseUrl/login';
    final response = await http.post(
      Uri.parse(url),
      body: json.encode(data),
      headers: {'Content-Type': 'application/json'},
    );
    return response;
  }
}
