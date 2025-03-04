myfamily = {
    "1234": {
        "detail": {
            "profile": {
                "name": "Alex",
                "contact no": "8876987455",
                "age": "23"
            },
            "education": {
                "school": "state",
                "College": "Government"
            },
            "skills": {
                "primary": "frontend",
                "secondary": "Marketing"
            }
        }
    },
    "2345": {
        "detail": {
            "profile": {
                "name": "Godf",
                "contact no": "9876887425",
                "age": "25"
            },
            "education": {
                "school": "10Th",
                "College": "Arts"
            },
            "skills": {
                "primary": "HTML",
                "secondary": "JS"
            }
        }
    }
}

def myfun(x, obj="name"):
    if x in myfamily:
        detail = myfamily[x]["detail"]
        
        for category in detail:
            if obj in detail[category]:
                print(detail[category][obj])
                return
        
    print("Invalid key")

myfun("1234", "school")  
myfun("2345", "primary") 
