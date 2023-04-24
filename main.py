from tkinter import *
from sympy import *

root = Tk()
root.geometry('650x700')
root.resizable(width=True, height=True)

t_title = Label(text='Введите \nзначение времени:')
row_t_value = IntVar()
t_entry = Entry(textvariable=row_t_value)

m_title = Label(text='Введите \nзначение массы:')
row_m_value = IntVar()
m_entry = Entry(textvariable=row_m_value)

R2_title = Label(text='Значение R2:\n60мм')
row_R2_value = IntVar()
R2_entry = Entry(textvariable=row_R2_value)

r2_title = Label(text='Значение r2:\n82мм')
row_r2_value = IntVar()
r2_entry = Entry(textvariable=row_r2_value)

R3_title = Label(text='Значение R3:\n170мм')
row_R3_value = IntVar()
R3_entry = Entry(textvariable=row_R3_value)

r3_title = Label(text='Значение r3:\n100мм')
row_r3_value = IntVar()
r3_entry = Entry(textvariable=row_r3_value)

Name_res_label = Label(text='Вычисление:')

result = Label(text='', font=('Arial', 14))
result_ = Label(text='', font=('Arial', 12))


def calculate(event):
    try:

        eq_value = '21 + 120 * t**2'
        m = row_m_value.get()
        t_value = row_t_value.get()
        t = t_value
        R2_value = 60 / 1000
        r2_value = 82 / 1000
        R3_value = 170 / 1000
        r3_value = 100 / 1000
        S1 = eval(eq_value)  # MM
        V1_diff = diff(eq_value)  # MM/c
        a1 = float(diff(V1_diff) / 1000)  # M/с^2
        V1 = eval(str(V1_diff / 1000))  # M/c
        omega2 = round(V1 / R2_value, 3)  # c^-1
        Vb = round(omega2 * r2_value, 3)  # M/c
        omega3 = round(Vb / R3_value, 3)  # c^-1

        G1 = m * 9.81
        F_in_1 = m * a1

        R1 = G1 - F_in_1

        M2 = G1 * r2_value

        M3 = (M2 * omega2) / omega3

        Fm = M3 / r3_value
        print(M3)





        result["text"] = f'Ответ:'
        result_["text"] = f'для прекращения движения груза 1 в момент времени {t}с \nк нему необходимо приложить ' \
                          f'силу равную {R1}Н,\n при этом в момент времени {t}с в точке М малого цилиндра блока 3\n' \
                          f' механизма сформируется сила равная {Fm}Н.'



    except Exception as e:
        result["foreground"] = 'red'
        result["font"] = '20'
        result["text"] = f'Проверьте введенные данные.'
        print(e)
        pass


button = Button(text='Рассчитать')

t_title.grid(column=2, row=1)
t_entry.grid(column=2, row=2)
m_title.grid(column=1, row=1)
m_entry.grid(column=1, row=2)
R2_title.grid(column=3, row=1)
r2_title.grid(column=1, row=3)
R3_title.grid(column=2, row=3)
r3_title.grid(column=3, row=3)
button.grid(column=2, row=5)
Name_res_label.grid(column=2, row=10)
result.grid(column=2, row=27)
result_.grid(column=2, row=28)
button.bind('<Button-1>', calculate)

if __name__ == '__main__':
    root.mainloop()
    init_printing(use_unicode=False, wrap_line=False, no_global=True)
