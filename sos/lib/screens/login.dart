import 'package:flutter/material.dart';
import 'package:sos/screens/registration.dart';

class LoginScreen extends StatefulWidget {
  const LoginScreen({super.key});

  @override
  State<LoginScreen> createState() => _LoginScreenState();
}

class _LoginScreenState extends State<LoginScreen> {
  final _formKey = GlobalKey<FormState>();
  @override
  Widget build(BuildContext context) {
    return Scaffold(
      resizeToAvoidBottomInset: true,
      body: SingleChildScrollView(
        child: Column(
          children: [
            Container(
              decoration: const BoxDecoration(
                  color: Colors.red,
                  borderRadius: BorderRadius.only(
                      bottomLeft: Radius.circular(100.0),
                      bottomRight: Radius.circular(100.0))),
              padding: const EdgeInsets.fromLTRB(30.0, 100, 30.0, 100),
              child: const Center(
                  child: Text(
                'Login',
                style: TextStyle(color: Colors.white, fontSize: 30.0),
              )),
            ),
            const SizedBox(
              height: 20.0,
            ),
            Container(
              padding: const EdgeInsets.fromLTRB(30.0, 30, 30.0, 30),
              child: Form(
                key: _formKey,
                child: Column(
                  children: [
                    TextFormField(
                        decoration: const InputDecoration(
                            fillColor: Color.fromARGB(255, 230, 229, 229),
                            filled: true,
                            errorBorder: OutlineInputBorder(
                              borderSide: BorderSide(color: Colors.red),
                            ),
                            border: OutlineInputBorder(
                                borderSide: BorderSide(
                                  width: 0.0,
                                  style: BorderStyle.none,
                                ),
                                gapPadding: 4.0,
                                borderRadius:
                                    BorderRadius.all(Radius.circular(50.0))),
                            prefixIcon: Icon(
                                size: 30.0, color: Colors.red, Icons.email),
                            hintText: "Enter Email",
                            hintStyle: TextStyle(fontSize: 15.0)),
                        validator: (String? value) {
                          if (value == null || value.isEmpty) {
                            return "Please enter a valid email";
                          }
                          return null;
                        }),
                    const SizedBox(
                      height: 40.0,
                    ),
                    TextFormField(
                        obscureText: true,
                        obscuringCharacter: "*",
                        decoration: const InputDecoration(
                            fillColor: Color.fromARGB(255, 230, 229, 229),
                            filled: true,
                            errorBorder: OutlineInputBorder(
                              borderSide: BorderSide(color: Colors.red),
                            ),
                            border: OutlineInputBorder(
                                borderSide: BorderSide(
                                  width: 0.0,
                                  style: BorderStyle.none,
                                ),
                                gapPadding: 2.0,
                                borderRadius:
                                    BorderRadius.all(Radius.circular(50.0))),
                            prefixIcon:
                                Icon(size: 30.0, color: Colors.red, Icons.key),
                            hintText: "Password",
                            hintStyle: TextStyle(fontSize: 15.0)),
                        validator: (String? value) {
                          if (value == null || value.isEmpty) {
                            return "Please enter your password";
                          }
                          return null;
                        }),
                    const SizedBox(
                      height: 40.0,
                    ),
                    ElevatedButton(
                        onPressed: () {
                          if (_formKey.currentState!.validate()) {}
                        },
                        style: ElevatedButton.styleFrom(
                            backgroundColor: Colors.red,
                            foregroundColor: Colors.white,
                            padding: const EdgeInsets.symmetric(
                                horizontal: 100, vertical: 15.0),
                            textStyle: const TextStyle(fontSize: 15.0)),
                        child: const Text("LOGIN"))
                  ],
                ),
              ),
            ),
            const SizedBox(
              height: 20.0,
            ),
            Row(
              mainAxisAlignment: MainAxisAlignment.center,
              children: [
                const Text(
                  "Don't Have Any Account ?  ",
                  style: TextStyle(fontSize: 15.0, fontWeight: FontWeight.bold),
                ),
                GestureDetector(
                    onTap: () {
                      Navigator.push(
                          context,
                          MaterialPageRoute(
                              builder: (context) =>
                                  const RegistrationScreen()));
                    },
                    child: const Text(
                      "Register Now",
                      style: TextStyle(
                          color: Colors.red,
                          fontSize: 15.0,
                          fontWeight: FontWeight.bold),
                    ))
              ],
            ),
          ],
        ),
      ),
    );
  }
}
