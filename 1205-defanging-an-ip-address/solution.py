class Solution:
    def defangIPaddr(self, address: str) -> str:
        list=address.split(".")
        return "[.]".join(list)
