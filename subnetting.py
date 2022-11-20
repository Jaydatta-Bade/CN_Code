
Ip = "198.168.1.1/26"
m = Ip.split(".")

cidr = Ip.split("/")
# print(int(m[0]))

print( "CIDR:- ",cidr[1])


def classAsunmask():
    print("It's in class A" )
    print( f'Subnet_mask:- 255.0.0.0' )
    print("Default Subnet Mask for class A:- 11111111.00000000.00000000.00000000")

def classBsunmask():
    print("It's in class B" )
    print( f'Subnet_mask:- 255.255.0.0' )
    print("Default Subnet Mask for class B:- 11111111.11111111.00000000.00000000")
    
    
def classCsunmask():
    print("It's in class C" )
    print( f'Subnet_mask:- 255.255.255.0' )
    print("Default Subnet Mask for class D:- 11111111.11111111.11111111.00000000")
    
    getSubnerMask()

def classDsunmask():
    print("It's in class D" )
    print("Default Subnet Mask is not defined for class D")


def getSubnerMask():
    port_no = cidr[1] # 28 
    rem_bits = 32 - int(port_no)  #32- 28 = 4 
    rem_val = 2 ** rem_bits - 1 # 2 ** 4 - 1 = 15 
    add_val = 255 - rem_val  # 255 - 15 = 
    print("subnet Mask is " +"255.255.255."+ str(add_val))

def check_class():

    if ( 0 < int( m[0]) <= 127):
        classAsunmask()
        
    
    elif ( 128 <= int( m[0]) <= 191):
        classBsunmask()
        
    
    elif ( 192 <= int( m[0]) <= 223):
        classCsunmask()
    
        
    elif ( 224 <= int( m[0]) <= 239):
        classDsunmask()
    

check_class()
