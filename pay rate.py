#funcion to convert input to float
def conv_tofloat(x):
    try:
        y = float(x)
        return y
    except:
        print("Please enter numeric input")
        quit()

#get user inputs and convert them to floats
hours = input("Enter hours:")
h = conv_tofloat(hours)

rate = input("Enter rate per hour:")
r = conv_tofloat(rate)

#calculate pay per hour including overtime after 40 hours
if h <= 40 :
	pay = h * r
	print(pay)
else :
	ot = h - 40
	otpay = ot * (r * 1.5)
	pay = 40 * r
	print(otpay + pay)