import copy
def build_inventory():
    return [
        {"name":"Laptop","info":{"cost":50000,"quantity":10,"vendor":{"rating":4.5}}},
        {"name":"Phone","info":{"cost":20000,"quantity":25,"vendor":{"rating":4.2}}}
    ]
def update_inventory(data_list,reg_no):
    size=len(data_list)
    position=reg_no%size
    for j in range(size):
        if j==position:
            data_list[j]["info"]["cost"]=int(data_list[j]["info"]["cost"]*0.9)
            data_list[j]["info"]["quantity"]+=5
    return data_list
def analyze_changes(original_data,modified_data):
    modified_items=[]
    same_items=[]
    for k in range(len(original_data)):
        if original_data[k]!=modified_data[k]:
            modified_items.append(original_data[k]["name"])
        else:
            same_items.append(original_data[k]["name"])
    return modified_items,same_items
reg_no=24110011666
main_inventory=build_inventory()
copy_shallow=main_inventory.copy()
copy_deep=copy.deepcopy(main_inventory)
update_inventory(copy_shallow,reg_no)
update_inventory(copy_deep,reg_no)
print("Original Data:",main_inventory)
print("Shallow Version:",copy_shallow)
print("Deep Version:",copy_deep)
sh_mod,sh_same=analyze_changes(main_inventory,copy_shallow)
dp_mod,dp_same=analyze_changes(main_inventory,copy_deep)
print("\nChanges Analysis:")
print("Shallow Modified:",sh_mod)
print("Shallow Unchanged:",sh_same)
print("Deep Modified:",dp_mod)
print("Deep Unchanged:",dp_same)
print("\nFinal Count (Tuple):")
print("Shallow:",(len(sh_mod),len(sh_same)))
print("Deep:",(len(dp_mod),len(dp_same)))