# _*_ coding:utf-8 _*_
import  requests

def use_request():
    response=requests.get("http://www.httpbin.org")
    print(response.status_code)
    print(response.reason)
    print(response.headers)
    print(response.url)

if __name__ == '__main__':
    use_request()