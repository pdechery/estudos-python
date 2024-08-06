import re

phonenumbers = ['  987-123-4567  ','123 456 7890','  (123) 456-7890  ']

def validate_phone_numbers(phonenumbers):

	for n in phonenumbers:
		pattern1 = re.compile(r"\([0-9]{3}\) [0-9]{3}-[0-9]{4}")
		pattern2 = re.compile(r"[0-9]{3}-[0-9]{3}-[0-9]{4}")
		number = n.strip()
		print(f'will {number} match?')
		if pattern1.match(number) or pattern2.match(number):
			print(f'yes, {number} is a match')

if __name__ == '__main__':
	
	validate_phone_numbers(phonenumbers)