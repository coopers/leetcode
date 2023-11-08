from collections import defaultdict, deque


class Solution(object):
    def __init__(self):
        self.length = 0
        self.adjacent_words = defaultdict(list)

    def visitWordNode(self, queue, visited, others_visited):
        queue_size = len(queue)
        for _ in range(queue_size):
            current_word = queue.popleft()
            for i in range(self.length):
                intermediate_word = current_word[:i] + "*" + current_word[i+1:]
                for word in self.adjacent_words[intermediate_word]:
                    if word in others_visited:
                        return True
                    if word not in visited:
                        visited.add(word)
                        queue.append(word)
                        
        return False

    def ladderLength(self, beginWord, endWord, wordList):
        if (
            not beginWord or
            not endWord or
            not wordList or
            endWord not in wordList
        ):
            return 0

        self.length = len(beginWord)
        for word in wordList:
            for i in range(self.length):
                self.adjacent_words[word[:i] + "*" + word[i+1:]].append(word)

        queue_begin = deque([beginWord])
        queue_end = deque([endWord])
        visited_begin = {beginWord}
        visited_end = {endWord}
        count = 2
        while queue_begin and queue_end:
            if len(queue_begin) <= len(queue_end):
                ans = self.visitWordNode(queue_begin, visited_begin, visited_end)
            else:
                ans = self.visitWordNode(queue_end, visited_end, visited_begin)
            if ans:
                return count
            count += 1

        return 0