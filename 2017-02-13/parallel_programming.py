import threading 

from threading import Lock

############################################################################################
# Nebenläufige Programmierung
############################################################################################

# Warum braucht man Nebenläufige/Parallele Programmierung?

#   1.  Betriebssystem:
#       Mehrere Programme werden nebeneinander ausgeführt, ein Taskswitcher verwaltet die 
#       Prozessorzeit zwischen verschiedenen Anwendungen (Timesahring)
#   2.  Performance
#       Da CPU-Takterhöhung nicht mehr effizient ist (<4 GHz) werden Multicore-CPUs entwickelt. 
#       100%-CPU Nutzung nur mit mehreren simultan ausgeführten Tasks

# Welche Arten gibt es, Programme nebenläufig zu machen?

#   1.  Prozesse/Tasks
#       Jedes Programm auf dem Computer läuft in einem eigenen Prozess mit Resourcen, 
#       die nur innerhalb des Prozesses verfügbar sind
#   2.  Threads
#       Threads sind wie Tasks, laufen aber innerhalb eines Prozesses ab, daher können sie 
#       gemeinsame Resourcen(Speicher) nutzen
#   3.  (Green Threads)
#       Ähnlich wie Threads, werden aber vom Programm/Laufzeitumgebung verwaltet. Wird hier 
#       nicht behandelt.


#############################################################################################
# Multithreading Beispiel
#############################################################################################

# Einfache Counter-Funktion, als Argumente werden Thread-ID und Counter-Limit übergeben

def counter(thread_id, limit):
    """ assert counter(1):
    """
    i = 0
    if limit > 0:
        while i < limit:
            i += 1
            #print("Thread #" + str(thread_id) + "- Counter is at " + str(i))

    print("Thread #" + str(thread_id).zfill(2) + "- Counter finished ")

# Hier werden die Threads erzeugt und aufgerufen
def simple_counter_multithreading():

    threadlist = []
    for i in range(0, 20):
        my_thread = threading.Thread(target=counter, args=(i, 10000,))
        my_thread.start()
        threadlist.append(my_thread)


#simple_counter_multithreading()




counter_variable = 0





def shared_counter(thread_id, limit):

    global counter_variable
    global mutex

    counter_running = True

    if limit > 0:
        while counter_running:

            if counter_variable < limit:
            
                temp_counter = counter_variable
                temp_counter += 1
                counter_variable = temp_counter
                print("Thread #" + str(thread_id).zfill(2) + "- Counter is at " + str(counter_variable))
            else:
                counter_running = False
            
            

    #print("Thread #" + str(thread_id).zfill(2) + "- Counter finished ")


def conflict_counter_multithreading():

    threadlist = []
    for i in range(0, 50):
        my_thread = threading.Thread(target=shared_counter, args=(i, 1000,))
        my_thread.start()
        threadlist.append(my_thread)


#conflict_counter_multithreading()


counter_variable_fixed = 0

mutex = Lock()



def shared_counter_fixed(thread_id, limit):

    global counter_variable_fixed
    global mutex

    counter_running = True

    if limit > 0:
        while counter_running:
            mutex.acquire()
            if counter_variable_fixed < limit:
            
                temp_counter = counter_variable_fixed
                temp_counter += 1
                counter_variable_fixed = temp_counter
                print("Thread #" + str(thread_id).zfill(2) + "- Counter is at " + str(counter_variable_fixed))
            else:
                counter_running = False
            
            
            mutex.release()
    
    #print("Thread #" + str(thread_id).zfill(2) + "- Counter finished ")


def fixed_counter_multithreading():

    threadlist = []
    for i in range(0, 50):
        my_thread = threading.Thread(target=shared_counter_fixed, args=(i, 10000,))
        my_thread.start()
        threadlist.append(my_thread)


fixed_counter_multithreading()
