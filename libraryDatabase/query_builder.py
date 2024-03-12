
class QueryBuilder(object):
    
    # Get all books 
    @staticmethod
    def query_title(title: str) -> str:
        base = "SELECT {} FROM {} JOIN {} {}"
        columns = "TITLE, AUTHOR, YEAR, STATUS"
        table1 = "BOOKCOPIES"
        table2 = "BOOKTITLES"
        on = "ON BOOKTITLES.TITLE LIKE %" + title + "%"
        query = base.format(columns, table1, table2, on)
        return query
    
    # Get all books by an author
    @staticmethod
    def query_author(author: str) -> str:
        base = "SELECT {} FROM {} JOIN {} {}"
        columns = "TITLE, AUTHOR, YEAR, STATUS"
        table1 = "BOOKCOPIES"
        table2 = "BOOKTITLES"
        on = "ON BOOKTITLES.AUTHOR=" + author
        query = base.format(columns, table1, table2, on)
        return query
    
    # Update status of an individual copy of a book
    # @staticmethod
    # def update_status(book_id: int)

    
    

def main():
    print("\n")
    print( QueryBuilder.query_title("Dune") )
    print( QueryBuilder.query_author("Frank Herbert") )
    print("\n")
    
main()