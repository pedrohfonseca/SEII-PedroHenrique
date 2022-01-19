import concurrent.futures
import time

start = time.perf_counter()

def do_something(seconds):
	print(f'Sleeping {seconds} second(s)...')
	time.sleep(seconds)
	return 'Done Sleeping...'


with concurrent.futures.ProcessPoolExecutor() as executor:
	results = [executor.submit(do_something, 1) for _ in range(10)]
	
	for f in concurrent.futures.as_completed(results):
		print(f.result())

#processes = []
#for _ in range(10):
#	p = multiprocessing.Process(target=do_something, args=[1.5])
#	p.start()
#	processes.append(p)
#
#for process in processes:
#	process.join()

finish = time.perf_counter()

print(f'Finished in {round(finish-start, 2)} second(s)')

