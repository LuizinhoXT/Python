import phonenumbers

from phonenumbers import geocoder

num = input("digite o telefone a ser verificado: ")

phone_number = phonenumbers.parse(num)

info = (geocoder.description_for_number(phone_number, "pt"))

print(info)