jautajumi = [

["Kur es visbiežāk pavadīju laiku vasarā?",["A Pie jūras","B Pie datora","C Laukos","D Ārā ar draugiem"],"C"],
["Kurā Latvijas ezerā es šovasar peldējos?",["A Lubānā","B Rāznas ezerā","C Usmas ezerā","D Burtnieku ezerā"],"A"],
["Ar ko es pārsvarā pārvietojos vasarā?",["A Ar velosipēdu","B Ar mašīnu","C Ar vilcienu","D Ar motociklu"],"D"],
["Kādu filmu žanru skatījos visvairāk?",["A Komēdijas","B Šausmenes","C Dokumentālās","D Animācijas"],"A"],
["Kuru sporta spēli spēlēju ar draugiem?",["A Volejbolu","B Basketbolu","C Futbolu","D Kriketu"],"B"],
["Kuru augli es visbiežāk ēdu vasarā?",["A Banānu","B Arbūzu","C Ābolu","D Mango"],"A"],
["Kuru Latvijas pilsētu visbiežāk apmeklēju vasarā?",["A Ogri","B Liepāju","C Valku","D Rēzekni"],"D"],
["Kādu artistu visbiežāk klausījos vasarā?",["A Ansi","B Eoliku","C Wiesuli","D Kastrāciju"],"C"],
["Kādu jaunu prasmi es apguvu vasarā?",["A Gatavot ēst","B Paraut ratā","C Zīmēt","D Nekādu"],"D"],
["Uz kurieni es visbiežāk braucu ar moci vasarā?",["A Uz sporta zāli","B Uz veikalu","C Pie draugiem","D Uz purvu"],"A"],

]

punkti = 0

for i, q in enumerate (jautajumi, 1):
    print(f"{i}. {q[0]}")
    for opcijas in q[1]:
        print(opcijas)
    atbilde = input ("Tava atbilde (A/B/C/D):").strip().upper()
    if atbilde == q[2]:
        print("Pareizi!")
        punkti += 1
    else:
        print(f"Nepareizi, pareizā atbilde: {q[2]}")

print(f"\nTests pabeigts! Tavi punkti: {punkti}/{len(jautajumi)}")