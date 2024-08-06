import logging

logging.basicConfig(level=logging.INFO)
log = logging.getLogger('__wn__')

HOUR_IN_SECONDS = 3600
MINUTE_IN_SECONDS = 60


def format_time(seconds, get_fractions) -> str:
	"""
	Transfom seconds in hours (depending on input), minutes, seconds and miliseconds
	Creates a user-friendly formatted message using the above mentioned values
	Parameters are the same as in decorated function. 

	:return: string
	"""
	ms = (seconds - int(seconds)) * 1000
	ms = int(ms) if not get_fractions else round(ms, 4) # round value can be changed as needed
	if seconds >= HOUR_IN_SECONDS:
		h, r = divmod(int(seconds), HOUR_IN_SECONDS)
		m, s = divmod(int(r), MINUTE_IN_SECONDS)
		result = f'{int(h)} hours {int(m)} mins {int(s)} secs and {ms} miliseconds'
	else:
		m, s = divmod(int(seconds), MINUTE_IN_SECONDS)
		result = f'{int(m)} mins {int(s)} secs and {ms} miliseconds'
	return result


def log_time(func):
	"""
	Decorator will get time from decorated function and log it like so: 
	"000 hours 000 mins 000 secs and 000 miliseconds"
	After logging, it will return whatever the decorated function returns
	"""
	def wrap(*args):
		try:
			s = args[0]
			if len(args) == 1:
				f = func.__defaults__[0] # getting default argument value from decorated function, as it's not passed
			else:
				f = args[1]
			log.info(f'input is {s}')
			res = func(s, f)
			formatted_time = format_time(s, f)
			log.info(formatted_time)
			return res # bugfix: needed to return response from decorated function 
		except Exception as err:
			log.exception(err)
	return wrap


@log_time
def counter_challenge(seconds, get_fractions=False) -> str:
	"""
	Dummy function that passes its arguments to decorator and returns a string
	To allow simultaneous testing with multiple values the implementation just passes the arguments instead of simulating execution with sleep()

	:param seconds: Integer or Float representing time in seconds
	:param get_fractions: Boolean to control display of fractional values beyond miliseconds
	:return: string
	"""
	return '''
	Done with main function
	'''


if __name__ == '__main__':
	
	seconds = [
		3,
		61,
		60,
		52,
		22.660061734999545,
		7245.888765,
		9945.660061734999545,
	]	
	for s in seconds:
		print(counter_challenge(s, True))
	
	
