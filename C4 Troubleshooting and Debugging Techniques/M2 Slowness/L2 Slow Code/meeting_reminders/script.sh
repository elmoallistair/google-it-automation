time ./send_reminders.py "2020-01-13|Example|test1" # measure the script speed | one test user
time ./send_reminders.py "2020-01-13|Example|test1,test2,test3,test4,test5,test6,test7,test8,test9" # measure the script speed | nine test user
pprofile3 -f callgrind -o profile.out time ./send_reminders.py "2020-01-13|Example|test1,test2,test3,test4,test5,test6,test7,test8,test9" # get some data about what's going on
kcachefrind profile.out # gui for looking into profile.out file