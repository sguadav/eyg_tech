import datetime
import pytz
import calendar

PTY = pytz.timezone('America/Panama')

greens_data = {
    'girasol': 44,
    'guisante': 48,
    'brocoli': 46,
    'rabano': 48,
    'ssm': 46,
    'cilantro': 144,
    'berr2': 72,
    'albahaca': 60,
    'gui2': 72
}

months = {
    '1': 'Enero',
    '2': 'Febrero',
    '3': 'Marzo',
    '4': 'Abril',
    '5': 'Mayo',
    '6': 'Junio',
    '7': 'Julio',
    '8': 'Agosto',
    '9': 'Septiembre',
    '10': 'Octubre',
    '11': 'Noviembre',
    '12': 'Diciembre'
}

months_inverted = {
    'Enero': '1',
    'Febrero': '2',
    'Marzo': '3',
    'Abril': '4',
    'Mayo': '5',
    'Junio': '6',
    'Julio': '7',
    'Agosto': '8',
    'Septiembre': '9',
    'Octubre': '10',
    'Noviembre': '11',
    'Diciembre': '12'
}

def get_current_time():
    return datetime.datetime.now(PTY)

def print_datetime(curr_time=None):
    if curr_time.time().hour > 12:
        new_hour = curr_time.time().hour - 12
        if curr_time.time().minute < 10:
            new_minute = '0' + str(curr_time.time().minute)
        else:
            new_minute = str(curr_time.time().minute)
        print(f"El {curr_time.date().day} de {months[str(curr_time.date().month)]}, a las {new_hour}:{new_minute} PM")
    else:
        print(f"El {curr_time.date().day} de {months[str(curr_time.date().month)]}, a las {curr_time.time().hour}:{curr_time.time().minute} AM")

    return

def calculate_time_germination(green_product, inserted_datetime=None):
    if inserted_datetime is None:
        current_time = get_current_time()
        time_to_germination = datetime.timedelta(hours=greens_data[green_product])
        germination_date = current_time + time_to_germination
    else:
        time_to_germination = datetime.timedelta(hours=greens_data[green_product])
        germination_date = inserted_datetime + time_to_germination
    return germination_date

def main_calculator(green_original=None):
    print("--------------------------------------------------")
    print("                 Eat Your Greens                \n")
    print("             Calculadora de germinacion         \n")
    print("--------------------------------------------------")
    print("\nLista de productos:                             ")
    print("- Girasol (GIR)                                   ")
    print("- Guisante (GUI)                                  ")
    print("- Brocoli (BRO)                                   ")
    print("- Rabano (RAB)                                    ")
    print("- Spicy Salad Mix (SSM)                           ")
    print("- Cilantro (CIL)                                  ")
    print("- Berro 2 (BERR2)                                 ")
    print("- Albahaca (ALB)                                  ")
    print("- Guisante 2 (GUI2)                             \n")

    repeat_order = True
    while repeat_order:
        repeat_product_inquiry = True

        while repeat_product_inquiry: 
            print("Usando los nombres o abreviaciones de arriba.")
            print("Que producto desea calcular el tiempo de germinacion?")
            green_original = input('- ')
            print()
            green = green_original.lower().rstrip().replace(' ', '')

            if green not in greens_data.keys():
                if green == 'spicysaladmix' or green == 'spicysaladmix(ssm)':
                    green = 'ssm'
                    repeat_product_inquiry = False
                elif green == 'berro2' or green == 'berro2(berr2)':
                    green = 'berr2'
                    repeat_product_inquiry = False
                elif green == 'gir' or green == 'girasol(gir)':
                    green = 'girasol'
                    repeat_product_inquiry = False
                elif green == 'gui' or green == 'guisante(gui)':
                    green = 'guisante'
                    repeat_product_inquiry = False
                elif green == 'bro' or green == 'brocoli(bro)':
                    green = 'brocoli'
                    repeat_product_inquiry = False
                elif green == 'rab' or green == 'rabano(rab)':
                    green = 'rabano'
                    repeat_product_inquiry = False
                elif green == 'cil' or green == 'cilantro(cil)':
                    green = 'cilantro'
                    repeat_product_inquiry = False
                elif green == 'alb' or green == 'albahaca(alb)':
                    green = 'albahaca'
                    repeat_product_inquiry = False
                elif green == 'guisante2' or green == 'guisante2(gui2)':
                    green = 'gui2'
                    repeat_product_inquiry = False
                else: 
                    print("### ATENCION: El nombre introducido no fue reconocido, por favor intente otra vez ###\n ")
            else:
                repeat_product_inquiry = False

        print("\nSi desea ingresar el dia y hora de comienzo, inserte 'Si'. Inserte 'No' si desea usar la hora actual.")
        is_time_inserted = input('- ').lower().rstrip()
        inserted_datetime = None

        if is_time_inserted == 'si':
            print("\nIngrese el mes de siembra")
            time_inserted_month = int(months_inverted[input('- ').capitalize()])
            print("\nIngrese el numero del dia de siembra")
            time_inserted_day = int(input('- '))
            print("\nIngrese la hora de siembra")
            time_inserted_hour = int(input('- '))
            print("\nIngrese el minuto de siembra")
            time_inserted_minute = int(input('- '))
            print("\nIngrese 'AM' o 'PM'")
            time_inserted_ampm = input('- ').upper()

            if time_inserted_ampm == 'PM':
                time_inserted_hour += 12

            inserted_datetime = datetime.datetime(
                year=2023,
                month=time_inserted_month, 
                day=time_inserted_day, 
                hour=time_inserted_hour, 
                minute=time_inserted_minute
                )

        print(f"\nUsted ha ingresado el producto '{green_original}', el programa lo procesa como '{green}'.\n")
        print("Calculando tiempo para producto...\n")

        germination_date = calculate_time_germination(green_product=green, inserted_datetime=inserted_datetime)
        print(f"La germinacion del producto {green_original} termina:")
        print_datetime(germination_date)

        print("\nQuiere hacer otro calculo con un nuevo producto? Si o No?")
        repeat_answer = input('- ').lower()
        print()
        if repeat_answer != 'si':
            repeat_order = False
    print("\nListo.\n")
    return germination_date


if __name__ == '__main__':
    main_calculator()
    # To run file: 'python3 time_calculator.py'

    # To instal;:
    # python3 -m pip install datetime
    # python3 -m pip install pytz