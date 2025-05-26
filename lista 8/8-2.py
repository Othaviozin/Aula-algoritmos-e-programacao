def horarios(hora):
    try:
        hr, min = map(int, hora.split(":"))  # Converte diretamente para inteiros
        if 0 <= hr < 24 and 0 <= min < 60:
            if hr == 0:
                return f"12:{min:02d} AM"
            elif hr < 12:
                return f"{hr}:{min:02d} AM"
            elif hr == 12:
                return f"12:{min:02d} PM"
            else:
                return f"{hr-12}:{min:02d} PM"
        else:
            return "Horário incompatível"
    except ValueError:
        return "Formato inválido. Use HH:MM"

horario = input("Digite a hora para conversão (HH:MM): ")
print(horarios(horario))
  