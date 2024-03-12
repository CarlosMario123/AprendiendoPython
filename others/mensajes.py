from sherlock_lib import search_target

username = "john_doe"

result = search_target(username,sfw=True)

for k, v in result.items():
    print(f"{k}: {v}")