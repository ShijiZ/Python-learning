# Encoding=utf-8
import io

f = io.open('unicode.txt', 'wt', encoding='utf-8')
f.write(u'嘿嘿嘿')
f.close()

text = io.open('unicode.txt', encoding='utf-8').read()
print text
