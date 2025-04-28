# dict_variable= {key:value for (key,value) in dictionary.items()} -------------SYNTAX
#A common use for this is to build up an index to symbolic column names.

text = ['col-zero' , 'col-one' , 'col-two' , 'col-three']
lookup = { key : value for (value,key) in enumerate(text)}
print(lookup)