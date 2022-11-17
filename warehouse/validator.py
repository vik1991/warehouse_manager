from django.core.validators import RegexValidator, EmailValidator


class Validator:

    def EmailValidation(self, email):
        print("in the validation form")
        validateEmail = EmailValidator(message="rewrite your email")
        validateEmail(email)
        print(validateEmail)
