""" Este modulo contem a definicao das classes responsaveis pela analise da pagina web."""

# -*- coding: utf-8 -*-

from urllib import request
from wordcountweb.WebPageInformation import WebPageInformation


class PageChecker:
    """ Esta classe e responsavel pela analise da pagina web
    e prove os metodos necessarios para busca e contagem de
    palavras chaves."""

    def __init__(self, web_page_information: WebPageInformation):
        self.web_page_information = web_page_information

    def get_analysis_result(self) -> int:
        """ Retorna o resultado da analise de uma pagina web"""
        page = self.open_url(self.web_page_information.url, self.web_page_information.data)
        page_content = self.read_page(page, self.web_page_information.encode)
        return self.count_word(self.web_page_information.key_word, page_content)

    def open_url(self, url: str, data: object):
        """ Realiza uma requisicao para a pagina especificada
        :param data: Dados adicionais a serrem enviados ao server
        :return: A pagina obtida atraves da requisicao"""

        web_page = request.urlopen(url, data)
        return web_page

    def read_page(self, web_page, encode: str) -> str:
        """ Realiza o processo de decode e leitura de uma pagina web
        retornando seu conteudo.
        :param web_page: A pagina a ser lida
        :param encode: O formato de codificacao da pagina
        :return: O conteudo do corpo da pagina"""

        content = web_page.read().decode(encode)
        return content

    def count_word(self, key_word: str, text: str):
        """ Realiza a contagem de ocorrencias de uma palavra em
        um determinado texto."""

        return 0
