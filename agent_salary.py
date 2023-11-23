# import 
import datetime 

# constant
shift = [
    {"code":"M","shift":"Morning", "time":"6H-12H"},
    {"code":"A","shift":"Afternoon", "time":"12H-18H"}
]

pickup_type = ("r","c")

bonuses = {"bonus_of_twenty": 1000,"bonus_of_ten": 500, "bonus_of_five":200}


booking_list = [
    {"agent":1,"pickup_date":"2023-09-22 08:16:11", "type":"c","shift":"M"},
    {"agent":2,"pickup_date":"2023-11-22 09:16:11", "type":"r","shift":"A"},
    {"agent":1,"pickup_date":"2023-11-22 12:16:11", "type":"r","shift":"M"},
    {"agent":4,"pickup_date":"2023-10-22 11:16:11", "type":"r","shift":"M"},
    {"agent":1,"pickup_date":"2023-11-22 12:16:11", "type":"c","shift":"M"},
    {"agent":1,"pickup_date":"2023-11-22 10:16:11", "type":"r","shift":"A"},
    {"agent":3,"pickup_date":"2023-11-22 16:16:19", "type":"r","shift":"A"},
    {"agent":1,"pickup_date":"2023-11-22 12:16:11", "type":"c","shift":"M"},
    {"agent":1,"pickup_date":"2023-01-22 17:16:11", "type":"r","shift":"A"},
    {"agent":1,"pickup_date":"2023-11-22 18:16:11", "type":"r","shift":"M"},
    {"agent":1,"pickup_date":"2023-09-22 08:16:00", "type":"c","shift":"M"},
    {"agent":2,"pickup_date":"2023-11-22 09:16:11", "type":"r","shift":"A"},
    {"agent":5,"pickup_date":"2023-12-22 12:16:11", "type":"r","shift":"M"},
    {"agent":4,"pickup_date":"2023-10-22 11:16:11", "type":"r","shift":"M"},
    {"agent":1,"pickup_date":"2023-11-22 12:16:11", "type":"c","shift":"M"},
    {"agent":1,"pickup_date":"2023-11-22 10:16:51", "type":"r","shift":"A"},
    {"agent":3,"pickup_date":"2023-11-22 16:16:11", "type":"r","shift":"A"},
    {"agent":8,"pickup_date":"2023-11-22 12:16:31", "type":"c","shift":"M"},
    {"agent":1,"pickup_date":"2023-12-22 17:16:11", "type":"r","shift":"A"},
    {"agent":1,"pickup_date":"2023-11-22 18:16:11", "type":"r","shift":"M"}
]


# inputs
agent = input("Enter the agent unique ID: ")
month = input("Enter the month for which you want to determine the salary(*Example: 01 for January): ")

def remainder_utility(total_resident):

    try:
        res1 =  total_resident / 20
        r1 = res1 * 0.2

        if r1 != 0 :
            res2 = r1 / 10
            r2 = r1 * 0.1
        
        if r2 != 0:
            res3 =  r2 / 5
            r3 =  r2 * 0.05

        result = {"result1":res1,"result2":res2,"result3":res3,"r1":r1,"r2":r1,"r3":r3}

        return  result
    except:
        return {"result1":0,"result2":0,"result3":0,"r1":0,"r2":0,"r3":0}
    


def get_agent_salary(agent,month):
    agent_monthly_pickup = []
    commercials = []
    residents = []

    try:
        for booking in booking_list:
            get_month = booking['pickup_date'].split('-')[1] 
            # TODO extrack the pickup month from this date
            if booking['agent'] == int(agent) and get_month == month:
                agent_monthly_pickup.append(booking)

        total_agent_shift = len(agent_monthly_pickup)

        for item in agent_monthly_pickup:
            if item['type'] == pickup_type[0]:
                residents.append(item)
            else: 
                commercials.append(item)

        # step 5 
        result =  remainder_utility(len(residents))
        
        # # # TODO step 6
        for key,value in bonuses.items():

            if key == 'bonus_of_twenty':
                m1  = value * result['result1']

            if key == 'bonus_of_ten':
                m2  = value * result['result2']
                
            if key == 'bonus_of_five':
                m3  = value * result['result3']

        total_bonus = (m1+m2+m3) + (result['r3'] * 50)

        total_salary = (total_agent_shift * 500) +  total_bonus
        
        print( { "total_salary": total_salary })

        return { "total_salary": total_salary }
    except:
        raise ValueError("Error! Please enter valid data")
    
    

get_agent_salary(agent, month)