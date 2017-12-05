from prepare_data import data_fill
import operator

data = data_fill()

courses = data[0]
topics = data[1]
prof = data[2]
course_match = data[3]
prof_exp = data[4]


total_wieght = 0.0


for course in courses:
    c_id_topics_ids = course_match[course]
    length_topics = len(c_id_topics_ids)

    for x in c_id_topics_ids:
        c_id_topics = topics[x]
        c_id_topics_perc = c_id_topics_ids[x]

    def lookup(dic, key, *keys):
        if keys:
            return lookup(dic.get(key, {}), *keys)
        return dic.get(key)


    i = 0
    best_prof = {}
    best_prof_index = {}
    index_m = 0
    for x in prof:
        index_m = 0
        for j in c_id_topics_ids:
            level_exp = int(lookup(prof_exp, x, j))
            t_percnt = int(c_id_topics_ids[j])
            index_m = index_m + (level_exp * t_percnt)


        best_prof_index[prof[x]] = (index_m / (length_topics * 100) * 100)

    best_prof_sorted = sorted(best_prof_index.items(), key=operator.itemgetter(1), reverse=True)

    total_wieght = total_wieght + best_prof_sorted[0][1]

    print("Ranks of Prof. in this course :",courses[course] )
    print(best_prof_sorted)

    print("Best Prof to teach" + courses[course] + " is:", best_prof_sorted[0], "%\n")

print('Total wieght =',total_wieght,' = ', (total_wieght/500)*100,'%')
