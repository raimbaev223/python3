text = input('')
def normal_text(text):
    text = ''.join([i for i in text if i not in ('!',',','?','.')])
    return text
print(normal_text(text))