class Title_sq:
    """
    This defines the data schema for a Squarespace product according to the existing structure of a squarespace products CSV.

    This can later be seperated in mutable and immutable data fields for code-clarity.
    """

    def __init__(self, product_id, variant_id, product_type, product_page, product_url, title, description, sku, option_name_1, option_value_1, option_name_2, option_value_2, option_name_3, option_value_3, price, sale_price, on_sale, stock, categories, tags, weight, length, width, height, visible, hosted_image_urls):

        self.product_id = product_id
        self.variant_id = variant_id
        self.product_type = product_type
        self.product_page = product_page
        self.product_url = product_url
        self.title = title
        self.description = description
        self.sku = sku
        self.option_name_1 = option_name_1
        self.option_value_1 = option_value_1
        self.option_name_2 = option_name_2
        self.option_value_2 = option_value_2
        self.option_name_3 = option_name_3
        self.option_value_3 = option_value_3
        self.price = price
        self.sale_price = sale_price
        self.on_sale = on_sale
        self.stock = stock
        self.categories = categories
        self.tags = tags
        self.weight = weight
        self.length = length
        self.width = width
        self.height = height
        self.visible = visible
        self.hosted_image_urls = hosted_image_urls

# "Product ID [Non Editable]","Variant ID [Non Editable]","Product Type [Non Editable]","Product Page","Product URL","Title","Description","SKU","Option Name 1","Option Value 1","Option Name 2","Option Value 2","Option Name 3","Option Value 3","Price","Sale Price","On Sale","Stock","Categories","Tags","Weight","Length","Width","Height","Visible","Hosted Image URLs"
