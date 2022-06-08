import urllib.request as req
url="https://www.ptt.cc/bbs/part-time/index.html"
request=req.Request(url, headers={
    "User-Agent":"Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.77 Mobile Safari/537.36",
    "Cookie":"mid=YLzCOQALAAED-KxtFvBh8LyJYBDW; ig_did=108370D1-014A-4E12-A83E-15DB1D00F74F; ig_nrcb=1; fbm_124024574287414=base_domain=.instagram.com; csrftoken=H6VoMWnxWXUpMM8Mh2PggsSsAtOSlGJX; ds_user_id=7407771650; sessionid=7407771650%3AHf01s8WtalN7na%3A23; shbid=8772; shbts=1622983231.3523788; rur=RVA; fbsr_124024574287414=tGi_rsKB4gH62-XcuYOHIeWW7bZ2Pc57QbEtmARRzCk.eyJ1c2VyX2lkIjoiMTAwMDA4NTgzMjI0MjQ2IiwiY29kZSI6IkFRQmNXdmVZSFQ1N2Q0SDRXMmE3NXVaZldDWWJEcUpaSHM2ejhWTUpxUlg4eHRJYXhiVmVyNzFHY1BZTzlDTjF5N0VZNllrSmtFQVpMZUFwRmNHcG1jN2x5bTRfUnFsVTJ5WldmWkVkMVNFTEVOM1RKMzBua0ZjZno0ZnNmUml2eWlvczdDUGUtZWJ2VkxtTjluWUM3T05JYm9YMmhGS3lVMDJJRWlpYXhSWkQwcjMyTHJ4MGVlTzJWcG1YYjA4c2pRWF90UTl3NlVVam04U09XbHN3VUNDXzI1Si05NkRXSEs3YmJzNk5sRW4tUGJ0dXhidFVIaVN5SkNEXzFqUVdncjE5bTJQbk5mcXM5a3ZZOXlhTUQ2bGFuNVh6V3FtbU53M0kyV0I5YmUwdk4zMFpaMU4yRldtbXFTZXhidGJTQVlISl9ab2t6UHFLYWYxblFRUjF5Y0sxVm0wQVEzTVRNRWlra29fbE56THpuUSIsIm9hdXRoX3Rva2VuIjoiRUFBQnd6TGl4bmpZQkFOWEJNRERaQzhHcVEwV3hPeUVwczRFOEpHRm93N1NPNnpaQXFYUGdyUVJLYjI2bmYyRWZwaEs1WkE1ZTJjWkNUZm91WkFPRGxFUjgwMmVxaGpXT2ZaQWtaQVQ3NzI4RWhQQnJndW5oRlpCTUdHZG91VGY2V045dmxoWkFPbFEwVGpWUGZySVY4SFl5eGhlcE81S1YyMmRLSE04bU9zWkJzaUhZT3JaQlhLQ1pCeDJjRDFpNUtJdVhFbWdaRCIsImFsZ29yaXRobSI6IkhNQUMtU0hBMjU2IiwiaXNzdWVkX2F0IjoxNjIzMjE2MTA2fQ",
})
with req.urlopen(request) as response:
    data=response.read().decode("utf-8")
import bs4
root=bs4.BeautifulSoup(data, "html.parser")
titles=root.find_all("div", class_="title")
for title in titles:
    if title.a != None:
        print(title.a.string)