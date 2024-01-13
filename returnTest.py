#파라미터: 함수에 넘겨주는 값

def get_square(x):
    return x + x
    
# 함수 사용 1
print(get_square(3))    

# 함수 사용 2
y=get_square(3)
print(y)

# 함수 사용 3
# 2 + 4
print(get_square(1)+get_square(2))