# AirBnB clone
### Models/Classes
- BaseModel
- User
- State
- City
- Amenity
- Place
- Review
## The console
Cmd line interface to execute CRUD operations on the different models
can be launched from root directory like so:
```
AirBnB_clone$ ./console
```
### Create
- usage: Create <model>
```
(hbnb) create User
```
### Read (single instance)
- usage 1: show \<model\> \<id\>
```
(hbnb) show City a1651f54-8acd-4716-a8d7-12ec797ec84d
```
- usage 2: \<model\>.show(\<id\>)
```
(hbnb) City.show("a1651f54-8acd-4716-a8d7-12ec797ec84d")
```
### Read (all)
show all instances of all models
- usage : all
```
(hbnb) all
```
show all instances og given model
- usage 1: all \<model\>
```
(hbnb) all Place
```
- usage 2: \<model\>.all()
```
(hbnb) Place.all()
```
### Update
- usage 1: update \<model\> \<id\> \<attribute name\> "\<attribute value\>"
```
(hbnb) update BaseModel 49faff9a-6318-451f-87b6-910505c55907 first_name "Betty"
```
- usage 2: \<module\>.update(\<id\>, \<attribute name\>, \<attribute value\>)
```
(hbnb) User.update("38f22813-2753-4d42-b37c-57a17f1e4f88", "first_name", "John")
```
- usage 3: \<model\>.update(\<id\>, \<dictionary representation\>)
```
(hbnb) User.update("38f22813-2753-4d42-b37c-57a17f1e4f88", {'first_name': "John", "age": 89})
```
### Destroy
- usage 1: destroy \<model\> \<id\>
```
(hbnb) destroy Aminity 356c227a-d5c1-403d-9bc7-6a34bb9f0f6c
```
- usage 2: \<model\>.destroy(\<id\>) 
```
(hbnb) User.destroy("246c227a-d5c1-403d-9bc7-6a47bb9f0f68")
```
### Other commands
#### count
count all instances of given class
- usage: \<model\>.count()
```
(hbnb) City.count()
```
#### quit
exit the console
- usage 1: quit
```
(hbnb) quit
```
- usage 2: Ctrl-D
