from VkAPI import VkAPI
from YaAPI import YaAPI


def init():
    y_token = input('YandexDisk token:')
    uid = input('VK user id:')
    qty = input('Number of photos to upload: ')
    vk_api = VkAPI()
    ya_api: YaAPI = YaAPI(y_token)
    ya_api.upload(uid, vk_api.get_photos(uid, int(qty)))


if __name__ == '__main__':
    init()
