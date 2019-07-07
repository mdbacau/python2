d = {'k1': [{'nest_key': ['this is deep', 'hello']}]}
print(
    str(
        d['k1'][0]['nest_key'][1]
    )
)

d = {'k1':[1,2,{'k2':['this is tricky',{'tough':[1,2,['hello']]}]}]}
print(
    str(
        d['k1'][2]['k2'][1]['tough'][2]
    )
)