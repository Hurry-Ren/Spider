import urllib.request
import re
def comment(book_id):
    # 拼接评论链接，获取评论信息
    comment = []
    for i in range(0, len(book_id)):
        url = 'https://club.jd.com/comment/productCommentSummaries.action?referenceIds='+book_id[i]
        targetData = urllib.request.urlopen(url).read().decode('utf-8','ignore')
        #"CommentCount":858970,
        pat = '"CommentCount":(.*?),'
        res = re.compile(pat).findall(targetData)
        comment.append(res)

    return comment

