from django.core.validators import RegexValidator


class Validator:

    def EmailValidation(self):
        print("in the validation form")
        validateUsername = RegexValidator(r'/[a-zA-Z0-9]', message="validator trigger")

        if not validateUsername:
            print("validation is done")
            # validateEmail = RegexValidator()
            # validateassword = RegexValidator()
            print(validateUsername)
