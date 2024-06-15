def get_country_code():
    print("Enter your country code:")
    country_code = input()
    return country_code

def get_phone_number():
    print("Enter your phone number:")
    phone_number = input()
    return phone_number

def get_number():
    country_code = get_country_code()
    phone_number = get_phone_number()
    number = country_code + phone_number
    return number

