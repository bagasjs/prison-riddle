import random

def simulate_riddle(number_of_prisoners, with_log = False):
    chance_per_prisoner = int(number_of_prisoners / 2)

    box = [i for i in range(number_of_prisoners)]
    random.shuffle(box)
    if with_log:
        for i in range(len(box)):
            print(f"{i}={box[i]}", end=",")
        print(end="\n")
    
    for i in range(number_of_prisoners):
        last_number = i
        number_found = False
        for _ in range(chance_per_prisoner):
            current_number = box[last_number]
            if with_log:
                print(f"Prisoner {i} open box #{last_number} and found the number {current_number}")
            if current_number == i:
                number_found = True
                break
            else:
                last_number = current_number
        if not number_found:
            return False
    
    return True

if __name__ == "__main__":
    nsimulation = 100
    nprisoners = 100
    simulation_success_count = 0

    for i in range(nsimulation):
        if simulate_riddle(nprisoners):
            simulation_success_count += 1
    
    print(f"The chance of {nprisoners} prisoners success escape the prison is {simulation_success_count/nsimulation}")