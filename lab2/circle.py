def get_circle_info(r: float):
    pi = 3.1415926
    circumference = 2 * pi * r
    area = pi * (r ** 2)
    
    print("The area of the circle is: ", area,"\n The circumference of the circle is: ", circumference)
    print(f"Area is {area:.2F}, circumference is {circumference:.2F}")

get_circle_info(5)