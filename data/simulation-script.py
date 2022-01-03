import requests
import json
import time

# kafka producer
URL = "http://localhost:3000/events"
# how many minutes the simulator waits in order to send again a new request
MINS_INTERVAL = 3

def main():
    # read all simulation data
    with open('events.json', 'r') as f:
        events = f.read().strip().split('\n')

    # for every event
    for event in events[1:-1]:
        # set it to the right format in order to be able to convert it to json
        if event[-1] == ',': 
            e = '{' + event[:-1] + '}'
        else:                    
            e = '{' + event + '}'
        # json.loads creates a dict if string is valid
        data = json.loads(e)
        # get the response and print it
        r = requests.post(url = URL, json = data)
        print("Response text is:", r.text)
        
        time.sleep(60 * MINS_INTERVAL)
    
    print("Simulation completed.")

if __name__ == "__main__":
    main()
