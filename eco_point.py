# constant 
entry = 1000
index = 0
services = [
    {"service":"Voice", "code":"1", "points": 1000},
    {"service":"Data",  "code":"2","points": 1500},
    {"service":"Electricity", "code":"3", "points": 2000}
]

# Input 

number_of_ecopoint = input("Enter the number of ecopoint: ")
services_to_reedem =  input("Select a service. 1=Voice, 2=Data, 3=Electricity: ")

def get_ecopoint_value(price):
    points = round(price/100,None)
    return points

def earn_ecopoint(points,available_points):
    total = int(points + available_points)
    if total < 1000:
        level = "Entry"
    elif total > 1000:
        level = "Bronze"
    elif total > 2000:
        level = "Gold"
    else:
        level = "Platinium"
    
    return level, total


def redeem_ecopoint(point,service):
    try:
        if int(point) < entry :
           print("You are not yet eligible to redeem point yet")
           message = "You are not yet eligible to redeem point yet"
           return message
        elif int(point)>=entry:
            for item in services:
               code =  item['code'] 
               base = item['points']
               name = item["service"]

               if service == code: 
                   available_point = int(point) - base
                   if available_point == 0:
                       level = "Entry"
                       message = f"""You sucessfully redeem your ecopoint for {name} . You have {available_point} ecopoints  left. Your Eco-level: {level}"""
                   elif available_point > 0:
                        level = earn_ecopoint(0,available_point)
                        message  = f"""You sucessfully redeem your ecopoint for {name} . You have {available_point} ecopoints  left. Your Eco-level: {level}"""
                   else:
                    level = earn_ecopoint(0,int(point))
                    message = f"""Sorry you are not eligible to the service { name }. Points Needed:{ item['points'] }. Your points:{point}. Choose another service."""
            print(message)
            return available_point , level
    except:
        print("Error! Please enter valid data")

    
redeem_ecopoint(number_of_ecopoint,services_to_reedem)