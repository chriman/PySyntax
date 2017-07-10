#coding:utf-8
#递归函数：一个函数在内部调用自身本身

def fact(n):
    if n == 1:
        return 1
    return n * fact(n-1)

def fact_optimized(n):
    return fact_iter(n,1)

def fact_iter(num,product):
    if num == 1:
        return product
    return fact_iter(num-1,num*product)

def fact2(n,result=1):
    result = n * result
    if n == 1:
        return result 
    return fact2(n-1,result)

if __name__ == "__main__":
#     result = fact(5)        #120
#     result = fact(1000)     #出现栈溢出，RecursionError: maximum recursion depth exceeded in comparison
#     result = fact2(1000)
    result = fact_optimized(1000)

    print(result)
    
    
    
