segundos_str = input("Por favor, entre com o número de segundos que deseja converter: ")
total_segs = int(segundos_str)

dias = total_segs // (3600 * 24)
segs_restantes_dias = total_segs % (3600 * 24)

horas = segs_restantes_dias // 3600
segs_restantes_hora = segs_restantes_dias % 3600

minutos = segs_restantes_hora // 60
segs_restante_final = segs_restantes_hora % 60

print(dias, "dias, ", horas, "horas, ", minutos, "minutos e", segs_restante_final, "segundos.")