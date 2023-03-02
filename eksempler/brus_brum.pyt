grænse = 100

hvert n i spænd(1, grænse + 1):
    hvis n % 15 == 0:
        udskriv("BrusBrum")
    elvis n % 3 == 0:
        udskriv("Brus")
    elvis n % 5 == 0:
        udskriv("Brum")
    ellers:
        udskriv(tekst(n))
