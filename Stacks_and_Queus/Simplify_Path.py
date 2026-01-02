class Solution:
    def simplifyPath(self, path: str) -> str:
        stack = []

        for dir in path.split('/'):
            #we will check if the path contains ..
            if dir == "..":
                if stack:
                    stack.pop()
            elif dir == "." or not dir:
                continue
            else:
                stack.append(dir)
        
        return "/" + "/".join(stack)
