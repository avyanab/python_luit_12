#Start with an empty list of AWS services
aws_services = []
print(aws_services)
print("The list is empty")

#Populate list using insert
aws_services.insert(0, 'cloudformation')
aws_services.insert(1, 'IAM')
aws_services.insert(2, 'KMS')
aws_services.insert(3, 'Lambda')

#Print the list and the length of the list
print(aws_services)
print("This list is", len(aws_services), "items long")

#Remove last two services from the list by index
aws_services[2:] = []

#Print the new list and new length of the list
print(aws_services)
print("This list is now", len(aws_services), "items long")