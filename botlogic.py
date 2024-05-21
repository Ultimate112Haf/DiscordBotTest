import random

def pass_gen(pass_lenght):
    character = "+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"


    password = ""


    for char in range(pass_lenght):
        password += random.choice(character)

    return password

def emoji_gen():
    emoji = [":grinning:", ":sweat_smile:", ":watermelon:", ":cold_face:"]
    return random.choice(emoji)

#kegunaan untuk mengerjakan tugas sekolah dan pingin ngasal karena bingung
def capcipcup():
    pilihan = ["PilihA", "PilihB", "PilihC", "PilihD"]
    return random.choice(pilihan)

def randomnumber():
    rn = random.randint(0,10)
    return rn

if __name__ == "__main__":
    print(pass_gen(10))

