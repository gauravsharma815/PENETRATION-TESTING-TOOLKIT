def print_results(results):
    for result in results:
        print(result)

def log_activity(activity):
    with open('activity.log', 'a') as log_file:
        log_file.write(activity + '\n')