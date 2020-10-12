class Title_eb:
    """
    This defines the data schema for a FoxPRO product record according to the existing structure of a CSV exported from a FoxPRO DBF.
    
    I hate FoxPRO.

    This can later be seperated in mutable and immutable data fields for code-clarity.
    """

    def __init__(self, isbn, none, title, qty_sold, cost_of_sales, nett_sales, rrp, on_hand, profit):

        self.isbn = isbn
        self.none = none
        self.title = title
        self.qty_sold = qty_sold
        self.cost_of_sales = cost_of_sales
        self.nett_sales = nett_sales
        self.rrp = rrp
        self.on_hand = on_hand
        self.profit = profit

# ISBN,,TITLE,QTY,COST OF,NETT,RRP,ON,PROFIT
# ,,,SOLD,SALES,SALES,,HAND,
