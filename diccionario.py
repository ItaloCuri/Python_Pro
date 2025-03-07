for i in range(5):
    print("...")
    meme_dict = {
                "CRINGE": "Algo excepcionalmente raro o embarazoso",
                "LOL": "Una respuesta común a algo gracioso",
                "CREEPY": "Aterrador,siniestro",
                "XD": "algo gracioso",
                "EZ": "facilisimo/fue muy facil de ganarte(solo para juegos)"
                "ZZZ": "eres aburrido/me aburri"
                "BODRIO": "algo o alguien es aburrido"
                }

    word = input("Escribe una palabra que no entiendas (¡con mayúsculas!): ")

    if word in meme_dict.keys():
        # ¿Qué debemos hacer si se encuentra la palabra?
        print(meme_dict[word])
    
    else:
        # ¿Qué hacer si no se encuentra la palabra
        print("no se encuentra o aun no esta")
