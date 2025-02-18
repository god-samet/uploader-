from samet_core import database
from random import choice, randint

cache_ip_list = {}


def get_random_range_ip_from_database():
    return choice(database.get_cache_parameter('range_ips').split('\n'))


def get_random_ip_from_database():
    fragmented_random_ip = get_random_range_ip_from_database().split('.')

    def valid_octet(octet, allow_zero=False):
        return octet.isdigit() and (0 if allow_zero else 1) <= int(octet) < 255

    if all(valid_octet(fragmented_random_ip[i], allow_zero=(i >= 2)) for i in range(4)):
        return f"{fragmented_random_ip[0]}.{fragmented_random_ip[1]}." \
               f"{fragmented_random_ip[2] or randint(1, 255)}." \
               f"{fragmented_random_ip[3] or randint(1, 255)}"

    return get_random_ip_from_database()  # بازگشت مجدد در صورت نامعتبر بودن


def get_udp_port():
    return randint(1024, 65535)  # انتخاب تصادفی پورت از رنج UDP


def cache_ip_ports_from_database():
    global cache_ip_list
    cache_ip_list.update(database.get_ip_ports_from_database())  # به‌جای جایگزینی، آپدیت می‌کنه


def get_random_ip_port():
    if cache_ip_list:
        target_ip, target_port = cache_ip_list.popitem()
    else:
        target_ip = get_random_ip_from_database()
        target_port = get_udp_port()
        database.set_ip_port_to_database(target_ip, target_port)

    return target_ip, target_port
