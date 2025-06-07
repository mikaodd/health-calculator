# 綜合健康計算機
def get_bmi (height, weight):
    height /= 100
    bmi = weight / height ** 2
    bmi = round(bmi, 1)
    return bmi

def get_bmr(sex, height, weight, age):
    if sex == '男':
        bmr = 66 + (13.7*weight + 5*height - 6.8*age)
    else:
        bmr = 655 + (9.6*weight + 1.8*height - 4.7*age)
    bmr = round(bmr, 2)
    return bmr

def get_tdee(sex, height, weight, age, times):
    bmr = get_bmr(sex, height, weight, age)
    tdee = bmr * times
    tdee = round(tdee, 2)
    return tdee

while True:
    print('-歡迎使用綜合健康計算機-')
    print('(1)計算BMI')
    print('(2)計算基礎代謝率(BMR)')
    print('(3)計算總熱量消耗(TDEE)')
    print('(Q)離開')
    choice = input('請選擇要計算的項目(輸入1 or 2 or 3 or Q)').strip().upper()

    if choice == '1':
        height = float(input('請輸入你的身高(公分):'))
        weight = float(input('請輸入你的體重(公斤):'))
        bmi = get_bmi(height, weight)
        print(f'您的BMI是:{bmi}')
    elif choice == '2':
        sex = input('請輸入你的性別(男or女):').strip()
        height = float(input('請輸入你的身高(公分):'))
        weight = float(input('請輸入你的體重(公斤):'))
        age = int(input('請輸入你的年齡:'))
        bmr = get_bmr(sex, height, weight, age)
        print(f'您的基礎代謝率(BMR)是:{bmr}')
    elif choice == '3':
        sex = input('請輸入你的性別(男or女):').strip()
        height = float(input('請輸入你的身高(公分):'))
        weight = float(input('請輸入你的體重(公斤):'))
        age = int(input('請輸入你的年齡:'))
        print('(1)沒在運動\n(2)1週運動1-3天\n(3)1週運動3-5天\n(4)1週運動6-7天\n(5)每天動')
        exer = input('選擇您的運動量(輸入1~5):')
        act_dict = {
            '1':1.2,
            '2':1.375,
            '3':1.55,
            '4':1.725,
            '5':1.9,
        }
        times = act_dict.get(exer)
        if times is None:
            print('輸入錯誤,請重新輸入')
            continue
        tdee = get_tdee(sex, height, weight, age, times)
        print(f'您的總熱量消耗(TDEE)是:{tdee}')
    elif choice == 'Q':
        print('感謝使用,再見!')
        break
    else:
        print('輸入錯誤,請重新輸入!')