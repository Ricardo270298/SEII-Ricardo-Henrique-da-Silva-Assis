import concurrent.futures
import time
import threading

start = time.perf_counter() #inicia o timer usado pra saber quanto tempo demorou pra tudo acontecer


def do_something(seconds):
    print(f'Sleeping {seconds} second(s)...')
    time.sleep(seconds) #espera/dorme por 1 segundo
    #print('Done Sleeping...')
    return f'Done Sleeping...{seconds}'

#do_something()
#t1 = threading.Thread(targe=do_something) #Cria uma thread cujo alvo é a função do_something
#t2 = threading.Thread(targe=do_something)

#t1.start() #Inicia a Thread
#t2.start()

with concurrent.futures.ThreadPoolExecutor() as executor:
	
#	f1 = executor.submit(do_something,1)
#	f2 = executor.submit(do_something,1)
#	print(f1.result())
#	print(f2.result())

    secs = [5, 4, 3, 2, 1]
		#Retorna um objeto futuro
	results = [executor.submit(do_something, sec) for sec in secs] #executando a função e usando como argumento o "sec" que varia de acordo com o loop
	
	for f in concurrent.futures.as_completed(results): 
		print(f.result()) # por usar o metodo completed, será printado na ordem que as threads forem finalizadas 


    results = executor.map(do_something, secs) #Executa a função para cada valor da lista e retorna os resultados
					       #Os resultados serão retornados na ordem em que as threads foram iniciadas
    for result in results:
         print(result)

 threads = []

 for _ in range(10): #loop criado para criar varias threads de uma vez
     t = threading.Thread(target=do_something, args=[1.5]) # passa os argumentos
     t.start()
     threads.append(t)

 for thread in threads: #loop criado pra finalizar todas as threads
     thread.join()

t1.join() #Garante que a thread seja completada/juntada antes de finalizar o contador
t2.join()
finish = time.perf_counter() #Finaliza o contador

print(f'Finished in {round(finish-start, 2)} second(s)')
