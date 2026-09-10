def zeg_hallo(aantal):
    tekst = ""

    for getal in range(1, aantal + 1):
        tekst += f"Hello from function town {getal}!\n"
    return tekst

print(zeg_hallo(3))