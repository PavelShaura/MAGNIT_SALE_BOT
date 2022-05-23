url = 'https://magnit.ru/upload/iblock/caa/caa34565215c9211e877eadc4fa1b601.jpg'

article_id = url.split('/')[-1]
article_id = article_id[:-6]

print(article_id)