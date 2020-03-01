
my_big_list = []

for number in range(1, 1000):
    my_big_list.append(number)

my_file = open("output.txt", "w")

my_file.write(str(my_big_list))

my_file.close()
