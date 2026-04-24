from modelos.servicios_derivados import ReservaSala, AlquilerEquipo, AsesoriaEspecializada

sala = ReservaSala("Sala", 50000)
equipo = AlquilerEquipo("Laptop", 30000)
asesoria = AsesoriaEspecializada("Consultoría", 80000)

print("Sala:", sala.calcular_costo(2))
print("Equipo:", equipo.calcular_costo(2))
print("Asesoría:", asesoria.calcular_costo(2))