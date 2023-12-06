trash_size_list = [
        {"container":"Bucket","size":"10","code":"1","unit":"L"},
        {"container":"Trash Bag","size":"27","code":"2","unit":"L"},
        {"container":"Wheelbarrow","size":"80","code":"3","unit":"L"}
    ]

packages = [
        {"name":"Pickup", "code": "1"},
        {"name":"Cleaning", "code": "2"},
        {"name":"Cleaning & Pickup", "code": "3"}
]

# inputs 
trash_size_input = input("Select your trash size. 1=(bucket-10L), 2=(trash bag-27L), 3=(wheelbarrow-80L): ")
trash_quantity  = input("Enter your trash quantity: ")
trash_package = input("Choose package. 1=Pickup, 2=Cleanup, 3=Cleanup & Pickup: ")
bid_amount = input("How much are you ready to pay for your service? : ")

class PriceDetermination():
    
    bid_status = ("Approved", "Rejected")

    def __init__(self,trash_size_input,trash_quantity,trash_package,bid_amount):
        self.trash_size_input = trash_size_input
        self.trash_quantity = trash_quantity
        self.trash_package = trash_package
        self.bid_amount = bid_amount

    
    def get_trash_price(self,code,quantity,package,bid):
        
        try:
            for element in trash_size_list:
                trash_code = element['code']
                trash_size = element['size']
                if trash_code == code:
                    trash_volume = (int(trash_size)/1000) * int(quantity)

            for item in packages:
                package_choose = item['code']
                if package == package_choose:
                    price = trash_volume * 5000
                    if package == "1": 
                        trash_price =  price
                    else:
                        trash_price = 1.2 * price
            
            if int(bid) < price:
                status = self.bid_status[1]
                print(f"{ status } : Price too low. Minimum:{ price }, Your price: { bid }")
            elif int(bid) > price:
                status = self.bid_status[0]

            print(trash_price,status)
            return { "price":trash_price, "status": status, "bid_amount":bid }
        except:
            print("Error! Please enter valid data")
            raise ValueError("Error! Please enter valid data")

    get_trash_price(trash_size_input,trash_quantity,trash_package,bid_amount)
