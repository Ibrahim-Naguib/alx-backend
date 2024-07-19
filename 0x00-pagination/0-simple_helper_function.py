#!/usr/bin/env python3
"""Simple helper function"""
from typing import Tuple


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
