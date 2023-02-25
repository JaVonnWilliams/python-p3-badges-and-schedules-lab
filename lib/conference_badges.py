def badge_maker(name):
    return f'Hello, my name is {name}.'

def batch_badge_creator(names):
   badges = []
   for name in names:
        badge_message = f"Hello, my name is {name}."
        badges.append(badge_message)
   return badges

def assign_rooms(names):
    rooms = range(1, 9)

    assignments = []
    for room in rooms:
        assignments.append(f'Hello, {names[room -1]}! You\'ll be assigned to room {room}!')
    
    return assignments

def printer(names):
    for badge in batch_badge_creator(names):
        print(badge)

    for assignment in assign_rooms(names):
            print(assignment)
