import concurrent.futures
import time

t1 = time.perf_counter()


def do_something(seconds):
    print(f'Sleeping {seconds} second(s)...')
    time.sleep(seconds)
    return f'Done Sleeping...{seconds}'

# do_something()
# do_something()

#Criando multiplos processos cujo o alvo seja a função do_something
#p1 = multiprocessing.Process(target=do_something)
#p2 = multiprocessing.Process(target=do_something)
#Para iniciar os processos criados anteriormente é necessario usar o seguinte metodo:
#p1.start()
#p2.start() #Desta forma o restante do codigo é executado antes do processo finalizar, e assim o tempo 
	   # assinalado é menor do que o real
#p1.join()  #É usado para garantir que os processos criados serão finalizados antes que o restante do codigo seja executado
#p2.join()
processes = []
#Loop para iniciar varios processos de forma mais pratica:
for _ in range(10):
	p = multiprocessing.Process(target=do_something, args=[1.5])#args representa o argumento que sera passado para a função
	p.start() #Não se pode usar o join dentro do mesmo loop em que o processo foi iniciado.
		  #Isso faria com que cada processo fosse finalidao separadamente, tendo uma situação parecida com um metodo assincrono
	processes.append(p) #colocando os processos iniciados dentro de uma lista criada anteriormente
#Loop criado para finalizar os processos
for process in processes:
	process.join()
with concurrent.futures.ProcessPoolExecutor() as executor:
	#f1 = executor.submit(do_something,1) # Agenda a execução da função e e retorna um objeto futuro
 	#f2 = executor.submit(do_something,1)
        #print(f1.result)
	#print(f2.result)
	secs = [5, 4, 3, 2, 1]
	#results = [executor.submit(do_something,1) for _ range(10)]
	#for f in concurrent.futures.as_completed(results):
	#	print(f.result())
	results = executor.map(do_something, secs)
	
	for result in results:
		print(result)


t2 = time.perf_counter()

print(f'Finished in {round(t2-t1, 2)} second(s)')
