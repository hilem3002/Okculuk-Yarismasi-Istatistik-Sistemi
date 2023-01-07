def okcu():
    PUAN_SAYISI = 11
    MIN_PUAN = 0

    # okcu sayisina giriebilecek hatali veri kontrolu
    try:
        okcu_sayisi = int(input("lutfen okcu sayisini giriniz"))
        while okcu_sayisi <= 0:
            okcu_sayisi = int(input("okcu sayisi 0 dan kucuk veya esit olamaz lutfen okcu sayisini tekrar giriniz"))

    except ValueError:
        okcu_sayisi = int(input("hatali veri girisi oldu lutfen okcu sayisini tekrar giriniz"))

    # atis hakkina giriebilecek hatali veri kontrolu
    try:
        atis_hakki = int(input("lutfen atis hakki sayisini giriniz"))
        while atis_hakki <= 0:
            atis_hakki = int(input("atis hakki o dan kucuk veya esit olamaz lutfen atis hakki sayisini tekrar giriniz"))

    except ValueError:
        atis_hakki = int(input("hatali veri girisi oldu lutfen atis hakki sayisini tekrar giriniz"))

    ruzgar_turlari_sayilari = {}
    puanlar_listesi = []

    for atis_no in range(atis_hakki):

        her_atis_puanlar_listesi = []
        okcu_icin_puan_sayilari = {}

        for okcu_no in range(okcu_sayisi):

            # puana giriebilecek hatali veri kontrolu
            puan = int(input(f"lutfen atis icin {okcu_no+1}. okcunun puanini giriniz"))
            while puan not in [0,1,2,3,4,5,6,7,8,9,10]:
                puan = int(input(f"yanlis veri girdiniz lutfen atis icin {okcu_no + 1}. okcunun puanini tekrar giriniz"))
            her_atis_puanlar_listesi.append(puan)

            # puan 0 a esit olmasi durumunda 0 atis oldugu andaki ruzgar adi aliniyor
            if puan == MIN_PUAN:
                ruzgar_turu = input("lutfen 0 puan aldiğiniz atistaki var olan ruzgarin adini giriniz")

                if ruzgar_turu in ruzgar_turlari_sayilari:
                    ruzgar_turlari_sayilari[ruzgar_turu] += 1
                else:
                    ruzgar_turlari_sayilari[ruzgar_turu] = 1

        puanlar_listesi.append(her_atis_puanlar_listesi)

    for okcu_no in range(okcu_sayisi):
        okcu_puanlari = []
        for atis_no in range(atis_hakki):
            okcu_puanlari.append(puanlar_listesi[atis_no][okcu_no])
        puanlar_listesi.append(okcu_puanlari)

    for atis_no in range(atis_hakki):
        puanlar_listesi.pop(0)

    puanlarin_sayilari = []
    toplam_puanlar = []

    for okcu_no in range(okcu_sayisi):
        puanlarin_sayilari_her_okcu = {}

        for atis_no in range(atis_hakki):

            if puanlar_listesi[okcu_no][atis_no] in puanlarin_sayilari_her_okcu:
                puanlarin_sayilari_her_okcu[puanlar_listesi[okcu_no][atis_no]] += 1
            else:
                puanlarin_sayilari_her_okcu[puanlar_listesi[okcu_no][atis_no]] = 1

        # okcularin puanlari toplaniyor
        toplam = sum(puanlar_listesi[okcu_no])
        toplam_puanlar.append(toplam)

        puanlarin_sayilari.append(puanlarin_sayilari_her_okcu)

    print("Okcu Kayit No     10p               9p               8p               7p               6p               5p               4p               3p               2p               1p               0p            Toplam Puan")
    print("-------------    -----             -----            -----            -----            -----            -----            -----            -----            -----            -----            -----          -----------")

    # her puan cesidi icin toplamlar aliniyor
    onlar_toplam = 0
    dokuzlar_toplam = 0
    sekizler_toplam = 0
    yediler_toplam = 0
    altilar_toplam = 0
    besler_toplam = 0
    dortler_toplam = 0
    ucler_toplam = 0
    ikiler_toplam = 0
    birler_toplam = 0
    sifirlar_toplam = 0

    # formatli print yaptiriliyor
    for okcu_no in range(okcu_sayisi):
        print(okcu_no+1,end="                  ")
        keyler = list(puanlarin_sayilari[okcu_no].keys())

        for puan_no in range(PUAN_SAYISI):
            if puan_no not in keyler:
                (puanlarin_sayilari[okcu_no])[puan_no] = 0
        son_puan_sayisi_listesi_sirasiz = puanlarin_sayilari[okcu_no]

        for puan_no in range(PUAN_SAYISI+1,1,-1):
            print(son_puan_sayisi_listesi_sirasiz[puan_no-2],end="                ")
        print(toplam_puanlar[okcu_no])
        print()

        onlar_toplam += son_puan_sayisi_listesi_sirasiz[10]
        dokuzlar_toplam += son_puan_sayisi_listesi_sirasiz[9]
        sekizler_toplam += son_puan_sayisi_listesi_sirasiz[8]
        yediler_toplam += son_puan_sayisi_listesi_sirasiz[7]
        altilar_toplam += son_puan_sayisi_listesi_sirasiz[6]
        besler_toplam += son_puan_sayisi_listesi_sirasiz[5]
        dortler_toplam += son_puan_sayisi_listesi_sirasiz[4]
        ucler_toplam += son_puan_sayisi_listesi_sirasiz[3]
        ikiler_toplam += son_puan_sayisi_listesi_sirasiz[2]
        birler_toplam += son_puan_sayisi_listesi_sirasiz[1]
        sifirlar_toplam += son_puan_sayisi_listesi_sirasiz[0]

    print("tum Okcular(%)",end="    ")
    genel_toplam = onlar_toplam + dokuzlar_toplam + sekizler_toplam + yediler_toplam + altilar_toplam + besler_toplam + dortler_toplam + ucler_toplam + ikiler_toplam + birler_toplam + sifirlar_toplam
    print(f"{onlar_toplam/genel_toplam*100:.2f},%",end="           ")
    print(f"{dokuzlar_toplam/genel_toplam*100:.2f},%",end="           ")
    print(f"{sekizler_toplam/genel_toplam*100:.2f},%",end="           ")
    print(f"{yediler_toplam/genel_toplam*100:.2f},%",end="           ")
    print(f"{altilar_toplam/genel_toplam*100:.2f},%",end="           ")
    print(f"{besler_toplam/genel_toplam*100:.2f},%",end="           ")
    print(f"{dortler_toplam/genel_toplam*100:.2f},%",end="           ")
    print(f"{ucler_toplam/genel_toplam*100:.2f},%",end="           ")
    print(f"{ikiler_toplam/genel_toplam*100:.2f},%",end="           ")
    print(f"{birler_toplam/genel_toplam*100:.2f},%",end="           ")
    print(f"{sifirlar_toplam/genel_toplam*100:.2f},%")
    print()

    print("Ruzgar adi",end="     ")
    print("Iska atis orani(%)")
    print("------------",end="   ")
    print("--------------------")
    ruzgar_isimleri = list(ruzgar_turlari_sayilari.keys())
    for ruzgar_no in range(len(ruzgar_turlari_sayilari)):
        print(ruzgar_isimleri[ruzgar_no],end="       ")
        ruzgar_orani = ruzgar_turlari_sayilari[ruzgar_isimleri[ruzgar_no]]/sum(ruzgar_turlari_sayilari.values())*100
        print(f"{ruzgar_orani:.2f},%")
        print()

okcu()
