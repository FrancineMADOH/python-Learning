
# constant
trash_size_list = [
    {"container":"Bucket","size":"10","code":"1","unit":"L"},
    {"container":"Trash Bag","size":"27","code":"2","unit":"L"},
    {"container":"Wheelbarrow","size":"80","code":"3","unit":"L"}
]

# input 
trash_size_input = input("Select your trash size. 1=(bucket-10L), 2=(trash bag-27L), 3=(wheelbarrow-80L): ")
trash_quantity  = input("Enter your trash quantity: ")
def get_trash_volume(code,quantity):
    
    try:
        for element in trash_size_list:
            trash_code = element['code']
            trash_size = element['size']
            if trash_code == code:
                trash_volume = (int(trash_size)/1000) * int(quantity)
            else:
                raise ValueError("Choice not available")
        return trash_volume
    except:
        print("Error! Please enter valid data")

get_trash_volume(trash_size_input,trash_quantity)