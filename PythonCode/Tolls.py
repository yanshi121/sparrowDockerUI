import hashlib
from UserConfig import USER_MAC, USER_NAME, USER_PASSWORD


def md5_encrypt(data):
    md5_1 = hashlib.md5(data.encode(encoding='UTF-8')).hexdigest()
    md5_2 = hashlib.md5(md5_1.encode(encoding='UTF-8')).hexdigest()
    md5_3 = hashlib.md5(md5_2.encode(encoding='UTF-8')).hexdigest()
    md5_4 = hashlib.md5(md5_3.encode(encoding='UTF-8')).hexdigest()
    md5_5 = hashlib.md5(md5_4.encode(encoding='UTF-8')).hexdigest()
    md5_6 = hashlib.md5(md5_5.encode(encoding='UTF-8')).hexdigest()
    return md5_6


def is_login(name, password, MAC):
    if USER_NAME == '':
        return '0'
    name_md5 = md5_encrypt(name)
    password_md5 = md5_encrypt(password)
    MAC_md5 = md5_encrypt(MAC)
    if name_md5 == USER_NAME and password_md5 == USER_PASSWORD:
        if MAC_md5 == USER_MAC:
            return '1'
        else:
            return '2'
    else:
        return '3'

print(is_login("39", "aDYLL121380O!", "020712"))
