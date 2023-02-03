import json
import random
import uuid
import base64
from datetime import date

date = str(date.today())
id_tag = "some_id"

def prepare_json(name):
    with open(name) as cheque:
        cheque = cheque.read()
        # Encoding the string into bytes
        cheque_bytes = cheque.encode('utf-8')
        # Base64 Encode the bytes
        cheque_b64_bytes = base64.b64encode(cheque_bytes)
        # Decoding the Base64 bytes to string
        cheque_b64_string = cheque_b64_bytes.decode("utf-8")
    data = cheque_b64_string
    uri = fsrarid + '-' + str(uuid.uuid1())
    mess = {"foo":"", "baar":"", "type":"ChequeV3", "foo_1":data, "date":date, "bar_2":"bar_2", "some_id":id_tag, "uri":uri}
    return mess

print(prepare_json('Cheque_v3.xml'))
