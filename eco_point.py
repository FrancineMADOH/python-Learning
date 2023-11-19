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


def earn_ecopoint(points,available_point):
    total = int(points + available_point)
    if total < 1000:
        level = "Entry"
    elif total < 2000:
        level = "Bronze"
    elif total < 3000:
        level = "Gold"
    elif total > 3000:
        level = "Platinium"
    else:
        "Invalid data"
    
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
                   ecopoints_left = int(point) - base
                   if ecopoints_left == 0:
                       level = "Entry"
                       message = f"""You sucessfully redeem your ecopoint for {name} . You have {ecopoints_left} ecopoints  left. Your Eco-level: {level}"""
                   elif ecopoints_left > 0:
                        level = earn_ecopoint(0,ecopoints_left)
                        message  = f"""You sucessfully redeem your ecopoint for {name} . You have {ecopoints_left} ecopoints  left. Your Eco-level: {level}"""
                   else:
                    level = earn_ecopoint(0,int(point))
                    message = f"""Sorry you are not eligible to the service { name }. Points Needed:{ item['points'] }. Your points:{point}. Choose another service."""
            print(message)
            return ecopoints_left , level
    except:
        print("Error! Please enter valid data")

    
redeem_ecopoint(number_of_ecopoint,services_to_reedem)