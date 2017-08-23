"""
Este modulo contem a definicao da classe que encapsula informacoes de uma pagina web.

author:     Augusto Santos
version:    1.0

"""

# -*- coding: utf-8 -*-

from tkinter import Entry


class WebPageInformation:
    """ Contem as informacoes sobre a pagina a ser analisada pela aplicacao."""

    def __init__(self, url_component: Entry, proxy_component: Entry,
                 encode_component: Entry, key_word_component: Entry):
        self.url_component = url_component
        self.proxy_component = proxy_component
        self.encode_component = encode_component
        self.key_word_component = key_word_component

    def get_url_value(self) -> str:
        return self.url_component.get()

    def get_proxy_value(self) -> str:
        return self.proxy_component.get()

    def get_encode_value(self) -> str:
        return self.encode_component.get()

    def get_keyword_value(self) -> str:
        return self.key_word_component.get()
