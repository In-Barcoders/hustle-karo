class Solution:
    def simplifyPath(self, path: str) -> str:
        inp = path.split('/')
        arr = []
        for i in inp:
            if i in ['.', '']:
                continue
            if i == '..':
                if not arr == []:
                    arr.pop()
            else:
                arr.append(i)
        return '/' + '/'.join(arr)
