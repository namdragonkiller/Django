#proejct_02.py에 게시글을 저장하는 class를 만들려고 합니다.
# 클래스 안에 들어갈 변수는 ( id, title, author, content) 으로 모두 빈 문자열로 저장하고,
# 게시글 한 개를 저장해 보세요!

class post:
    id = ''
    title = ''
    author = ''
    content = ''

board= post()
board.id = 'skaekqls789'
board.title = 'post'
board.author = '남다빈'
board.content = '수업이 재밌다.'

print('id: ' + board.id)
print('title: ' + board.title)
print('author: ' + board.author)
print('content: ' + board.content)