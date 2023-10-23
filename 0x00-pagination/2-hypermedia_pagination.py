#!/usr/bin/env python3
""" Pagination """
import csv
import math
from typing import List, Tuple


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
        Return list of baby names
        or raise assertion error if input datatype is wrong
        """
        assert (isinstance(page, int) and isinstance(page_size, int))
        assert (page > 0 and page_size > 0)
        [start, end] = index_range(page, page_size)
        return self.dataset()[start: end]

    def get_hyper(self, page: int, page_size: int) -> dict:
        """
        method that takes the same arguments (and defaults) as
        get_page and returns a dictionary containing the
        following key-value pairs:
        """
        dataset_records = self.get_page(page, page_size)

        page_level = math.ceil(len(self.__dataset) / page_size)

        return {
            'page_size': len(dataset_records),
            'page': page,
            'data': dataset_records,
            'next_page': page + 1 if (page + 1) <= page_level else None,
            'prev_page': page - 1 if (page - 1) > 0 else None,
            'total_pages': page_level
        }


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """
    function named index_range that takes two integer arguments
    page and page_size. The function should return a tuple of
    size two containing a start index and an end index
    corresponding to the range of indexes to return in
    a list for those particular pagination parameters.
    """
    return (((page - 1) * page_size), (page * page_size))