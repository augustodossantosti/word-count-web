""" Este modulo contem a definicao da classe que encapsula informacoes de uma pagina web."""

# -*- coding: utf-8 -*-


class WebPageInformation:
    """ Contem as informacoes sobre a pagina a ser analisada pela aplicacao."""

    def __init__(self, url: str, data: object, encode: str, key_word: str):
        self.url = url
        self.data = data
        self.encode = encode
        self.key_word = key_word
