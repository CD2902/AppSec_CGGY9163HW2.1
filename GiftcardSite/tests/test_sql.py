

"""

POST /use.html HTTP/1.1

Host: 127.0.0.1:8000

Content-Length: 619

Cache-Control: max-age=0

Upgrade-Insecure-Requests: 1

Origin: http://127.0.0.1:8000

Content-Type: multipart/form-data; boundary=----WebKitFormBoundaryAWfUKowlSW6wEKrN

User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.121 Safari/537.36

Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9

Sec-Fetch-Site: same-origin

Sec-Fetch-Mode: navigate

Sec-Fetch-User: ?1

Sec-Fetch-Dest: document

Referer: http://127.0.0.1:8000/use.html

Accept-Encoding: gzip, deflate

Accept-Language: en-US,en;q=0.9

Cookie: sessionid=wr42s1trysw9g8vn2rht4clymg0cuaah

Connection: close



------WebKitFormBoundaryAWfUKowlSW6wEKrN

Content-Disposition: form-data; name="card_data"; filename="newcard (2).gftcrd"

Content-Type: application/octet-stream



{"merchant_id": "NYU Apparel Card", "customer_id": "chrisd", "total_value": "2000", "records": [{"record_type": "amount_change", "amount_added": 2000, "signature": "[ insert crypto signature here ]"}]}

------WebKitFormBoundaryAWfUKowlSW6wEKrN

Content-Disposition: form-data; name="card_supplied"



True

------WebKitFormBoundaryAWfUKowlSW6wEKrN

Content-Disposition: form-data; name="card_fname"



ChrisD

------WebKitFormBoundaryAWfUKowlSW6wEKrN--

"""
