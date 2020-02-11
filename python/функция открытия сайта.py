import urllib.request
wp=urllib.request.urlopen('vk.com')
pw=wp.read()
print (pw)

