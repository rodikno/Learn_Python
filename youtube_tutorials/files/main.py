file = open('sample.txt', 'w')

file.write('Lorem ipsum blah blah\n')
file.write('I like bacon\n')
file.close()

read_file = open('sample.txt', 'r')
text = read_file.read()
print(text)
read_file.close()
