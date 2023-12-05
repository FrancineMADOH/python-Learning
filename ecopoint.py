
class Ecopoint():
    entry  = 1000
    services = []
    number_of_ecopoint = 0
    services_to_reedem =  0

    def __str__(self,entry):
        self.entry = entry
        
    
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
                for item in self.services:
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
