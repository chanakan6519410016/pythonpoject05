#return not values
#หมายถึง การสิ้นสุดหรือจบการทำงานของ Block Scope การทำงานหนึ่งๆ เมื่อมันถูกงาน

def func1( ) :
    print('AAA')
    print('BBB')
    return
    print('CCC')
    

def func2( x ) :
    return
    print(f'X is {x}')
    
func1( )
func2( 10 )
