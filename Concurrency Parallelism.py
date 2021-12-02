
import time
import random
import threading


class Philosopher(threading.Thread):
    running = True  

    def __init__(self, index, l_fork, r_fork):
        threading.Thread.__init__(self)
        self.index = index
        self.l_fork = l_fork
        self.r_fork = r_fork

    def p_run(self):
        while(self.running):
            
            time.sleep(30)
            print ('Philosopher %s hungry ' % self.index)
            self.dine()

    def p_dine(self):

        f1, f2 = self.l_fork, self.r_fork
        while self.running:
            f1.acquire() 
            locked = f2.acquire(False) 
            if locked: break 
            f1.release()
            print ('swaps %s ' % self.index)
            f1, f2 = f2, f1
        else:
            return
        self.dining()
        
        f2.release()
        f1.release()
 
    def p_dining(self):			
        print ('Philosopher %s eats. '% self.index)
        time.sleep(30)
        print ('Philosopher %s finish eating.' % self.index)

def main():
    forks = [threading.Semaphore() for i in range(5)] 

    
    philosophers= [Philosopher(i, forks[i%5], forks[(i+1)%5])
            for i in range(5)]

    Philosopher.running = True
    for p in philosophers: p.start()
    time.sleep(100)
    Philosopher.running = False
    print ("finally finish.")
 

if __name__ == "__main__":
    main()

