# MYHTMLParser
from MyHTMLParser import MyHTMLParser
class MyHTMLParser(HTMLParser):
    def start_tag(self,tag,attrs):
        print ("encountered a start tag: ",tag)
    def end_tag(self,tag):
        print("encountered an end tag : ",tag)
    def handel_data(self,data):
        print("encountered some data is : ",data)
parser=MyHTMLParser()

parser.feed=('<html><head><title>test</title></head>'
             "<body><h1>parse me!</h1></body></html>")
