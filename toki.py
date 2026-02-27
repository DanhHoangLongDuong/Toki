import sys
import time



def focusTime(focus):
    print("""
　　　　　 ／＞　　フ 
　　　　　 | 　_　_|
　 　　　／` ミ＿xノ  
　　 　 /　　　   |
　　　 /　 ヽ　　 ﾉ
      │　   |　|　|
　／￣|　　 |　|　|
　| (￣ヽ＿_ヽ_)__)
　＼二つ
    """)

    print("""
   __                     
  / _|                    
 | |_ ___   ___ _   _ ___ 
 |  _/ _ \\ / __| | | / __|
 | || (_) | (__| |_| \\__ \\
 |_| \\___/ \\___|\\__,_|___/
        """)

    while focus:
        mins, secs = divmod(focus, 60)
        timer = '{:02d}:{:02d}'.format(mins, secs)
        print(timer, end='\r')
        time.sleep(1)
        focus -= 1


def clear(r):
    for i in range(r):
        sys.stdout.write("\033[1A\033[K")
        sys.stdout.flush()

def restTime(rest):
    print("""
          
                _   
  _ __ ___  ___| |_ 
 | '__/ _ \\/ __| __|
 | | |  __/\\__ \\ |_ 
 |_|  \\___||___/\\__|
        """)
    while rest:
        mins, secs = divmod(rest, 60)
        timer = '{:02d}:{:02d}'.format(mins,secs)
        print(timer, end='\r')
        time.sleep(1)
        rest -= 1

    

print("""\
  _______ ____  _  _______ 
 |__   __/ __ \\| |/ /_   _|
    | | | |  | | ' /  | |  
    | | | |  | |  <   | |  
    | | | |__| | . \\ _| |_ 
    |_|  \\____/|_|\\_\\_____|                          
""")

count = 0
focus = int(input("Enter focus time (in second): "))
rest = int(input("Enter resting time: "))

while True: 
    focusTime(focus)
    clear(8)
    restTime(rest)
    count += 1
    confirm = input("Continue? (Y/N)")
    sys.stdout.flush()
    if confirm == "N" or confirm == "n":
        print(f"you completed {count} cycles!")
        break
    elif confirm == "Y" or confirm == "y":
        clear(20)
