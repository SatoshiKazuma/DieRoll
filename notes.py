#die
#system picks random number
#number corresponds to variable on die
#some of them are blank spaces while others are circles
# dierows = [[1, 2, 3],[4, 5, 6], [7, 8, 9]]
# print(f'{dierows[0]}\n{dierows[1]}\n{dierows[2]}')
# [a, b, c]
# [d, e ,f]
# [g, h, i]
# die,a,b,c,d,e,f,g,h,i
# 1," "," "," "," ",⏺," "," "," "," "
# 2,"⏺"," "," "," "," "," "," "," ",⏺
# 3,"⏺"," "," "," ",⏺," "," "," ",⏺
# 4,"⏺"," ",⏺," "," "," ",⏺," ",⏺
# 5,"⏺"," ",⏺," ",⏺," ",⏺," ",⏺
# 6,"⏺"," ",⏺,⏺," ",⏺,⏺," ",⏺

# die,1,2,3,4,5,6
# " a "," ",⏺,⏺,⏺,⏺,⏺
# " c "," "," "," ",⏺,⏺,⏺
# " d "," "," "," "," "," ",⏺
# " e ",⏺," ",⏺," ",⏺," "
# " f "," "," "," "," "," ",⏺
# " g "," "," "," ",⏺,⏺,⏺
# " i "," ",⏺,⏺,⏺,⏺,⏺

# dierows = [[a, b, c],[d, e, f], [g, h, i]]
#     result = str(f'{dierows[0]}\n{dierows[1]}\n{dierows[2]}')
#     print(result.strip('[').strip(']').strip(',').strip("'"))