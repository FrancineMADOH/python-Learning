import 'package:flutter/material.dart';

class RegistrationScreen extends StatefulWidget {
  const RegistrationScreen({super.key});

  @override
  State<RegistrationScreen> createState() => _RegistrationScreenState();
}

class _RegistrationScreenState extends State<RegistrationScreen> {
  final _formkey = GlobalKey<FormState>();
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
                'Registration',
                style: TextStyle(color: Colors.white, fontSize: 30.0),
              )),
            ),
            const SizedBox(
              height: 20.0,
            ),
            Padding(
              padding: const EdgeInsets.fromLTRB(30.0, 30, 30.0, 30),
              child: Form(
                  key: _formkey,
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
                                gapPadding: 2.0,
                                borderRadius:
                                    BorderRadius.all(Radius.circular(50.0))),
                            prefixIcon: Icon(
                                size: 30.0, color: Colors.red, Icons.person),
                            hintText: "Full Name",
                            hintStyle: TextStyle(fontSize: 15.0)),
                        validator: (String? value) {
                          if (value == null || value.isEmpty) {
                            return "Please enter your full name";
                          }
                          return null;
                        },
                      ),
                      const SizedBox(
                        height: 20.0,
                      ),
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
                                gapPadding: 2.0,
                                borderRadius:
                                    BorderRadius.all(Radius.circular(50.0))),
                            prefixIcon: Icon(
                                size: 30.0, color: Colors.red, Icons.phone),
                            hintText: "Phone",
                            hintStyle: TextStyle(fontSize: 15.0)),
                        validator: (String? value) {
                          if (value == null || value.isEmpty) {
                            return "Invalid Phone Number";
                          }
                          return null;
                        },
                      ),
                      const SizedBox(
                        height: 10.0,
                      ),
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
                                  gapPadding: 2.0,
                                  borderRadius:
                                      BorderRadius.all(Radius.circular(50.0))),
                              prefixIcon: Icon(
                                  size: 30.0, color: Colors.red, Icons.email),
                              hintText: "Email",
                              hintStyle: TextStyle(fontSize: 15.0)),
                          validator: (String? value) {
                            if (value == null || value.isEmpty) {
                              return "Invalid Phone Number";
                            }
                            return null;
                          }),
                      const SizedBox(
                        height: 10.0,
                      ),
                      TextFormField(
                        obscureText: true,
                        obscuringCharacter: "*",
                        decoration: const InputDecoration(
                            fillColor: Color.fromARGB(255, 230, 229, 229),
                            filled: true,
                            errorBorder: OutlineInputBorder(
                              borderSide:
                                  BorderSide(color: Colors.red, width: 0.0),
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
                      ),
                      const SizedBox(
                        height: 20.0,
                      ),
                      ElevatedButton(
                          onPressed: () {
                            if (_formkey.currentState!.validate()) {}
                          },
                          style: ElevatedButton.styleFrom(
                              foregroundColor: Colors.white,
                              backgroundColor: Colors.red,
                              padding: const EdgeInsets.symmetric(
                                  horizontal: 100, vertical: 15.0),
                              textStyle: const TextStyle(fontSize: 15.0)),
                          child: const Text("REGISTER"))
                    ],
                  )),
            ),
            const SizedBox(
              height: 10.0,
            ),
            Row(
              mainAxisAlignment: MainAxisAlignment.center,
              children: [
                const Text(
                  "Have An Account Already ?  ",
                  style: TextStyle(fontSize: 15.0, fontWeight: FontWeight.bold),
                ),
                GestureDetector(
                    onTap: () {
                      Navigator.pop(context);
                    },
                    child: const Text(
                      "Login Now",
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
//#D6B9B9ff