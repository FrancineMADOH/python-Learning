
class Notification():
    entry = 1000
    number_of_ecopoint = input("Enter the number of ecopoint: ")
    services_to_reedem =  input("Select a service. 1=Voice, 2=Data, 3=Electricity: ")
    
    def __str__(self,notification,user,status):
        self.notification = notification
        self.user = user
        self.status = status

    def send_notification():
        print( )
        

    def agent_assignement(agent):
        print("agent assigned")

    def agent_performance(agent):
        print("agent performance")

    def price_determination():
        print("test")



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
    
    return level


def redeem_ecopoint(point,service):
    try:
        if int(point) < entry :
           message = "You are not yet eligible to redeem points"
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
                       message = f"""You sucessfully redeem your ecopoint for {name} ."""
                   elif ecopoints_left > 0:
                        level = earn_ecopoint(0,ecopoints_left)
                        message  = f"""You sucessfully redeem your ecopoint for {name} . You have {ecopoints_left} ecopoints  left."""
                   else:
                    level = earn_ecopoint(0,int(point))
                    message = f"""Sorry you are not eligible to the service { name }. Points Needed:{ item['points'] }. Your points:{point}. Choose another service."""
            print(message)
    
            return {"total_points":ecopoints_left , "level":level,"message":message}
    except:
        print("Error! Please enter valid data")
        raise ValueError("Error! Please enter valid data")

    def discount_algorithm():
        print("")

