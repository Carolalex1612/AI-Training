class DictionaryUpdater:
    def __init__(self, dict_list):
        self.dict_list = dict_list

    def update_dicts(self, id, key, value, option):
        for d in self.dict_list:
            if d.get("id") == id:  
                if option == "add":    
                    d[key] = value  
                elif option == "delete":
                    if key in d:
                        d.pop(key)
                    else:
                        print(f"Key '{key}' not found in dictionary with id '{id}'.")

dict_list = [
    {"id": "001", "brand": "Ford", "model": "Mustang"},
    {"id": "002", "brand": "Volkswagen", "model": "Virtus"},
    {"id": "003", "brand": "Maruti", "model": "800"},
]

updater = DictionaryUpdater(dict_list)

updater.update_dicts("001", "year", 1993, "add")
print(dict_list) 

updater.update_dicts("001", "year", None, "delete")
print(dict_list)  
