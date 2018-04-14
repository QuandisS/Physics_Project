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

class math_extension():
    def __init__(self, used_instr, var):
        self.used_instr = used_instr
        self.var = var
    def show_ext(self):
        print("Math  extension")
        print("Used instr:", self.used_instr)
        print("Var:", self.var)


# функция берет массив инструкций и словарь переменных
# и ищет инстукцию в которой все переменные известны

unknown = math_extension

def check_instr(list_inst, variable):
    # значения из variable
    values_var_list = list(dict.values(variable))

    # ключи из variable
    keys_var_list = list(dict.keys(variable))

    error_inst = []

    i = 0
    a = 0
    # определяет номер инструкции в которой есть неизвестная перменная

    for a in range(len(list_inst)):
        for i in range(len(keys_var_list)):
            if keys_var_list[i] in list_inst[a]:
                if values_var_list[i] == None:
                    error_inst.append(a)
                    i = 0
                    a += 1
                    break

    return error_inst

# функция принимает номер нормальной инструкции, массив интрукций, название переменной к которой относятся инструкции


def doing_inst(error_inst, list_inst, var):

    good_inst = None

    unknown.used_instr = error_inst
    unknown.var = var
    # определяет номер хорошей инструкции
    a = 0
    for a in range(len(list_inst)):
        if a in error_inst:
            a += 1
        else:
            good_inst = a
            break
    if good_inst == None:
        return unknown
    else:
        z = 0
        var = eval(list_inst[good_inst])
        return var

