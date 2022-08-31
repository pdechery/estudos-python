'''
https://www.hackerrank.com/challenges/one-week-preparation-kit-time-conversion

AM = antes meio dia
PM = depois de meio dia

'''

def timeConversion(s):

	'''
	Converte tempo AM/PM para 24hs
	Recebe string com o tempo em formato AMPM e devolve em formato 24h

	Exemplos:
	12:00AM 00:00
	12:00PM	12:00
	08:00AM 20:00
	04:00PM 16:00
	'''
    
	ampm = s[-2:]
	hour = int(s[:2])

	# 12:00:00AM precisa passar para 00:00:00
	if ampm == "AM" and hour == 12:
		hour = 00

	# 12:00:00PM equivale a 12:00:00
	if ampm == "PM"  and hour != 12:
		hour += 12

	new_time = f'{hour:0>2}{s[2:8]}'

	return new_time

if __name__ == '__main__':

	time = input()
	
	res = timeConversion(time)

	print(res)