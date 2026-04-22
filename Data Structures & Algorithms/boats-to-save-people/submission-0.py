class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()
        boat_Count=0
        left,right=0,len(people)-1

        while left<=right:
            if people[left]+people[right]<=limit:
                left+=1
            right-=1
            boat_Count+=1

        return boat_Count