#!/usr/bin/env python3
"""
Deletion-resilient hypermedia pagination
"""

import csv
import math
from typing import List, Dict


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None
        self.__indexed_dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def indexed_dataset(self) -> Dict[int, List]:
        """Dataset indexed by sorting position, starting at 0
        """
        if self.__indexed_dataset is None:
            dataset = self.dataset()
            truncated_dataset = dataset[:1000]
            self.__indexed_dataset = {
                i: dataset[i] for i in range(len(dataset))
            }
        return self.__indexed_dataset

    def get_hyper_index(self, index: int = None, page_size: int = 10) -> Dict:
        """
        Get paginated data with hypermedia information, resilient to deletions.

        Args:
            index (int): The current start index of the return page.
            page_size (int): The number of elements to retrieve per page.

        Returns:
            Dict[str, Any]: A dictionary containing hypermedia information.
        """
        dataset = self.indexed_dataset()
        assert 0 <= index < len(dataset)

        response = {}
        data = []
        response['index'] = index

        for i in range(page_size):
            while True:
                current_index = dataset.get(index)
                index += 1
                if current_index is not None:
                    break
            data.append(current_index)

        response['data'] = data
        response['page_size'] = len(data)
        if dataset.get(index):
            response['next_index'] = index
        else:
            response['next_index'] = None

        return response
