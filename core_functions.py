############################################
# Это файл, содержащий функции с формулами #
############################################


# Настройка и вывод в лог #

version = 'Pre-Alpha Build'

def response():
    return True

# ------------------------#


#Инструкции#

def return_the_instructions(var):
        if var == 'V':
            return ['test', 'test']

        if var == 'a':
            return ['test', 'test']

######


# функция берет массив инструкций и словарь переменных
# и ищет инстукцию в которой все переменные известны

def check_instr(list_inst, variable):
    # значения из variable
    values_var_list = list(dict.values(variable))

    # ключи из variable
    keys_var_list = list(dict.keys(variable))

    number = len(list_inst)

    error_inst = []
    good_inst = None

    i = 0
    a = 0
    # определяет номер инструкции в которой есть неизвестная перменная

    for a in range(number):
        for i in range(len(keys_var_list)):
            if keys_var_list[i] in list_inst[a]:
                if values_var_list[i] == None:
                    error_inst.append(a)
                    i = 0
                    a += 1
                    break

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


def doing_inst(good_inst, list_inst, var):
    if good_inst == None:
        return 'абракадабра'
    else:
        z = 0
        var = eval(list_inst[good_inst])
        return var

