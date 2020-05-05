import sys
from urllib.request import urlopen
from bs4 import BeautifulSoup

def cnn(url,keyword):
    page = urlopen(url)
    soup = BeautifulSoup(page,'html.parser')
    headline = soup.find('h1',{"class":"pg-headline"})
    content = soup.find('div',{"itemprop":"articleBody"}).section.div
    return keyword in str(content)

def fox(url,keyword):
    page = urlopen(url)
    soup = BeautifulSoup(page,'html.parser')
    headline = soup.find('h1',{'class':'headline'})
    content = soup.find('div',{'class':'article-body'})
    articlebody = ''
    for i in content.findAll('p'):
        articlebody += str(i)
    return keyword in articlebody

def nytimes(url,keyword):
    page = urlopen(url)
    soup = BeautifulSoup(page,'html.parser')
    content = soup.find('section',{'name':'articleBody'})
    return keyword in str(content)

def bbc(url,keyword):
    page = urlopen(url)
    soup = BeautifulSoup(page,'html.parser')
    content = soup.find('div',{'class':'story-body__inner'})
    return keyword in str(content)

def nypost(url,keyword):
    page = urlopen(url)
    soup = BeautifulSoup(page,'html.parser')
    content = soup.find('div',{'class':'entry-content'})
    return keyword in str(content)

def final(url,keyword):
    website = url.split('.com')[0]
    if 'cnn' in website:
        return cnn(url,keyword)
    if 'fox' in website:
        return fox(url,keyword)
    if 'nytimes' in website:
        return nytimes(url,keyword)
    if 'bbc' in website:
        return bbc(url,keyword)
    if 'nypost' in website:
        return nypost(url,keyword)

def main():
	for arg in sys.argv[1:]:
		print(arg)

if __name__ == '__main__':
	print(final(sys.argv[1],sys.argv[2]))
	#main()

#print(final(sys.argv[0],sys.argv[1]))