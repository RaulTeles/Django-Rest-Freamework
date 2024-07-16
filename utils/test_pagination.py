from unittest import TestCase
from utils.pagination import make_pagination_range


class PaginationTeste(TestCase):
    def test_make_pagination_range_returns_a_pagination_range(self):
        pagination = make_pagination_range(
            page_range=list(range(1,21)),
            qtd_pages=4,
            current_page=1,
        )['pagination']
        self.assertEqual([1,2,3,4], pagination)

        pagination = make_pagination_range(
            page_range=list(range(1,21)),
            qtd_pages=4,
            current_page=2,
        )['pagination']
        self.assertEqual([1,2,3,4], pagination)
        
        pagination = make_pagination_range(
            page_range=list(range(1,21)),
            qtd_pages=4,
            current_page=3,
        )['pagination']
        self.assertEqual([2,3,4,5], pagination)
        
        pagination = make_pagination_range(
            page_range=list(range(1,21)),
            qtd_pages=4,
            current_page=4,
        )['pagination']
        self.assertEqual([3,4,5,6], pagination)

    def test_make_pagination_range_is_static_when_last_page_is_next(self):
        pagination = make_pagination_range(
            page_range=list(range(1,21)),
            qtd_pages=4,
            current_page=18,
        )['pagination']
        self.assertEqual([17,18,19,20], pagination)