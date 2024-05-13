 -- Problem 1 : Make a Pandas DataFrame with two-dimensional list 
 
 
 def createDataframe(student_data: List[List[int]]) -> pd.DataFrame:
    df1 = pd.DataFrame(student_data, columns=['student_id','age'])
    return df1
 
 
 
 -- Problem 2 : Big Countries
 
 
 def big_countries(world: pd.DataFrame) -> pd.DataFrame:
    return world[(world.area >=3000000) | (world.population >= 25000000)][["name","population","area"]]
 
 
 
 -- Problem 3 : Recyclable and low fat products
 
 
 
 def find_products(products: pd.DataFrame) -> pd.DataFrame:
    return pd.DataFrame(products[(products.low_fats == 'Y') & (products.recyclable == 'Y')]['product_id'])
 
 
 -- Problem 4 : Customer who never order 
 
 
def find_customers(customers: pd.DataFrame, orders: pd.DataFrame) -> pd.DataFrame:
    df1 = pd.merge(customers,orders, left_on = 'id', right_on='customerId',how='left')
    return pd.DataFrame({'Customers' : df1[df1['customerId'].isnull()]['name']})
    