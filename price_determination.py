
# constants
trash_size_list = [
    {"container":"Bucket","size":"10","code":"1","unit":"L"},
    {"container":"Trash Bag","size":"27","code":"2","unit":"L"},
    {"container":"Wheelbarrow","size":"80","code":"3","unit":"L"}
]

packages = [
    {"name":"Pickup", "code": "1"},
    {"name":"Cleaning", "code": "2"},
    {"name":"pickup & Cleaning", "code": "3"}
]

# inputs 
trash_size_input = input("Select your trash size. 1=(bucket-10L), 2=(trash bag-27L), 3=(wheelbarrow-80L): ")
trash_quantity  = input("Enter your trash quantity: ")
trash_package = input("Choose package. 1=Pickup, 2=Cleanup, 3=Cleanup & Pickup: ")

def get_trash_volume(code,quantity,package):
    
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
        print(trash_price)
        return trash_price
    except:
        print("Error! Please enter valid data")

get_trash_volume(trash_size_input,trash_quantity,trash_package)