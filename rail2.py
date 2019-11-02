import math
import gps 
import time

session = gps.gps("127.0.0.1", "2947") 
session.stream(gps.WATCH_ENABLE | gps.WATCH_NEWSTYLE)

def gpsdis():
    while True:
        try:
            time.sleep(0.5)
            raw_data = session.next()

            return(raw_data.lat, raw_data.lon)
                
        except KeyError:
                    pass
        except KeyboardInterrupt:
                    quit()
        except StopIteration:
                    session = None
                    print("No incoming data from the GPS module")


def distance(x1,y1,x2,y2):
    return(math.sqrt(((y1-y2)**2) + ((x1-x2)**2)))

def run():
    for i in range(2):
        lat1, lng1 = gpsdis()

        distance1 = distance(lat1, lng1,2,2)
        distance2 = distance(lat1, lng1, 15, 15)
        print(distance1,'***************************' ,distance2)
        
        if distance1 <= 1 :
            print('Welcome 1 km to station A')
            
        elif distance1 <= 3 :
            print('Welcome 3 km to station A')
        elif distance1 <= 5:
            print('Welcome 5 km to station A') 
        
        
        
        if distance2 <= 1 :
            print('Next station is B in 1 km')
            
        elif distance2 <= 3 :
            print('Next station is B in 3 km')
        elif distance2 <= 5:
            print('Next station is B in 5 km ') 
            
        i += 1

if __name__ == '__main__':
    run()
    
