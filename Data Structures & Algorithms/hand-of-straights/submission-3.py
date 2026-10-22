# class Solution:
    # def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
    #     if (not len(hand)%4):
    #         return False

    #     count = Counter(hand)
    #     hand.sort()
    #     for i in range(len(hand)):
    #         if count[hand[i]]:
    #             for j in range(hand[i], hand[i]+ groupSize):
    #                 if not count[j]:
    #                     return False
    #                 count[j] -= 1
            
    #     return True

class Solution:
    def isNStraightHand(self, hand, groupSize):
        if len(hand) % groupSize:
            return False

        count = Counter(hand)
        hand.sort()
        for num in hand:
            if count[num]:
                for i in range(num, num + groupSize):
                    if not count[i]:
                        return False
                    count[i] -= 1
        return True