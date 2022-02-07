import streamlit as st

st.title("... Welcome to Marz Cafe' !!!")
st.subheader("fresh homemade meals")


from PIL import Image
img = Image.open("marz cafe logo.png")

st.image(img, width=100)


customer_name = st.text_input("Customer Name:\n")

city = st.selectbox("Select Location: ",
                     [ 'Port-Harcourt', 'Lekki', 'Uyo', 'Abuja'])

location = st.text_input("Others:\n")

order_type = st.selectbox("Select Order Type: ",
                     [ 'Table-Reservation', 'Dine-in', 'Take-Out', 'Delivery'])

order_date = st.date_input('Date of Order')

meal_item = {}
meal_history = []


st.text("Details of your order")

meal_name = st.radio("Select Dish: ", ('Continental', 'National'))


continental_dishes = ["Basmati Rice", "Spaghetti Bolognese", "Singapore Noodles"]


continental_dishes.append("Chicken Curry Sauce")
continental_dishes.append("Steak")
continental_dishes.append("Lamb")


st.text("\nContinental dishes: ")
st.text(continental_dishes)

meal_type = st.selectbox("Continental Combo: ",
                     [ 'Rice + Chicken Curry Sauce', 'Spaghetti Bolognese + Steak', 'Singapore Noodles + Lamb', 'None' ])


national_dishes = ["Afang Soup", "Egusi Soup", "Fisherman Soup"]

national_dishes.append("Goatmeat")
national_dishes.append("Fresh Fish")
national_dishes.append("Cowleg")

st.text("\nNational Dishes: ")
st.text(national_dishes)

meal_type = st.selectbox("National Combo: ",
                     [ 'Afang Soup + Goatmeat', 'Egusi Soup + Cowleg', 'Fisherman Soup + Fresh Fish', 'None' ])


meal_name = st.text_input("Meal Name :\n")

quantity = st.number_input("Number:\n")

confirm_Order = st.checkbox('I agree')

cost = st.number_input("Price:\n")


meal_item = {'name':meal_name, 'number':int(quantity), 'price':(cost)}
meal_history.append(meal_item)

grand_total = 0

for index,meal in enumerate(meal_history):
    meal_total = meal['number'] * meal['price']
    grand_total = grand_total + meal_total
    ('%d %s @ N%.2fSub_Total N%.2f' % (meal['number'], meal['name'], meal['price'], meal_total))
    
delivery_fee = 0

discount_amount = 0


st.text("Your Total Bill is ....")


st.write('Grand Total: N%.2f' % grand_total )

payment_mode = st.selectbox("Select Preferred Pay Option: ",
                     ['Cash', 'Card', 'Transfer', 'None'])

st.write("You have Selected: ", payment_mode)


payment_Mode = st.text_input("If None state other pay option\n")


receipt_number = st.text_input("Receipt No:\n")

st.text("Your Order has been confirmed and your Total Bill paid in full ")


payment_status = st.radio("Confirmation: ", ('YES', 'NO'))


if (payment_status == 'YES'):
    st.button("YES")
    st.text('Order Completed')
    
else:
    st.button("NO")
    st.text('Order Incomplete')
    
delivery_mode = st.selectbox("Select preferred handling: ",
                     ['Dispatch Rider', 'Pickup'])

st.write("You have Selected: ", delivery_mode)


delivery_mode = st.text_input("Delivery Location\n")

st.text("*Standard dispatch fare applies for home or office delivery citywide, N1500" )    
    
if(st.button('Submit')):
    st.text('Thank You')
    
    st.text('Have a Good Day!!!')


