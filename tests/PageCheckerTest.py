""" Este modulo contem os testes para os metodos de PageChecker.py """

from unittest import TestCase, main

from wordcountweb.PageChecker import PageChecker


class PageCheckerTest(TestCase):

    @classmethod
    def setUpClass(cls):
        cls.page_checker = PageChecker()

    def test_remove_html_tags(self):
        raw_html = '<!DOCTYPE html><html><body:><h1>python is so cool</h1></body></html>'
        raw_text = self.page_checker.remove_html_tags(raw_html)
        self.assertTrue('<' not in raw_text and '>' not in raw_text, 'Erro ao remover as tags html.')

    def test_count_words(self):
        text = 'Python is so cool. Python is the best programming language!'
        total_occurrences = self.page_checker.count_words('python', text)
        self.assertEqual(2, total_occurrences, 'Erro ao encontrar a palavra chave.')

if __name__ == '__main__':
    main()
