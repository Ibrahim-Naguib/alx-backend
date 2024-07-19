#!/usr/bin/env python3
"""Hypermedia pagination"""
import csv
import math
from typing import List, Tuple, Dict


def index_range(page: int, page_size: int) -> Tuple:
    """
    Calculates the start and end indices for a given page and page size.

    Args:
        page (int): The current page number.
        page_size (int): The number of elements to retrieve per page.

    Returns:
        Tuple[int, int]: A tuple containing the start index and the end index
    """
    start_index = (page - 1) * page_size
    end_index = start_index + page_size

    return (start_index, end_index)


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """
        Get a page from the dataset.

        Args:
            page (int): The current page number.
            page_size (int): The number of elements to retrieve per page.

        Returns:
            List[List]: A list of rows for the specified page.
        """
        assert(type(page) == int and page > 0)
        assert(type(page_size) == int and page_size > 0)

        start_index, end_index = index_range(page, page_size)
        dataset = self.dataset()
        if start_index >= len(dataset):
            return []
        return dataset[start_index:end_index]

    def get_hyper(self, page: int = 1, page_size: int = 10) -> Dict:
        """
        Get paginated data with hypermedia information.

        Args:
            page (int): The current page number.
            page_size (int): The number of elements to retrieve per page.

        Returns:
            Dict: A dictionary containing hypermedia information.
        """
        data = self.get_page(page, page_size)
        total_items = len(self.dataset())
        total_pages = (total_items + page_size - 1) // page_size
        next_page = page + 1 if (page * page_size) < total_items else None
        prev_page = page - 1 if page > 1 else None
        return {
            "page_size": len(data),
            "page": page,
            "data": data,
            "next_page": next_page,
            "prev_page": prev_page,
            "total_pages": total_pages
        }
