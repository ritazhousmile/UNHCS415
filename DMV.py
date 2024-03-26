# Huan Zhou
# 12_Dictionary Lab
# 03/07/2024


def validate_nh_license_plate(s):
    if len(s) == 7 and s.isdigit():
        return True
    else:
        return False


def enter_record():
    t_plate = ""
    t_name = ""
    t_address = ""
    while t_plate == "":
        input_plate = input("Enter the vehicle plate number. ")
        validate_result = validate_nh_license_plate(input_plate)
        if validate_result:
            t_name = input("Enter the driver's full name. ")
            t_address = input("Enter the driver's street address. ")
            t_plate = input_plate
        else:
            print("Invalid plate number entered. Please enter a valid 7-digit plate number.")
    info = (t_plate, t_name, t_address)
    return info


def insert_record(record_tuple, plate_dic):
    new_tuple = record_tuple[1:]
    key = record_tuple[0]
    plate_dic[key] = new_tuple
    print(plate_dic)


def lookup_record(this_plate, plate_dic):
    if plate_dic.get(f"{this_plate}") is not None:
        return plate_dic[this_plate]
    else:
        return None


# enter_record()
plate_db = {}
print("Welcome to the Department of Motor Vehicles!")

while True:
    command = input("Enter a command. ")
    if command == "a":
        plate = enter_record()

        insert_record(plate, plate_db)

    elif command == "s":
        plate_to_search = input("Enter the plate number to search for > ")
        if validate_nh_license_plate(plate_to_search):
            result = lookup_record(plate_to_search, plate_db)
            if result is not None:

                name = result[0]
                address = result[1]
                print(f"Information for plate {plate_to_search}:")
                print(f"----Name: {name}")
                print(f"----Address: {address}")
            else:
                print(f"No record of plate {plate_to_search} exists")
        else:
            print("Invalid plate numbered entered. Please enter a valid 7-digit plate number")
    elif command == "p":
        for x in plate_db.keys():
            result = lookup_record(x, plate_db)
            print(f"Information for plate {x}:")
            print(f"----Name: {result[0]}")
            print(f"----Address: {result[1]}")
    elif command == "q":
        break
    else:
        print("Invalid Command")
