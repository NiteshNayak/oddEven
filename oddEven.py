#Number odd or even
#nnayak


def oddEven(numb):
    if numb % 2 == 0:
        print 'Number is Even'
    else:
        print 'Number is Odd'

try:
    iNumb = input("Enter a number: ")
    oddEven(iNumb)
except:
    print('Kindly enter a number only')
