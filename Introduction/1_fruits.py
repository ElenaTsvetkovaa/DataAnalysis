import pandas as pd

# Exercise 1
fruits_data = {
    'Apple': 30,
    'Banana': 21
}

df1 = pd.DataFrame([fruits_data])


# Exercise 2
fruit_sales = [
    {'Apple': 35, 'Banana': 21},
    {'Apple': 41, 'Banana': 34}
]

sales_df = pd.DataFrame(fruit_sales, index=['2017 Sales', '2018 Sales'])


# Exercise 3
ingredients = pd.Series(
    data=['4 cups', '1 cup', '2 large', '1 can'],
    index=['Flour', 'Milk', 'Eggs', 'Spam'],
    name='Dinner'
)
print(ingredients)




