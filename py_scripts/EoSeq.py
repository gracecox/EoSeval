from math import exp


def BMEOS(parameters):
	V = parameters(0)
	Vo = parameters(1)
	K = parameters(2)
	Kp= 4.0 	
	assert type(Vo) == float, 'Vo is not a float number'
	assert type(K) == float, 'K is not a float number'
	assert type(Kp) == float, 'Kp is not a float number'
	assert Kp == 4.0, 'This is trying to use BM3EOS for the 2nd Order Equation'
	
	n= Vo/V
	P = (((3.0/2.0)*K)
		*((n**(7.0/3.0))-(n**(5.0/3.0))))

	return P
	
def BM3EOS(parameters):
	V = parameters(0)
	Vo = parameters(1)
	K = parameters(2)
	Kp= parameters(3)
	
	assert type(Vo) == float, 'Vo is not a float number'
	assert type(K) == float, 'K is not a float number'
	assert type(Kp) == float, 'Kp is not a float number'
	
	n= Vo/V
	P= (((3.0/2.0)*K)
		*((n**(7.0/3.0))-(n**(5.0/3.0)))
		*(1+((3.0/4.0)*(Kp-4.0)*((n**(2.0/3.0))-1))))
	
	return P
	
def VINETEOS(parameters):
	V = parameters(0)
	Vo = parameters(1)
	K = parameters(2)
	Kp= parameters(3)
	
	assert type(Vo) == float, 'Vo is not a float number'
	assert type(K) == float, 'K is not a float number'
	assert type(Kp) == float, 'Kp is not a float number'
	
	n= (V/Vo)**(-1.0/3.0)
	P = (3*K*((1-n)/(n**2))
		*math.exp((3.0/2.0)*(Kp-1)*(1-n)))
		
	return P