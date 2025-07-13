task = input("Enter your task: ")
priority = input("Priority (high/medium/low): ")
time_bound = input("Is it time-bound? (yes/no): ")
if time_bound == "yes":
        print(f"Reminder: '{task}' is a {priority} priority task that requires immediate attention today!")
else:
    match priority:
        case "high":
           print(f"Note: '{task}' is a high priority task. Make sure to complete it as soon as possible to avoid any negative consequences.")
        case "medium":
            print(f"Note: '{task}' is a medium priority task. Try to schedule some time for it soon, but it's not immediately urgent.")
        case "low":
            print(f"Note: '{task}' is a low priority task. Consider completing it when you have free time.")