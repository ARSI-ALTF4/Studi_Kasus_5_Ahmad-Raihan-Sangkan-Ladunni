def hitung_biaya_hotel(jenis, lama):
    if jenis == "Standard":
        tarif = 200000

    elif jenis == "Deluxe":
        tarif = 400000

    else: tarif = 0
    total = tarif * lama
    return total


