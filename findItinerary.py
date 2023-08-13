"""
You are given a list of airline tickets where tickets[i] = [fromi, toi] represent the departure and the arrival airports
of one flight. Reconstruct the itinerary in order and return it.

All the tickets belong to a man who departs from "JFK", thus, the itinerary must begin with "JFK".
If there are multiple valid itineraries, you should return the itinerary that has the smallest lexical order when read
as a single string.

For example, the itinerary ["JFK", "LGA"] has a smaller lexical order than ["JFK", "LGB"].
You may assume all tickets form at least one valid itinerary. You must use all the tickets once and only once.

Input: tickets = [["MUC","LHR"],["JFK","MUC"],["SFO","SJC"],["LHR","SFO"]]
Output: ["JFK","MUC","LHR","SFO","SJC"]

"""


def findItinerary(tickets):
    adj = {src_city: [] for src_city, dst_city in tickets}

    for src_city, dst_city in sorted(tickets)[::-1]:
        adj[src_city].append(dst_city)

    stack = ['JFK']
    res = []

    print(adj)
    while stack:
        elem = stack[-1]
        if elem in adj and len(adj[elem]) > 0:
            stack.append(adj[elem].pop())
        else:
            res.append(stack.pop())

    return res[::-1]


tickets = [["JFK", "SFO"], ["JFK", "ATL"], ["SFO", "ATL"], ["ATL", "JFK"], ["ATL", "SFO"]]
# Output: ["JFK","ATL","JFK","SFO","ATL","SFO"]
print(findItinerary(tickets))


