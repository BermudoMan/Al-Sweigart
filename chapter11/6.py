import bs4

soup = bs4.BeautifulSoup(open('example.html'))
span_elem = soup.select('span')[0]
print(str(span_elem))
print(span_elem.get('id'))
print(span_elem.get('несуществующий_адрес') == None)
print(span_elem.attrs)
