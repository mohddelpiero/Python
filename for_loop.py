subjects = ['Arabic', 'English' , 'Math' , 'Science']
print(subjects) # print all subjects
print(subjects[1]) # print subject 1 = English
print(subjects[3]) # print subjeet 3 = Science
subjects.append('History') # add new subject at end
print(subjects)
print(subjects[1:4]) # print subjects from 1 to 4 only
print(subjects[0:3]) # print subjects from 0 to 3 only
print(subjects[-1]) # print last subject only
subjects.pop() # remove last added subject
print(subjects)

for m in subjects: # for help in case to read file or folder contents
   print(m)