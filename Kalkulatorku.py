from tkinter import *

#fungsi agar tombol angka dan yang lain dapat berfungsi [number=parameter]
def buttonClick(number):
    global operator
    operator = operator + str(number)
    input_value.set(operator)

#fungsi agar tombol clear dapat berfungsi
def buttonClear():
    global operator
    operator = ""
    input_value.set("")
    
#nilai/hasil dari operator yang telah dihitung dan menampilkannya di layar kalkulator || eval() digunakan untuk mengevaluasi biangan yang dimasukkan ke dalam operator.
def buttonEqual():
    global operator
    result = str(eval(operator)) #baris yang mengevaluasi sebuah string yang berisi operasi matematika dan mengembalikan hasil operasinya dalam bentuk string
    input_value.set(result)
    operator = ""

#fungsi tombol delete = menghapus 1 nilai setelahnya
def buttonDelete():
    global operator
    operator = operator[:-1]
    input_value.set(operator)

#fungsi untuk tombol desimal
def buttonDecimal():
    global operator
    operator = operator + "."
    input_value.set(operator)
    
    
####################################################
main = Tk()
main.title("Kalkulator ")

#variabel operator diisi dngan string ksong, yg kmudian variabelnya dapat digunakan untuk melakukan operasi jumlah, kurang, kali, bagi, dll
operator = ""

#nilai input variabel ini digunakan untuk menyimpan nilai.
input_value = StringVar()
display_text = Entry(main, font=("arial", 30, "bold"), textvariable=input_value, bd=40, insertwidth=5,
                     bg="light blue", justify=RIGHT)
display_text.grid(columnspan=5)

#Codingan Baris ke 1 = 7,8,9,+
btn_7 = Button(main, padx=24, bd=16, fg="black", font=("arial", 30, "bold"), text="7", command=lambda: buttonClick(7))
btn_7.grid(row=1, column=0)

btn_8 = Button(main, padx=24, bd=16, fg="black", font=("arial", 30, "bold"), text="8", command=lambda: buttonClick(8))
btn_8.grid(row=1, column=1)

btn_9 = Button(main, padx=24, bd=16, fg="black", font=("arial", 30, "bold"), text="9", command=lambda: buttonClick(9))
btn_9.grid(row=1, column=2)

btn_add = Button(main, padx=20, bd=16, fg="black", font=("arial", 30, "bold"), text="+", command=lambda: buttonClick("+"))
btn_add.grid(row=1, column=3)

#Codingan Baris ke 2 = 4,5,6, -
btn_4 = Button(main, padx=24, bd=16, fg="black", font=("arial", 30, "bold"), text="4", command=lambda: buttonClick(4))
btn_4.grid(row=2, column=0)

btn_5 = Button(main, padx=24, bd=16, fg="black", font=("arial", 30, "bold"), text="5", command=lambda: buttonClick(5))
btn_5.grid(row=2, column=1)

btn_6 = Button(main, padx=24, bd=16, fg="black", font=("arial", 30, "bold"), text="6", command=lambda: buttonClick(6))
btn_6.grid(row=2, column=2)

btn_sub = Button(main, padx=24, bd=16, fg="black", font=("arial", 30, "bold"), text="-", command=lambda: buttonClick("-"))
btn_sub.grid(row=2, column=3)

#Codingan Baris ke 3 = 1,2,3, *
btn_1 = Button(main, padx=24, bd=16, fg="black", font=("arial", 30, "bold"), text="1", command=lambda: buttonClick(1))
btn_1.grid(row=3, column=0)

btn_2 = Button(main, padx=24, bd=16, fg="black", font=("arial", 30, "bold"), text="2", command=lambda: buttonClick(2))
btn_2.grid(row=3, column=1)

btn_3 = Button(main, padx=24, bd=16, fg="black", font=("arial", 30, "bold"), text="3", command=lambda: buttonClick(3))
btn_3.grid(row=3, column=2)

btn_nul = Button(main, padx=22, bd=16, fg="black", font=("arial", 30, "bold"), text="*", command=lambda: buttonClick("*"))
btn_nul.grid(row=3, column=3)

#Codingan Baris ke 4 = desimal,0,=, /
btn_decimal = Button(main, padx=27, bd=16, fg="black", font=("arial", 30, "bold"), text=".", command=buttonDecimal)
btn_decimal.grid(row=4, column=0)

btn_0 = Button(main, padx=23, bd=16, fg="black", font=("arial", 30, "bold"), text="0", command=lambda: buttonClick("0"))
btn_0.grid(row=4, column=1)

btn_equal = Button(main, padx=24, bd=16, fg="black", font=("arial", 30, "bold"), text="=", command=buttonEqual)
btn_equal.grid(row=4, column=2)

btn_div = Button(main, padx=24, bd=16, fg="black", font=("arial", 30, "bold"), text="/", command=lambda: buttonClick("/"))
btn_div.grid(row=4, column=3)

#codingan Unutk baris clear smua angka, dan delete salah 1 angka
btn_del = Button(main, padx=20, bd=15, fg="black", font=("arial", 30, "bold"), text="D", command=buttonDelete)
btn_del.grid(row=5, column=0)

btn_clear = Button(main, padx=20, bd=15, fg="black", font=("arial", 30, "bold"), text="C", command=buttonClear)
btn_clear.grid(row=5, column=1)

main.mainloop()