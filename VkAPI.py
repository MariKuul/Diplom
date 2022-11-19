from urllib.parse import urljoin

import requests

from Photo import Photo


class VkAPI:
    BASE_URL = "https://api.vk.com/method/"

    @staticmethod
    def find_largest(sizes):
        sizes_chart = ['x', 'z', 'y', 'r', 'q', 'p', 'o', 'x', 'm', 's']
        for chart in sizes_chart:
            for size in sizes:
                if size['type'] == chart:
                    return size

    def __init__(self):
        self.token = 'vk1.a.MTfffb4LdjXnGdvjIEyRvNJFIM2Vhqe0Ic\
            P0SE0ABRg3EJJfprUsg_-VsxqBCk0mwZtL2U1PXNobUHikt17-G_be4JA90Xk2EZarEz_f93dKyKl1kgSetHjEHxp8\
        FCzokzZw2M5LilnxZuE2NHSWTS3Rs6A5MKS9HhQwh_\
        g6cP56Lsf1BSRWdP3iwBm7s63czlxIIuNqWJMBC0CwF74xpA'
        self.version = '5.131'

    def get_photos(self, uid, qty=5):
        get_url = urljoin(self.BASE_URL, 'photos.get')
        resp = requests.get(get_url, params={
            'access_token': self.token,
            'v': self.version,
            'owner_id': uid,
            'album_id': 'profile',
            'photo_sizes': 1,
            'extended': 1
        }).json().get('response').get('items')

        return sorted([Photo(photo.get('date'),
                             photo.get('likes')['count'],
                             self.find_largest(photo.get('sizes'))) for photo in resp],
                      key=lambda p: p.maxsize, reverse=True)[:qty]