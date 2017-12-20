import sys

try:
    with open('number') as orig_file:
        # the file from the generated personalized exercise instance
        start = int(orig_file.read().strip())
    with open('solution') as submitted_file:
        # student's submission
        solution = int(submitted_file.read().strip())
    
    orignumber = None
    try:
        # if the personal directory is used (testing store_user_files action)
        with open('orignumber') as f:
            orignumber = int(f.read().strip())
    except IOError:
        pass

    max_points = 10
    points = 0
    if solution == (start + 1):
        # correct solution
        points = max_points

    print("TotalPoints: {}".format(points))
    print("MaxPoints: {}".format(max_points))
    
    print("Original number was: {}".format(start))
    print("Your solution was: {}".format(solution))
    
    print("Previous number was: {}".format(orignumber)) # just to test store_user_files action

except Exception as e:
    print("ERROR")
    print(e)
    sys.exit(1)
