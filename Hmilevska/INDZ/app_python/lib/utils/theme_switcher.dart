import 'package:flutter/material.dart';

class ThemeSwitcher extends StatefulWidget {
  final Widget child;

  ThemeSwitcher({required this.child});

  static _ThemeSwitcherState of(BuildContext context) {
    final _ThemeSwitcherState? state = context.findAncestorStateOfType<_ThemeSwitcherState>();
    if (state != null) {
      return state;
    }
    throw Exception('ThemeSwitcher.of() called without ThemeSwitcher widget in the widget tree.');
  }

  @override
  _ThemeSwitcherState createState() => _ThemeSwitcherState();
}

class _ThemeSwitcherState extends State<ThemeSwitcher> {
  bool isDarkModeEnabled = false;

  void switchTheme() {
    setState(() {
      isDarkModeEnabled = !isDarkModeEnabled;
    });
  }

  @override
  Widget build(BuildContext context) {
    return widget.child;
  }
}
