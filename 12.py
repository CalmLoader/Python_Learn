#函数的多个返回值
import math
PI=3.14159

def mov(x,y,step,angle=0):
	nx=x+step*math.cos(angle)
	ny=y-step*math.sin(angle)
	return nx,ny

x,y=mov(100,100,60,math.pi/6)
r=mov(100,100,60,math.pi/6)
print(x,y)

print(r)

#practice
def quadratic(a,b,c):
	x=math.pow(b,2)-4*a*c
	if(x<0):
		return
	elif x==0:
		return -b/(2*a)
	else:
		r1=(-b+math.sqrt(x))/(2*a)
		r2=(-b-math.sqrt(x))/(2*a)
		return (r1,r2)

print(quadratic(2,3,1))
print(quadratic(1,3,-4))