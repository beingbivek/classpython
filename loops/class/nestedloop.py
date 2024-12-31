floors = ['floor1','floor2','floor3']
rooms = [1,2,3]

#print all floors with room
# for floor in floors:
#     for room in rooms:
#         print(floor,room)

# print all rooms of floor 1, room 2 of floor 2 and room 3 of floor 3
for floor in floors:
    for room in rooms:
        if floor == 'floor2':
            if (room == 1 or room == 3):
                continue
        elif floor == 'floor3':
            if (room == 1 or room == 2):
                continue
        print(floor,room,sep="-Room")