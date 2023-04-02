import phonenumbers
from phonenumbers import carrier, geocoder, timezone

mobileNo = str(input("Enter your phone number: "))

mobileNo = phonenumbers.parse(mobileNo)

# Get time zone info
print(f'Time Zone Info: {timezone.time_zones_for_number(mobileNo)}')

# Get carrier info
print(f'Carrier Info: {carrier.name_for_number(mobileNo, "en")}')

# Get region info
print(f'Region Info: {geocoder.description_for_number(mobileNo, "en")}')

# Check if number is valid
print(f'Valid Mobile Number: {phonenumbers.is_valid_number(mobileNo)}')

# Check if number is possible
print(
    f'Checking Possibility of Number: {phonenumbers.is_possible_number(mobileNo)}')

# Get number type
print(f'Number Type: {phonenumbers.number_type(mobileNo)}')

# Get national format
print(
    f'National Format: {phonenumbers.format_number(mobileNo, phonenumbers.PhoneNumberFormat.NATIONAL)}')

# Get international format
print(
    f'International Format: {phonenumbers.format_number(mobileNo, phonenumbers.PhoneNumberFormat.INTERNATIONAL)}')

# Get E164 format
print(
    f'E164 Format: {phonenumbers.format_number(mobileNo, phonenumbers.PhoneNumberFormat.E164)}')
