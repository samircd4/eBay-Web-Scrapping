name = 'Name:SamirDasEmail:sam@gmail.com'

name2 = name.replace('Name:', ' ')
name3= name2.replace('Email:', ' ').strip().split(' ')

print(name3)