# 1461 - 도서관


N, limit = map(int, input().split())
books = list(map(int, input().split()))

negative = []
positive = []
answer = 0

for book in books:
    if book < 0 :
        negative.append(abs(book))
    else:
        positive.append(book)

negative.sort()
positive.sort()

far_val = 0

def book_pop(books):
    global answer, far_val
    
    while books:
        
        book = books.pop()
        answer += book * 2
        
        far_val = max(book, far_val)
        
        for _ in range(limit-1):
            try:
                books.pop()
            except IndexError:
                break
        

book_pop(negative)
book_pop(positive)

print(answer-far_val)

# 7 2
# -37 2 -6 -39 -29 11 -28

# 131