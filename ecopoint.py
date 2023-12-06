services = [
    {"service":"Voice", "code":"1", "points": 1000},
    {"service":"Data",  "code":"2","points": 1500},
    {"service":"Electricity", "code":"3", "points": 2000}
]
# Input 

ecopoint = input("Enter the number of ecopoint: ")
service =  input("Select a service. 1=Voice, 2=Data, 3=Electricity: ")

class Ecopoint():
    
    entry  = 1000    

    def __str__(self,ecopoint,service):
        self.services_to_reedem = ecopoint
        self.number_of_ecopoint = service
        
    
    @classmethod
    def get_ecopoint_value(self,price):
        points = round(price/100,None)
        return points

    @classmethod
    def earn_ecopoint(self,points,available_point):
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

    @classmethod
    def redeem_ecopoint(self,point,service):
        try:
            if int(point) < self.entry :
                message = "You are not yet eligible to redeem points"
                return message
            
            elif int(point) >= self.entry:
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
                            level = self.earn_ecopoint(0,ecopoints_left)
                            message  = f"""You sucessfully redeem your ecopoint for {name} . You have {ecopoints_left} ecopoints  left."""
                    else:
                        level = self.earn_ecopoint(0,int(point))
                        message = f"""Sorry you are not eligible to the service { name }. Points Needed:{ item['points'] }. Your points:{point}. Choose another service."""
                print(message)
        
                return {"total_points": ecopoints_left , "level": level,"message": message}
        except:
            print("Error! Please enter valid data")
            raise ValueError("Error! Please enter valid data")
