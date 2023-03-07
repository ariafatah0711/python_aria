print("hello dari __init__")

from . import matematika
'''from . import matematika # dari init kembali ke sains lalu import matematika '''
from . import fisika

# # bisa jugaa seperti 
# from .say_hi import say # artinya dari .(kembali 1) say_hi(ke file say_hi) lalu import def say
# ''' from .matematika import kali '''

# hanya untuk yang import sains *
# namun tidak disarankan
'''
__all__ = [
    "matematika",
    "fisika"
]
'''