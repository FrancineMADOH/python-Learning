# import 
import  datetime

# constant
shift = [
    {"code":"M","shift":"Morning", "time":"6H-12H"},
    {"code":"A","shift":"Afternoon", "time":"12H-18H"}
]

pickup_type = ("r","c")

booking_list = [
    {"agent":1,"pickup_date":"", "type":"c","shift":"M"},
    {"agent":2,"pickup_date":"", "type":"r","shift":"A"},
    {"agent":1,"pickup_date":"", "type":"r","shift":"M"},
    {"agent":4,"pickup_date":"", "type":"r","shift":"M"},
    {"agent":1,"pickup_date":"", "type":"c","shift":"M"},
    {"agent":1,"pickup_date":"", "type":"r","shift":"A"},
    {"agent":3,"pickup_date":"", "type":"r","shift":"A"},
    {"agent":1,"pickup_date":"", "type":"c","shift":"M"},
    {"agent":1,"pickup_date":"", "type":"r","shift":"A"},
    {"agent":1,"pickup_date":"", "type":"r","shift":"M"}
]


# inputs
agent = input("Enter the agent unique ID: ")
month = input("Enter the month for which you want to determine the salary(*Reminder: This is for the current year): ")

def remainder_utility(total_resident):
    result_res =  total_resident / 20
    r1 = result_res * 0.2

    if r1 != 0 :
        res1 = r1 / 10
    
    r2 = r1 * 0.1

    if r2 != 0:
        res2 =  r2 / 5
    
    r3 =  r2 * 0.05

    return  r1,r2,r3



def get_agent_salary(agent,month):
    agent_monthly_pickup = []
    commercials = []
    residents = []

    try:
        for booking in booking_list:
            get_month = booking['pickup_date'] # TODO extrack the pickup month from this date
            if booking['agent'] == int(agent) and get_month == month:
                agent_monthly_pickup.append(booking)

        total_agent_shift = len(agent_monthly_pickup)
        print(agent_monthly_pickup)


        for item in agent_monthly_pickup:
            if item['type'] == pickup_type[0]:
                residents.append(item)
            else: 
                commercials.append(item)
        print(commercials)
        
        # TODO step 6
        total_bonus = 0

        total_salary = (total_agent_shift * 500) +  total_bonus
        print(total_salary)

        return total_salary
    except:
        raise ValueError("Error! Please enter valid data")
    
    

get_agent_salary(agent, month)