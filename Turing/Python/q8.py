book_ids = [1001,1002,1003,1004,1005,1006,1007,1008,1009]

overdue_ids ={1002,1006}

def display_sorted_books(books_ids, overdue_ids):
    found = False
    def helper(id):
        nonlocal found 
        if id in overdue_ids:
            found = True
            return (0,id)
        return (1,id)
    book_ids.sort(key=helper)
    return found

print(display_sorted_books(book_ids, overdue_ids))