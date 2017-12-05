import sys, operator
from builtins import print
from test_prepare_data import data_fill


data = data_fill()

courses = data[0]
topics = data[1]
prof = data[2]
course_match = data[3]
prof_exp = data[4]

prof_ids = [1,2,3,4,5]
size = len(prof_ids)

total_wieght = 0.0

prof_courses = {}
prof_sorted = {}


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

    for x in prof_ids:
        index_m = 0

        for j in c_id_topics_ids:
            level_exp = int(lookup(prof_exp, x, j))
            t_percnt = int(c_id_topics_ids[j])
            index_m = index_m + (level_exp * t_percnt)

            best_prof_index[prof[x]] = (index_m / (length_topics * 100) * 100)

        if x not in prof_courses:
            prof_courses[x] = {}
            prof_courses[x][course] = int(best_prof_index[prof[x]])
        else:
            prof_courses[x][course] = int(best_prof_index[prof[x]])

for x in prof_courses:
    if x not in prof_sorted:
        prof_sorted[x] = {}
        prof_sorted[x] = sorted(prof_courses[x].items(), key=operator.itemgetter(1), reverse=True)
    else:
        prof_sorted[x] = sorted(prof_courses[x].items(), key=operator.itemgetter(1), reverse=True)

print(prof_sorted)

#Matrix Ai has dimension p[i-1] x p[i] for i = 1..n
def MatrixChainOrder(p, n):
    # For simplicity of the program, one extra row and one
    # extra column are allocated in m[][].  0th row and 0th
    # column of m[][] are not used
    m = [[0 for x in range(n+1)] for x in range(n+1)]

    # m[i,j] = Minimum number of scalar multiplications needed
    # to compute the matrix A[i]A[i+1]...A[j] = A[i..j] where
    # dimension of A[i] is p[i-1] x p[i]

    # cost is zero when multiplying one matrix.
    for i in range(1, n):
        m[i][i] = 0

    for L in range(1, n):
        for i in range(1, n-L+1):
            j = i + L
            m[i][j] = 0
            for k in range(i, j):
                z = max(prof_sorted[i][0][1] ,prof_sorted[j][0][1])

                q = m[i][k] + m[k+1][j-1] + z

                #print(m[i][k] ," ", m[k + 1][j]," i= ",i," j= ",j ,prof_sorted[i][0][1]," ",prof_sorted[j][0][1] ," q=",q)

                if q > m[i][j]:
                    m[i][j] = q

    print(m)
    return m[1][n]


res = MatrixChainOrder(prof_ids, size)

total_wieght = total_wieght + res

print('Total wieght =',total_wieght,' = ', (total_wieght/500)*100,'%')
