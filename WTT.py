

Idioma = input('Si hablas español por favor, escribe Si \nIf you speak english please write Yes ')


if Idioma == 'Si':

    num_caps = int(input('Inserte el número total de capitulos: '))

    duracion_prom = int(input('Inserte el tiempo promedio de duración en minutos de cada cápitulo: '))

    minutos = num_caps * duracion_prom 

    horas = minutos // 60
    minutos_resto = minutos % 60

    print(f'El total de horas y minutos a ver es de {horas}h y {minutos_resto} minutos')

else:

    num_caps = int(input('Please enter the total of episodes: '))

    duracion_prom = int(input('Please enter the average time of each episode in minutes: '))

    minutos = num_caps * duracion_prom 

    horas = minutos // 60
    minutos_resto = minutos % 60

    print(f'The total of hours and minutes to watch its {horas}h and {minutos_resto} minutes')








