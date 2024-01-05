import re
import os

la = """ala ana ama 
assssssssssa ada 
ela ema 
eba ena eva mama mama """

print(re.findall('e.a|a.a', la))  # toate aparitiile a orice caracter a si e orice caracter e

print(re.match("ma+", la))