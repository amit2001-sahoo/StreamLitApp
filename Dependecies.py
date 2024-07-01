import pandas as pd
import streamlit as st

columns = ['Serial Number','Country','Holiday Date','Holiday Description']
holiday_df = pd.DataFrame(columns= columns)
edited_df = pd.DataFrame()
def find_length(edited_df):
    return len(edited_df)

# df_melted = df2.melt(id_vars=tf, var_name='subcategory', value_name='Value')
# fig = px.bar(df_melted, x='Value', y=tf, orientation='h',
#             barmode='stack', color='subcategory',text='subcategory')
# fig.update_traces(textposition='inside')
# fig.update_layout(
#     barmode='stack',  # Stack the bars
#     title='Predicted Ticket Count ',
#     legend=dict(
#     orientation='h',  # Set the legend to be horizontal
#     x=0.5,  # Center the legend horizontally
#     y=-0.1,  # Position the legend below the chart
#     xanchor='center',  # Anchor the legend horizontally at the center
#     yanchor='top'  # Anchor the legend vertically at the top
#     ),
#     yaxis_title='Predicted Ticket Count',
# )
# # Display the chart in Streamlit
# st.plotly_chart(fig)

# st.title('Vertical Graph')
# def find_series(df,category,subcategory,ticket_type):
#     data = df.copy()
#     age_values = [0] * 4
#     if category == 'All Category' and ticket_type == 'All Type' and subcategory == 'All Subcategories':
#         data['Call Date'] = pd.to_datetime(data['Call Date']).dt.date
#         age_values = find_age(df)
#         data = data.groupby('Call Date')['Ticket Number'].count().reset_index(name='all').fillna(0)
#         data.set_index('Call Date',inplace=True)
#         date_range = pd.date_range(start=data.index.min(),end=data.index.max())
#         data = data.reindex(date_range,fill_value=0)
#         data = data.rename_axis('Call Date').reset_index()
#         data.rename(columns={"Ticket Number": "all"}, inplace=True)
        
       
#     elif ticket_type == 'All Type' and category != 'All Category' and subcategory == 'All Subcategories':
#         data['Call Date'] = pd.to_datetime(data['Call Date']).dt.date
#         data = data[data['Category'] == category]
#         age_values = find_age(data)
#         data = data.groupby('Call Date')['Ticket Number'].count().reset_index(name='all').fillna(0)
#         data.set_index('Call Date',inplace=True)
#         date_range = pd.date_range(start=data.index.min(),end=data.index.max())
#         data = data.reindex(date_range,fill_value=0)
#         data = data.rename_axis('Call Date').reset_index()
#         data.rename(columns={"Ticket Number": "all"}, inplace=True)
        
        
#     elif ticket_type != 'All Type' and category == 'All Category' and subcategory == 'All Subcategories':
#         data['Call Date'] = pd.to_datetime(data['Call Date']).dt.date
#         data = data[data['Ticket Type'] == ticket_type]
#         age_values = find_age(data)
#         data = data.groupby('Call Date')['Ticket Number'].count().reset_index(name='all').fillna(0)
#         data.set_index('Call Date',inplace=True)
#         date_range = pd.date_range(start=data.index.min(),end=data.index.max())
#         data = data.reindex(date_range,fill_value=0)
#         data = data.rename_axis('Call Date').reset_index()
#         data.rename(columns={"Ticket Number": "all"}, inplace=True)
        
        
#     elif category != 'All Category' and subcategory != 'All Subcategories' and ticket_type == 'All Type':
#         data['Call Date'] = pd.to_datetime(data['Call Date']).dt.date
#         data = data[data['Category'] == category]
#         data = data[data['Subcategory'] == subcategory]
#         age_values = find_age(data)
#         data = data.groupby('Call Date')['Ticket Number'].count().reset_index(name='all').fillna(0)
#         data.set_index('Call Date',inplace=True)
#         date_range = pd.date_range(start=data.index.min(),end=data.index.max())
#         data = data.reindex(date_range,fill_value=0)
#         data = data.rename_axis('Call Date').reset_index()
#         data.rename(columns={"Ticket Number": "all"}, inplace=True)
        
#     elif ticket_type != 'All Type' and category != 'All Category' and subcategory == 'All Subcategories':
#         data['Call Date'] = pd.to_datetime(data['Call Date']).dt.date
#         data = data[data['Category'] == category]
#         data = data[data['Ticket Type'] == ticket_type]
#         age_values = find_age(data)
#         data = data.groupby('Call Date')['Ticket Number'].count().reset_index(name='all').fillna(0)
#         data.set_index('Call Date',inplace=True)
#         date_range = pd.date_range(start=data.index.min(),end=data.index.max())
#         data = data.reindex(date_range,fill_value=0)
#         data = data.rename_axis('Call Date').reset_index()
#         data.rename(columns={"Ticket Number": "all"}, inplace=True)
        
        
#     elif ticket_type != 'All Type' and category != 'All Category' and subcategory != 'All Subcategories':
#         data['Call Date'] = pd.to_datetime(data['Call Date']).dt.date
#         data = data[data['Category'] == category]
#         data = data[data['Subcategory'] == subcategory]
#         data = data[data['Ticket Type'] == ticket_type]
#         age_values = find_age(data)
#         data = data.groupby('Call Date')['Ticket Number'].count().reset_index(name='all').fillna(0)
#         data.set_index('Call Date',inplace=True)
#         date_range = pd.date_range(start=data.index.min(),end=data.index.max())
#         data = data.reindex(date_range,fill_value=0)
#         data = data.rename_axis('Call Date').reset_index()
#         data.rename(columns={"Ticket Number": "all"}, inplace=True)

#     return data,age_values