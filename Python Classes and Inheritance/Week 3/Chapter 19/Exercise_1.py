# Below, we have provided buggy code. Add a try/except clause so the code runs without errors. If a blog post didn’t get
# any likes, a ‘Likes’ key should be added to that dictionary with a value of 0.

blog_posts = [{'Photos': 3, 'Likes': 21, 'Comments': 2}, {'Likes': 13, 'Comments': 2, 'Shares': 1},
              {'Photos': 5, 'Likes': 33, 'Comments': 8, 'Shares': 3}, {'Comments': 4, 'Shares': 2},
              {'Photos': 8, 'Comments': 1, 'Shares': 1}, {'Photos': 3, 'Likes': 19, 'Comments': 3}]
total_likes = 0

for post in blog_posts:
    try:
        post.keys() == 'Likes'
        total_likes = total_likes + post['Likes']
    except KeyError:
        post['Likes'] = 0

print(total_likes)
