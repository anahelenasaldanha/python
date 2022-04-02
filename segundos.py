segs_str = input ("Por favor, entre com o número de segundos que deseja converter ")
segs_total = int(segs_str)

dias = segs_total // 86400
dias_rest = segs_total % 86400
horas = dias_rest // 3600
horas_rest = dias_rest % 3600
minutos = horas_rest // 60
segundos = horas_rest % 60

print(dias,"dias,",horas,"horas,",minutos,"minutos e",segundos,"segundos.")



