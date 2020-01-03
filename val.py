import json
import relation_extract

test_data=[]
f = json.load(open('../datasets/test_data_me.json'))
test_data.extend(f)

relation_extract.test(test_data)