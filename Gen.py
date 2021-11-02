from discord_webhook 
import DiscordWebhook
import requests
import random
import string
import time
import os

class NitroGen: 
    def __init__(self): 
        self.fileName = "Nitro gen.txt" 

    def main(self): 
        os.system('cls' if os.name == 'nt' else 'clear')

        print("""   ______      _____  _____ _____  _    _ _   _
 |  ____/\   |  __ \|_   _|  __ \| |  | | \ | |
 | |__ /  \  | |__) | | | | |  | | |  | |  \| |
 |  __/ /\ \ |  _  /  | | | |  | | |  | | . ` |
 | | / ____ \| | \ \ _| |_| |__| | |__| | |\  |
 |_|/_/    \_\_|  \_\_____|_____/ \____/|_| \_|
                                               
                                               

                                                        """) 
        time.sleep(2) 
        self.slowType("Made by: Faridun AKA FullScopeJedi6", .02)
        time.sleep(1) 
        self.slowType("\nOk now just type how many codes do u wanna generate the max limit it 7mil at a time: ", .02, newLine = False)

        num = int(input('')) 

      
        self.slowType("\nDo you wanna to use a discord webhook? \nIf so type it here or press [enter] to ignore: ", .02, newLine = False)
        url = input('') 
        webhook = url if url != "" else None 

        print()

        valid = []
        invalid = 0

        for i in range(num): 
            code = "".join(random.choices(
                string.ascii_uppercase + string.digits + string.ascii_lowercase,
                k = 16
            ))
            url = f"https://discord.gift/{code}"

            result = self.quickChecker(url, webhook) 

            if result: 
                valid.append(url)
            else: 
                invalid += 1 

            if result and webhook is None: 
                break 


        print(f"""
Results:
 Valid: {len(valid)}
 Invalid: {invalid}
 Valid Codes: {', '.join(valid )}""") 

        input("\nThe end! Press Enter 6 times to close the program.") 
        [input(i) for i in range(4,0,-1)]  


    def slowType(self, text, speed, newLine = True): 
        for i in text: 
            print(i, end = "", flush = True) 
            time.sleep(speed) 
        if newLine:
            print() 

    def generator(self, amount): 
        with open(self.fileName, "w", encoding="utf-8") as file: 
            print("Wait, Generating for you") 

            start = time.time() 

            for i in range(amount): 
                code = "".join(random.choices(
                    string.ascii_uppercase + string.digits + string.ascii_lowercase,
                    k = 16
                )) 

                file.write(f"https://discord.gift/{code}\n") 

            
            print(f"Genned {amount} codes | Time taken: {round(time.time() - start, 5)}s\n") 

    def fileChecker(self, notify = None): 
        valid = []
        invalid = 0 
        with open(self.fileName, "r", encoding="utf-8") as file: 
            for line in file.readlines(): 
                nitro = line.strip("/n") 

                
                url = f"https://discordapp.com/api/v6/entitlements/gift-codes/{nitro}?with_application=false&with_subscription_plan=true"

                response = requests.get(url)

                if response.status_code == 200: 
                    print(f" Valid | {nitro} ") 
                    valid.append(nitro) 

                    if notify is not None:
                        DiscordWebhook( 
                            url = notify,
                            content = f"congrats bro, u got the correct code! @everyone \n{nitro}"
                        ).execute()
                    else: 
                        break 

                else: 
                    print(f" Invalid | {nitro} ") 
                    invalid += 1

        return {"valid" : valid, "invalid" : invalid} 

    def quickChecker(self, nitro, notify = None): 
        url = f"https://discordapp.com/api/v6/entitlements/gift-codes/{nitro}?with_application=false&with_subscription_plan=true"
        response = requests.get(url) 

        if response.status_code == 200: 
            print(f" Valid | {nitro} ") 

            if notify is not None: 
                DiscordWebhook(
                    url = notify,
                    content = f"Valid Nito Code detected! @everyone \n{nitro}"
                ).execute()

            return True

        else: 
            print(f" Invalid | {nitro} ") 
            return False 

if __name__ == '__main__':
    Gen = NitroGen() 
    Gen.main()
