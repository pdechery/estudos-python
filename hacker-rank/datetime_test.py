'''
Teste na Empresa da Gx2
26-04-22
'''

import datetime
from collections import defaultdict

accessLog = {}
accessLogDefaultDict = defaultdict(str)

def hasAccess_with_get(name,time):

	'''
	O método get() permite buscar uma chave sem dar Exception caso a mesma não exista, retornando None.
	'''

	past_time = 0

	if accessLog.get(name):
		past_time = datetime.datetime.strptime(accessLog[name],'%H:%M:%S')
		curr_time = datetime.datetime.strptime(time,'%H:%M:%S')
		res = curr_time - past_time
		res = res.seconds // 60
		if res > 5:
			print('No')
			return False

	accessLog[name] = time

	print('Yes')
	return True

def hasAccess(name,time):

	past_time = 0

	try:
		if accessLog[name]:
			past_time = datetime.datetime.strptime(accessLog[name],'%H:%M:%S')
			curr_time = datetime.datetime.strptime(time,'%H:%M:%S')
			res = curr_time - past_time
			res = res.seconds // 60
			if res > 5:
				print('No')
				return False

			
	except KeyError: 
		pass

	accessLog[name] = time

	print('Yes')
	return True


def hasAccess_with_default_dict(name,time):

	past_time = 0

	if accessLogDefaultDict[name]:

		past_time = datetime.datetime.strptime(accessLogDefaultDict[name],'%H:%M:%S')
		curr_time = datetime.datetime.strptime(time,'%H:%M:%S')
		res = curr_time - past_time
		res = res.seconds // 60
		if res > 5:
			print('No')
			return False

	accessLogDefaultDict[name] = time

	print('Yes')
	return True



if __name__ == '__main__':
	hasAccess_with_get(name='Harry',time='12:01:00')
	hasAccess_with_get(name='Beth',time='12:01:00')
	hasAccess_with_get(name='Harry',time='12:03:00')
	hasAccess_with_get(name='Beth',time='13:00:00')