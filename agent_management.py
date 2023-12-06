import time 
import datetime
  
  
curr_time = time.localtime() 
curr_clock = time.strftime("%H:%M:%S", curr_time) 
day_name = ''
print(curr_clock) 
print(datetime.datetime.now())

agent = {

    "agent_id":1,
    "available": True,
    "agent_shift": [
        {"monday":['M']},
        {"tuesday":['M','A']},
        {"wednesday":['M','A']},
        {"thursday":['M']},
        {"friday":['M','A']}
    ]
}

test = agent['agent_shift']
for el  in test:
    print(el.keys())
    # for value in el.values:
    #     print(value)

class AgentManagement():
    time_of_day = ''

    def __init__(self,agent):
        self.agent = agent

    def get_agent_shift(self):
        if(curr_time  > 12):
            self.time_of_day = 'A'
        else:
            self.time_of_day = 'M'

    def get_agent_availability(self,agent):
        print('')

# Available agent
# Requirements

# Input 
# An agent (date, shifts, available)
# Agent_shift is a map {“monday”: [“morning”, “afternoon”]}

# Output 
# Available

# Algorithm







