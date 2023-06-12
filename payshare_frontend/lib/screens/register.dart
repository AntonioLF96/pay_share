import 'package:flutter/material.dart';
import 'package:http/http.dart' as http;

import '../env.sample.dart';

class UserRegistrationPage extends StatefulWidget {
  @override
  _UserRegistrationPageState createState() => _UserRegistrationPageState();
}

class _UserRegistrationPageState extends State<UserRegistrationPage> {
  TextEditingController _codeController = TextEditingController();
  TextEditingController _passwordController = TextEditingController();
  TextEditingController _emailController = TextEditingController();
  TextEditingController _fiscalCodeController = TextEditingController();
  TextEditingController _birthDateController = TextEditingController();
  TextEditingController _birthPlaceController = TextEditingController();
  TextEditingController _residenceController = TextEditingController();
  TextEditingController _smartContractListController = TextEditingController();
  TextEditingController _extensionsController = TextEditingController();

  bool _registrationSuccess = false;


  Future<void> _registerUser() async {
    final url = '${Env.URL_PREFIX}/register/';
    final uri = Uri.parse(url);

    var response = await http.post(uri, body: {
      'code': _codeController.text,
      'password': _passwordController.text,
      'email': _emailController.text,
      'fiscalCode': _fiscalCodeController.text,
      'birthDate': _birthDateController.text,
      'birthPlace': _birthPlaceController.text,
      'residence': _residenceController.text,
      'smartContractList': _smartContractListController.text,
      'extensions': _extensionsController.text,
    });

    if (response.statusCode == 200) {
      setState(() {
        _registrationSuccess = true;
      });
    } else {
      _registrationSuccess = false;
      // User registration failed
      // Add your logic here for failed registration
    }
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: Text('User Registration'),
      ),
      body: SingleChildScrollView(
        child: Padding(
          padding: EdgeInsets.all(16.0),
          child: Column(
            children: [
              TextField(
                controller: _codeController,
                decoration: InputDecoration(labelText: 'Code'),
              ),
              TextField(
                controller: _passwordController,
                decoration: InputDecoration(labelText: 'Password'),
                obscureText: true,
              ),
              TextField(
                controller: _emailController,
                decoration: InputDecoration(labelText: 'Email'),
                keyboardType: TextInputType.emailAddress,
              ),
              TextField(
                controller: _fiscalCodeController,
                decoration: InputDecoration(labelText: 'Fiscal Code'),
              ),
              TextField(
                controller: _birthDateController,
                decoration: InputDecoration(labelText: 'Birth Date'),
                keyboardType: TextInputType.datetime,
              ),
              TextField(
                controller: _birthPlaceController,
                decoration: InputDecoration(labelText: 'Birth Place'),
              ),
              TextField(
                controller: _residenceController,
                decoration: InputDecoration(labelText: 'Residence'),
              ),
              TextField(
                controller: _smartContractListController,
                decoration: InputDecoration(labelText: 'Smart Contract List'),
              ),
              TextField(
                controller: _extensionsController,
                decoration: InputDecoration(labelText: 'Extensions'),
              ),
              SizedBox(height: 16.0),
              ElevatedButton(
                onPressed: _registerUser,
                child: Text('Register'),
              ),

              _registrationSuccess
                  ? const Text(
                'Registration Successful!',
                style: TextStyle(
                  color: Colors.green,
                  fontSize: 18.0,
                  fontWeight: FontWeight.bold,
                ),
              )
                  : Container(),
            ],
          ),
        ),
      ),
    );
  }
}