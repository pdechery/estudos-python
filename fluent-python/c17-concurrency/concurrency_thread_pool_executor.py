from concurrent import futures

from flags import save_flag, get_flag, show, main

MAX_WORKERS = 20

'''
Porquê executar este script é mais rápido do que flags.py?

Porque quando quando há a espera de algum resultado do OS (exemplo: downloads da internet) 
as standard libraries do Python liberam o GIL automaticamente

Assim, enquanto uma thread espera um resultado (ex: o download) as outras são liberadas para rodar na CPU.

Downloads da internet são considerados uma forma de I/O. Outra forma, acredito eu, seria leitura de dados do HD (algo 
que pode demorar sem necessariamente ser por causa de processamento (CPU)).

IMPORTANTE

Como o resultado comprova, é vantajoso usar as threads em tarefas que envolvem bloqueio de I/O.

Já que, como explicado, o desbloqueio da CPU (GIL) é automático.
'''

def download_one(cc):
	image = get_flag(cc)
	show(cc)
	save_flag(image, cc.lower() + '.gif')
	return cc

def download_many(cc_list):
	workers = min(MAX_WORKERS, len(cc_list))
	
	with futures.ThreadPoolExecutor(max_workers=3) as executor:
		to_do = []
		for cc in sorted(cc_list):
			future = executor.submit(download_one, cc)
			to_do.append(future)
			msg = 'Scheduled for {}: {}'
			print(msg.format(cc, future))
	
	results = []
	for future in futures.as_completed(to_do):
		res = future.result()
		msg = '{} result {!r}'
		print(msg.format(future, res))
		results.append(res)
		
	return len(list(res))

if __name__ == '__main__':
	main(download_many)







