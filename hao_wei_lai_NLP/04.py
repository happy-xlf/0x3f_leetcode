#
# 代码中的类名、方法名、参数名已经指定，请勿修改，直接返回方法规定的值即可
#
# 
# @param s string字符串 
# @return bool布尔型
#
# 判断字符串是否有效
#左括号必须用相同右括号闭合。
# 左括号必须以正确的顺序闭合。
class Solution:
    def isValid(self , s: str) -> bool:
        # write code here
        st = []
        for i in s:
            if i == '(' or i == '[' or i == '{':
                st.append(i)
            else:
                if len(st) == 0:
                    return False
                if i == ')' and st[-1] != '(':
                    return False
                if i == ']' and st[-1] != '[':
                    return False
                if i == '}' and st[-1] != '{':
                    return False
                st.pop()
        if len(st) == 0:
            return True
        else:
            return False
