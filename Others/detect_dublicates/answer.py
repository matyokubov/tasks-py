# Input
users = [
    "naucoder",
    "iceman",
    "abikbaev",
    "abikbaev",
    "petr",
    "abikbaev",
    "abikbaev",
    "x",
    "abikbaev",
    "acrush",
    "x"
]

def detectSpammers(usersList):
    res = []
    for user in usersList:
        usersList.count(user)!=1 and res.append(user)
    return sorted(set(res))

# Output
spammers = detectSpammers(users)
print(*spammers)