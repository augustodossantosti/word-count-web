""" Este modulo contem a definicao das classes responsaveis pela analise da pagina web."""

# -*- coding: utf-8 -*-

import string
import re

from urllib import request
from wordcountweb.WebPageInformation import WebPageInformation


class PageChecker:
    """ Esta classe e responsavel pela analise da pagina web
    e prove os metodos necessarios para busca e contagem de
    palavras chaves."""

    def __init__(self, web_page_information=None):
        self.web_page_information = web_page_information

    def set_web_page_information(self, web_page_information):
        self.web_page_information = web_page_information

    def get_analysis_result(self) -> int:
        """ Retorna o resultado da analise de uma pagina web"""

        page = self.open_url(self.web_page_information.get_url_value(), self.web_page_information.get_proxy_value())
        page_content = self.read_page(page, self.web_page_information.get_encode_value())
        raw_text = self.remove_html_tags(page_content)
        return self.count_words(self.web_page_information.get_keyword_value(), raw_text)

    def open_url(self, url: str, proxy_settings: str):
        """ Realiza uma requisicao para a pagina especificada
        :param url: A url a ser aberta
        :param proxy_settings: Configurações de proxy a serrem enviados ao server
        :return: A pagina obtida atraves da requisicao"""

        if proxy_settings != '':
            proxy = {'https': proxy_settings, 'http': proxy_settings}
            proxy_support = request.ProxyHandler(proxies=proxy)
            opener = request.build_opener(proxy_support)
            request.install_opener(opener)

        web_page = request.urlopen(url)
        return web_page

    def read_page(self, web_page, encode: str) -> str:
        """ Realiza o processo de decode e leitura de uma pagina web
        retornando seu conteudo.
        :param web_page: A pagina a ser lida
        :param encode: O formato de codificacao da pagina
        :return: O conteudo do corpo da pagina"""

        content = web_page.read().decode(encode)
        return content

    def remove_html_tags(self, raw_html: str) -> str:
        """ Remove todas as tags de um texto html puro. """

        clean_re = re.compile(r'<[^>]+>')
        clean_text = re.sub(clean_re, '', raw_html)
        return clean_text

    def count_words(self, key_word: str, raw_text: str) -> int:
        """ Realiza a contagem de ocorrencias de uma palavra em
        um determinado texto."""

        for character in string.punctuation:
            text = raw_text.replace(character, ' ')

        text = text.lower()
        key_word = key_word.lower()
        text = text.split()

        words = {}
        for character in text:
            if character not in words:
                words[character] = 1
            else:
                words[character] += 1

        return 0 if key_word not in words else words[key_word]
