
#შეამოწმეთ როგორი არის რიცხვი, ანუ დადებითია თუ უარყოფითი,და დააბრუნეთ საპირისპირო ნიშნის მქონე რიცხვი, ანუ თუ დადებითია დაპრინტეთ  უარყოფითი, ხოლო თუ უარყოფითია დაპრინტეთ დადებითი

num = int(input('Type in a number: '))

if num >=0:
    print(str(num) + ' is positive, its opposite is ' + str(num * -1))
else:
    print(str(num) + ' is negative, its opposite is ' + str(num * -1))