
# TODO: import some code
from app.shopping import format_usd, find_product
import os
from pandas import read_csv

# TODO: test the code

def test_format_usd():
    assert format_usd(9.5) == "$9.50"


#add lookup product test - need that function in shopping.py
#should return that product's dictionary
#also test invalid result - should return None

mock_filepath = os.path.join(os.path.dirname(__file__), "mock_data", "mock_products.csv")
mock_df = read_csv(mock_filepath)
mock_products = mock_df.to_dict("records")

def test_lookups():
    #good lookup
    valid_lookup = find_product("3", mock_products)
    assert valid_lookup == {
        'id': 3, 
        'name': 'Product 3', 
        'aisle': 'Aisle C', 
        'department': 'beverages',
        'price': 2.49
    }
    #bad lookup
    invalid_lookup = find_product("100000", mock_products)
    assert invalid_lookup == None
