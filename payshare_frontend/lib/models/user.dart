class User {
  final String code;
  final String password;
  final String email;
  final String fiscalCode;
  final DateTime birthDate;
  final String birthPlace;
  final String residence;
  final String smartContractList;
  final String extensions;

  User({
    required this.code,
    required this.password,
    required this.email,
    required this.fiscalCode,
    required this.birthDate,
    required this.birthPlace,
    required this.residence,
    required this.smartContractList,
    required this.extensions,
  });

  factory User.fromJson(Map<String, dynamic> json) {
    return User(
      code: json['code'],
      password: json['password'],
      email: json['email'],
      fiscalCode: json['fiscalCode'],
      birthDate: DateTime.parse(json['birthDate']),
      birthPlace: json['birthPlace'],
      residence: json['residence'],
      smartContractList: json['smartContractList'],
      extensions: json['extensions'],
    );
  }

  Map<String, dynamic> toJson() {
    return {
      'code': code,
      'password': password,
      'email': email,
      'fiscalCode': fiscalCode,
      'birthDate': birthDate.toIso8601String(),
      'birthPlace': birthPlace,
      'residence': residence,
      'smartContractList': smartContractList,
      'extensions': extensions,
    };
  }
}