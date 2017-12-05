import  csv

#This class is designed to help prepare the data from CSV format into python Dictionaries.
#The Function data_fill() returns 5 dict from our 5 CSV files.


def data_fill():

    #create dict to hold courses, topics, prof,course_match, prof_exp.
    courses = {}
    topics = {}
    prof = {}
    course_topic_match = {}
    prof_exp = {}

    #Create a variables to hold the CSV file location for each CSV file.
    courses_file = 'data/courses.csv'
    topics_file = 'data/topics.csv'
    prof_file = 'data/prof.csv'
    course_topic_match_file = 'data/course_topic_match.csv'
    prof_level_exp_file = 'data/prof_level_exp.csv'


    #fill_data_1 is as array that holds courses, topics and prof dict to make it easier to loop and fill them with data
    #we put those 3 together because they are identical to each other in term of CSV file structure.
    fill_data_1 = [courses, topics, prof]
    #Here same thing but with CSV file location for each to make it easier to loop and read data from those files.
    files_1 = [courses_file, topics_file, prof_file]

    #Similar to previous idea here we are holding date for course_topic_match and for prof_exp.
    fill_data_2 = [course_topic_match, prof_exp]
    #Same thing again but for CSV file locations for course_topic_match and for prof_exp
    files_2 = [course_topic_match_file, prof_level_exp_file]


    # We are using two for loops "Nested loops" to fill data into dictionaries, first loop deal with dict from fill_date_1 each time x will be an object from them.
    # Nested loop here takes care of the file location for each dict from fill_data_1.

    # i here works as a counter to help with nested loop for files so each time we take +1 to i we move to next file from files_1
    i = 0

    # loop based on len(fill_data_1).
    for x in range(0, len(fill_data_1)):
        with open(files_1[i], 'r') as f:
            reader = csv.reader(f)
            # read file row by row
            rowNr = 0
            for row in reader:
                # Skip the header row.
                if rowNr >= 1:
                    if row[0] in fill_data_1[x]:
                        print("Already here")
                    else:
                        fill_data_1[x][row[0]] = row[1]
                # Increase the row number
                rowNr = rowNr + 1
        i = i + 1

                ############################

    #Due to CSV files different structure we need two different loops.

    #We are using two for loops "Nested loops" to fill data into dictionaries, first loop deal with dict from fill_date_2 each time z will be an object from them.
    #Nested loop here takes care of the file location for each dict from fill_data_1.

    j = 0

    for z in range(0, len(fill_data_2)):
        with open(files_2[j], 'r') as f:
            reader = csv.reader(f)
            # read file row by row
            rowNr = 0
            for row in reader:
                # Skip the header row.
                if rowNr >= 1:
                    if row[0] not in fill_data_2[z]:
                        fill_data_2[z][row[0]] = {}
                        fill_data_2[z][row[0]][row[1]] = (row[2])
                    else:
                        fill_data_2[z][row[0]][row[1]] = (row[2])
                #Increase the row number
                rowNr = rowNr + 1
        j = j + 1

    #Here we return dictionary type data in a list.
    return [courses,topics,prof,course_topic_match,prof_exp]
