Python 3.10.2 (v3.10.2:a58ebcc701, Jan 13 2022, 14:50:16) [Clang 13.0.0 (clang-1300.0.29.30)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
from hashlib import blake2b
h = blake2b()
h.update(b'Jericho Missile')
h.hexdigest()
'688a3277c53fbd375f375083c35703b07b122693b04ced7842e8e308fde5b7696762a287abdd2a9e08c7f796b15b39e1935563e5372594d9cc13b84c027b3eb9'
