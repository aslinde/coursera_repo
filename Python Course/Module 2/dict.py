sample_dict = {'school':'SSE','future':'entrepreneur'}
print(sample_dict.keys())
print(sample_dict.get('school'))
print(sample_dict['future'])

d ={}
d[1]='one'
d[2]='two'
d[3]=5
print(d.items())
print(d.values())


## This will print out key-value pairs because the items method returns each key-value pair as a tuple which can then be indexed by the way we've defined the loop
for key, values in d.items():
    print(key, values)
#### Shows how the tuples work here
tuple_experiment = (1,2,3,4)
print(tuple_experiment[0],tuple_experiment[1])

### Prints out Keys
for i in d:
    print(f'different {i}')

### So then the values method should print out values
for i in d.values():
    print(f'different {i}')
    ## :> and it does
