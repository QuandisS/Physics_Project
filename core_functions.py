############################################
# Это файл, содержащий функции с формулами #
############################################

import cmath
import math

############################################
# Переменнная отвечающая за знак по которому осуществляется поиск неизвестных
############################################

sign_var = '-'

############################################
############################################

# Настройка и вывод в лог #

version = 'Pre-Alpha Build'
def response():
    return True

# ------------------------#


#Инструкции#

def return_the_instructions(var):
        if var == 'v0':
            return ['v0x / cos_a', 'v0y / sin_a', '( x - x0 ) / ( cos_a * t ) ', '( L - x0 ) / ( cos_a * t_all )', '( y - y0 + g * t * t / 2 ) / ( sin_a * t )', '( t_all * g ) / ( 2 * sin_a )', 'math.sqrt( ( 2 * g ) / cmath.sin( 2 * alpha ) )', '( vy + g * t ) / sin_a', 'math.sqrt( vy * vy + 2 * g * y ) / sin_a', 'math.sqrt( h_max * 2 * g ) / sin_a']

        if var == 'alpha':
            return ['math.radians( cmath.acos ( cos_a ) )', 'math.radians( cmath.asin ( sin_a ))', 'math.radians( cmath.asin( ( ( L * g ) / ( v0 * v0 )) / 2 )', 'math.radians( math.sqrt( cmath.asin( ( h_max * 2 * g ) / ( v0 * v0 ) ) ))']

        if var == 'g':
            return ['M * G / ( r * r )']

        if var == 'v0x':
            return ['v0 * cos_a', '( x - x0 ) / t', '( L - x0 ) / t_all']

        if var == 'v0y':
            return ['v0 * sin_a', '( y - y0 + g * t * t / 2 ) / t', 't_all * g / 2', 'vy + g * t', 'math.sqrt( vy * vy + 2 * g * y )', 'math.sqrt( h_max * 2 * g )']

        if var == 'vy':
            return ['v0y - g * t', 'v0 * sin_a - g * t', 'math.sqrt( v0y * v0y - 2 * g * y )']

        if var == 't_all':
            return ['( L - x0 ) / ( v0 * cos_a )', '( L - x0 ) / v0x']

        if var == 't':
            return ['( v0y - vy ) / g', '( v0y - v0 * sin_a ) / g', '( x - x0 ) / v0x', '( x - x0 )  / v0 * cos_a']

        if var == 'h_max':
            return ['y0 + v0 * sin_a * 0.5 * t_all - 0.25 * g * t_all * t_all / 2', 'y0 + v0y * 0.5 * t_all - 0.25 * g * t_all * t_all / 2']

        if var == 'x0':
            return ['x - vox * t', 'x - v0 * cos_a * t', 'L - v0 * cos_a * t_all', 'L - v0x * t_all']

        if var == 'x':
            return ['x0 + v0x * t', 'x0 + v0 * cos_a * t']

        if var == 'y0':
            return ['y - v0y * t + g * t * t / 2', 'y - v0 * sin_a * t + g * t * t / 2', 'h_max - v0y * 0.5 * t_all + 0.25 * g * t_all * t_all / 2', 'h_max - v0 * sin_a * 0.5 * t_all + g * t_all * 0.25 * t_all / 2']

        if var == 'y':
            return ['y0 + v0y * t - g * t * t / 2', 'y0 + v0 * sin_a * t - g * t * t / 2', '( vy * vy - v0y * v0y ) / ( -2 * g )', '( vy * vy - v0 * sin_a * v0 * sin_a ) / ( -2 * g )']

        if var == 'L':
            return ['x0 + v0 * cos_a * t_all', 'x0 + v0x * t_all', 'v0 * v0 * math.sin( alpha * 2 ) / g']

        if var == 'F':
            return ['test', 'test']

        if var == 'm':
            return ['test', 'test']

        if var == 'sin_a':
            return ['cmath.sin( alpha )', 'v0y / v0', '( y - y0 + g * t * t / 2 ) / ( v0 * t )', 't_all * g / ( 2 * v0 )', '( t * g + vy ) / v0', 'math.sqrt( h_max * 2 * g ) / v0']

        if var == 'cos_a':
            return ['v0x / v0', '( L - x0 ) / ( v0 * t_all )', '( x - x0 ) / ( v0 * t )', 'cmath.cos( alpha )']


######


# функция берет массив инструкций и словарь переменных
# и ищет инстукцию в которой все переменные известны
def check_instr(list_inst, variable):
    # значения из variable
    values_var_list = list(dict.values(variable))

    # ключи из variable
    keys_var_list = list(dict.keys(variable))

    s_lenght_inst = []

    error_inst = []
    good_inst = None

    i = 0
    a = 0

    # разделение инструкций для исключения неправильной работы ф-ции
    # раньше не было отличия между  v0 и v0_x
    for i in range(len(list_inst)):
        s_lenght_inst.append(list_inst[i].split())
        i += 1

    i = 0

    number = len(s_lenght_inst)

    # определяет номер инструкции в которой есть неизвестная перменная

    for a in range(number):
        for i in range(len(keys_var_list)):
            if keys_var_list[i] in s_lenght_inst[a]:
                try:
                    if values_var_list[i] == sign_var:
                        error_inst.append(a)
                        i = 0
                        a += 1
                        break
                except Exception:
                    error_inst.append(a)
                    i = 0
                    a += 1
                    break
            # elif keys_var_list[i] == 't' or keys_var_list[i] == 'vy' or keys_var_list[i] == 'x' or keys_var_list[i] == 'y':
            #     try:
            #         if type(variable[keys_var_list[i]]) != int:
            #             error_inst.append(a)
            #             i = 0
            #             a += 1
            #             break
            #     except Exception:
            #         error_inst.append(a)
            #         i = 0
            #         a += 1
            #         break
    # определяет номер хорошей инструкции
    a = 0
    for a in range(number):
        if a in error_inst:
            a += 1
        else:
            good_inst = a
            break

    return good_inst


# функция принимает номер нормальной инструкции, массив интрукций, название переменной к которой относятся инструкции


def doing_inst(good_inst, list_inst, global_vars):

    v0 = global_vars["v0"]
    alpha = global_vars["alpha"]
    sin_a = global_vars["sin_a"]
    cos_a = global_vars["cos_a"]
    v0x = global_vars["v0x"]
    v0y = global_vars["v0y"]
    try:
        vy = global_vars["vy"]
    except Exception:
        pass
    t_all = global_vars["t_all"]
    L = global_vars["L"]
    h_max = global_vars["h_max"]
    try:
        x = global_vars["x"]
    except Exception:
        pass
    x0 = global_vars["x0"]
    try:
        y = global_vars["y"]
    except Exception:
        pass
    y0 = global_vars["y0"]
    g = global_vars["g"]
    try:
        t = global_vars["t"]
    except Exception:
        pass
    M = global_vars["M"]
    G = global_vars["G"]
    r = global_vars["r"]


    if good_inst == None:
        return 'абракадабра'
    else:
        z = 0
        try:
            var = eval(list_inst[good_inst])
            return var
        except Exception as ex:

            #if hasattr(ex, 'message'):
            #    return ex.message
            #else:

                return ex


def consid_coord(global_vars, times):
    coord =[]

    good_instr = 0

    global_vars["t"] = times
    try:
        global_vars["x"] = doing_inst(good_instr, return_the_instructions("x"), global_vars)
    except Exception:
        return 'Heresy in var x'
    try:
        global_vars["y"] = doing_inst(good_instr, return_the_instructions("y"), global_vars)
    except Exception:
        return 'Heresy in var y'

    coord.append(global_vars["x"])
    coord.append(global_vars["y"])

    return coord


def gravity(gravity_constant, planet_mass, planet_radius, y):

    try:
        g = gravity_constant * planet_mass / ((planet_radius + y) * (planet_radius + y))
    except Exception:
        return "Heresy in var g"

    return g

def log_add_value(global_vars):

    a = "Начальная скорость : " + global_vars["v0"] + " m/c" + "\n"
    b = "Скорость по оси X : " + global_vars["v0x"] + " m/c"+ "\n"
    c ="Скорость по оси Y : " + global_vars["v0y"] + "m/c"+ "\n"
    d = "Угол броска : " + global_vars["alpha"] + " degrees"+ "\n"
    e = "Время полета : " + global_vars["t_all"] + " c"+ "\n"
    f = "Дальность полета : " + global_vars["L"] + " m"+ "\n"
    i = "Масса тела : " + global_vars["m"] + " kilograms"+ "\n"
    j = "Максимальная высота : " + global_vars["h_max"] + " m"+ "\n"
    k = "Начальные координаты : " + global_vars["x"] + " " + global_vars["y"] +"\n"
    l ="Сила броска : " + global_vars["F"] + " N" + "\n"

    all = a + b + c + d + e + f + i + j + k + l
    return all
