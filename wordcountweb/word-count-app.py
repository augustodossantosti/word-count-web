""" Este modulo define a interface grafica da aplicacao."""

# -*- coding: utf-8 -*-

from tkinter import Tk, Button, Label, Entry, messagebox
from tkinter.constants import CENTER

from wordcountweb.PageChecker import PageChecker
from wordcountweb.WebPageInformation import WebPageInformation

# Window functions

page_checker = PageChecker()


def count():
    """ Inicia o processo de contagem de ocorrencia de palavras
     na pagina web especificada."""

    if are_fields_valid():
        web_page_information = WebPageInformation(txt_url, txt_proxy, txt_encode, txt_keyword)
        page_checker.set_web_page_information(web_page_information)
        try:
            result = page_checker.get_analysis_result()
            lb_result_value['text'] = result
        except Exception as error:
            messagebox.showerror('Error!', '%s' % error)


def are_fields_valid() -> bool:
    """ Verifica se os campos da janela foram preenchidos de
    forma correta."""

    return txt_url.get() != '' and txt_encode.get() != '' and txt_keyword.get() != ''


# Window properties

window = Tk()
window.geometry('800x600+250+30')
window.title('Word Count Web')

lb_url = Label(window, text="URL:")
lb_url.place(x=40, y=130)
txt_url = Entry(window, width=35)
txt_url.place(x=100, y=130)

lb_proxy = Label(window, text="Proxy:")
lb_proxy.place(x=405, y=130)
txt_proxy = Entry(window, show='*', width=35)
txt_proxy.place(x=465, y=130)

lb_encode = Label(window, text="Encode:")
lb_encode.place(x=40, y=190)
txt_encode = Entry(window, width=35)
txt_encode.place(x=100, y=190)

lb_keyword = Label(window, text="Keyword:")
lb_keyword.place(x=405, y=190)
txt_keyword = Entry(window, width=35)
txt_keyword.place(x=465, y=190)

lb_result = Label(window, text='Result:')
lb_result.place(relx=0.5, y=300, anchor=CENTER)
lb_result_value = Label(window, text='', font=('Arial', 50))
lb_result_value.place(relx=0.5, y=380, anchor=CENTER)

btn_verify = Button(window, width=20, text='Verify', command=count)
btn_verify.place(relx=0.5, y=500, anchor=CENTER)

window.mainloop()
