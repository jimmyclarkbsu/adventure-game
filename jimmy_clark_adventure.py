"""Jimmy Clark
Adventure Game
An adventure game where you escape a monster.
"""
game = {

"start": ["Your car breaks down in the middle of the night. A monster approaches.", "Stay in the car and try to start it back up", "stay", "Get out of the car and run", "run"], 
 "stay": ["Your car doesn't start. The monster gets you.", "Start over", "start", "Quit", "quit"], 
 "run": ["You get out of the car and run. To the left is a wooded area. To the right is a small store.", "Go to the woods", "woods", "Go to the store", "store"], 
 "store": ["The store is closed. The monster catches you at the door.", "Start over", "start", "Quit", "quit"], 
 "woods": ["You run in the woods, but the monster saw you run into the woods. Do you keep running or hide?", "Keep running", "running", "Hide behind a tree", "tree"], 
 "tree": ["You hide behind a tree, but a twig snaps and the monster gets you.", "Start over", "start", "Quit", "quit"], 
 "running": ["You run into a fork in the road. You see an abandoned car or a small police station. Which option do you choose?", "Abandoned car", "car", "Police Station", "police"], 
 "car": ["You  run to the abandoned car, but it's locked. The monster gets you.", "Start over", "start", "Quit", "quit"], 
 "police": ["You run to the police station. But you need proof to show the police. Take a picture of the monster or lead it to the police station.", "Take a picture", "picture", "Lead it to station.", "station"], 
 "picture": ["You try to take a picture but your phone dies. The monster gets you.", "Start over", "start", "Quit", "quit"], 
 "station": ["You lead the monster to the station. An officer wants to fight back. Fight or hide.", "Fight", "fight", "Hide ", "hide"], 
 "hide": ["You hide from the monster. The monster overcomes the officer and gets you. You lose.", "Start over", "start", "Quit", "quit"], 
 "fight": ["You can trap the monster with a large net or you can use a taser.", "Use a taser", "taser", "Trap the monster", "trap"], 
 "taser": ["You try to tase the monster but the volts don't harm him. The monster gets you.", "Start over", "start", "Quit", "quit"], 
 "trap": ["You trap the monster with a large net and the monster can't get out. You have defeated the monster.", "Start over", "start", "Quit", "quit"],
}

list1 = ["run", "woods", "running", "police", "station", "fight", "trap"]
list2 = ["stay", "store", "tree", "car", "picture", "hide", "taser"]
choice = ()
main()

choice = input("Your car breaks down in the middle of the night. A monster approaches. Do you stay in the car and try to start it up or run? (Type stay or run.)")

if choice == "stay":
    print("Your car doesn't start. The monster gets you. You lose.")
    break
    return

elif choice == "run":
    print("You get out of the car and run.")
    
choice = input("To the left is a wooded area. To the right is a small store. (woods or store)")
if choice == "woods":
    print("You run in the woods, but the monster saw you run into the woods.")
elif choice == "store":
    print("The store is closed. The monster catches you at the door.")
    break
    
choice = input("Do you keep running or hide? (running or tree)")
if choice == "tree":
    print("You hide behind a tree, but a twig snaps and the monster gets you.")
    break
    
elif choice == "running":
    print("You run into a fork in the road. You see an abandoned car or a small police station.")
    
choice = input("Which option do you choose? (car or police)")
if choice == "car":
    print("You  run to the abandoned car, but it's locked. The monster gets you.")
    break

elif choice == "police":
    print("You run to the police station. But you need proof to show the police.")

choice = input("Take a picture of the monster or lead it to the police station. (picture or station)")
if choice == "picture":
    print("You try to take a picture but your phone dies. The monster gets you.")
    break

elif choice == "station":
    print("You lead the monster to the station.")

choice = input("An officer wants to fight back. (fight or hide)")
if choice == "hide":
    print("You hide from the monster. The monster overcomes the officer and gets you. You lose.")
    break

elif choice == "fight":
    print("You can trap the monster with a large net or you can use a taser.")
    
choice = input("Use the net or tase the monster: (taser or trap)")
if choice == "taser":
    print("You try to tase the monster but the volts don't harm him. The monster gets you.")
    break
elif choice =="trap":
    print("You trap the monster with a large net and the monster can't get out. You have defeated the monster.")
    

