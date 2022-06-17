from turtle import color
import uuid, base64
from customers.models import Customer
from profiles.models import Profile
from io import BytesIO
import matplotlib as plt
import matplotlib.pyplot as pltpy
import seaborn as sns

def generate_code():
    code = str(uuid.uuid4()).replace('-', '')[:12]
    return code

def get_salesman_from_id(val):
    salesman = Profile.objects.get(id=val)
    return salesman.user.username

def get_customer_from_id(val):
    customer = Customer.objects.get(id=val)
    return customer

def get_graph():
    buffer = BytesIO()
    pltpy.savefig(buffer, format='png')
    buffer.seek(0)
    image_png = buffer.getvalue()
    graph = base64.b64encode(image_png)
    graph = graph.decode('utf-8')
    buffer.close()
    return graph

def get_key(res_by):
    if res_by == '#1':
        key = 'transaction_id'
    elif res_by == '#2':
        key = 'created'
    else:
        print('There was an error with the results chosen')
    return key

def get_chart(chart_type, data, results_by, **kwargs):
    plt.use('AGG')
    fig = pltpy.figure(figsize=(10,4))
    key = get_key(results_by)
    d = data.groupby(key, as_index=False)['total_price'].agg('sum')
    if chart_type == '#1':
        print("bar chart")
        #pltpy.bar(data[key], data['total_price'])# this is implementing a bar chart using matplotlib
        sns.barplot(x=key, y='total_price', data=data)
    elif chart_type == '#2':
        print("pie chart")
        colors = sns.color_palette('deep')[0:5]
        pltpy.pie(data=d, x='total_price', labels=d[key].values, colors=colors)
    elif chart_type == '#3':
        print("line chart")
        pltpy.plot(d[key], d['total_price'], color="teal")
    else:
        print("Error with chart type")
    pltpy.tight_layout()
    chart = get_graph()
    return chart