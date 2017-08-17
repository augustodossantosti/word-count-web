""" Este modulo contem a definicao da classe que encapsula informacoes de uma pagina web."""

# -*- coding: utf-8 -*-


class WebPageInformation:
    """ Contem as informacoes sobre a pagina a ser analisada pela aplicacao."""

    def __init__(self, url_component: object, proxy_component: object,
                 encode_component: object, key_word_component: object):
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
