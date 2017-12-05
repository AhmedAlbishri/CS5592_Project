from prepare_data import data_fill
import operator

# Call our data_fill() function from prepare_data class to gat data.
data = data_fill()

courses = data[0]
topics = data[1]
prof = data[2]
course_match = data[3]
prof_exp = data[4]


# function to help in getting values from dictionaries;
# we pass dictionary, key and another key to get value, here we use it with prof_exp we pass it as dict and prof_id and topic_id to get prof_exp.
def lookup(dic, key, *keys):
    if keys:
        return lookup(dic.get(key, {}), *keys)
    return dic.get(key)

# To check if prof ateaching more than a subject, 
prof_flag = {}

#Initialize all as not teaching
for p in prof:
    prof_flag[prof[p]] = 0

#Comulitave running weight
total_wieght = 0.0

#Main Greedy Algo will loop by size of courses
for course in courses:

    #to take the topic IDs in this topic
    c_id_topics_ids = course_match[course]

    #To take the length of tiopics in this course
    length_topics= len(c_id_topics_ids)

    i = 0
    best_prof_index = {}
    index_m = 0

    for x in prof:
        index_m = 0
        for j in c_id_topics_ids:

            level_exp = int(lookup(prof_exp, str(x), j))
            t_percnt = int(c_id_topics_ids[j])
            index_m = index_m + (level_exp * t_percnt)

            best_prof_index[prof[x]] = (index_m / (length_topics * 100) * 100)

    best_prof_sorted = sorted(best_prof_index.items(), key=operator.itemgetter(1), reverse=True)

    print("Ranks of Prof. in this course :",courses[course] )
    print(best_prof_sorted)

    res_list = [x[0] for x in best_prof_sorted]
    p = 0
    for best_prof in prof_flag:

        if prof_flag[res_list[p]] == 2:
            p = p + 1
            continue
        else:
            print("Best Prof to teach " + courses[course] + " is:", best_prof_sorted[p], "%\n")
            total_wieght = total_wieght + best_prof_sorted[p][1]
            prof_flag[res_list[p]] = prof_flag[res_list[p]] + 1
            p = p + 1
            break

print('Total wieght =',total_wieght,' = ', (total_wieght/500)*100,'%')
