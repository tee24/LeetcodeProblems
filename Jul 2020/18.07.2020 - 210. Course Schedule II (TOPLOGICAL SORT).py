from collections import defaultdict
def course_schedule(numCourses, prerequisites):
    num_prereq = defaultdict(int)
    prereq = defaultdict(list)
    
    for course, course_prereq in prerequisites:
        num_prereq[course]+=1
        prereq[course_prereq].append(course)

    stack = []
    order = []

    for i in range(numCourses):
        if i not in num_prereq:
            stack.append(i)

    while stack:
        node = stack.pop()
        order.append(node)
        for child in prereq[node]:
            num_prereq[child]-=1
            if num_prereq[child] == 0:
                stack.append(child)

    return order if len(order) == numCourses else None

