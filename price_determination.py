class PriceDetermination():
    booking_list  = []
    bonuses = {"bonus_of_twenty": 1000,"bonus_of_ten": 500, "bonus_of_five":200}

    def __init__(self, shift,pickup_type,agent,month):
        self.shift = shift
        self.pickup_type = pickup_type
        self.agent = agent 
        self.month = month

    def remainder_utility(self,total_resident):

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
        


    def get_agent_salary(self,agent,month):
        agent_monthly_pickup = []
        commercials = []
        residents = []

        try:
            for booking in self.booking_list:
                get_month = booking['pickup_date'].split('-')[1] 
            
                if booking['agent'] == int(agent) and get_month == month:
                    agent_monthly_pickup.append(booking)

            total_agent_shift = len(agent_monthly_pickup)

            for item in agent_monthly_pickup:
                if item['type'] == self.pickup_type[0]:
                    residents.append(item)
                else: 
                    commercials.append(item)

            result =  self.remainder_utility(len(residents))
            
            for key,value in self.bonuses.items():

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
        
        