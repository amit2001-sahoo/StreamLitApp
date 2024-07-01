import streamlit as st
import snowflake.connector
import pandas as pd
from datetime import datetime,timedelta
import random

@st.cache_data
def find_data():
    sf_creds = {
        'user': 'AMITDEMO',
        'password': 'Amit@2001',
        'account': 'YODPKGM-JI93499',
        'warehouse': 'COMPUTE_WH',
        'database': 'DEMOSTREAMLIT',
        'schema': 'PUBLIC',
        'role': 'ACCOUNTADMIN'
    }
    
    conn = snowflake.connector.connect(**sf_creds)
    
    cursor = conn.cursor()
    
    # SQL query
    table='user_panel_ticketvolumeforcastmodel'
    query = f"SELECT * FROM {table}"
    
    # Execute the query and fetch the results
    cursor.execute(query)
    results = cursor.fetchall()
    
    # Get the column names from the cursor description
    columns = [desc[0] for desc in cursor.description]
    
    # Create a pandas DataFrame
    df = pd.DataFrame(results, columns=columns)
    df2 = pd.read_excel(r'uploaded_excel_file_2024-06-13.xlsx')
    df2['Call Date'] = df2['Call Date'].dt.date
    df3 = pd.read_excel(r'C:\Users\CZ0223\Desktop\Streamlit\Oazis Master data 2.xlsx')
    # Close the cursor and connection
    cursor.close()
    conn.close()
    return df,df2,df3

# def show_pred_data()
month_dict = {
    1:'January',2:'February',3:'March',4:'April',5:'May',6:'June',7:'July',8:'August',9:'September',10:'October',11:'November',12:'December'
}

def find_last_six(period,df,current,year):
    result = []
    time_list = []
    if period == 'month':
        
        current = current - 1
        for i in range(6):
            if current == 0:
                current = 12
                year = year - 1
            result.insert(i,df[(df.month == current) & (df.year == year)].shape[0])
            time_list.insert(i,f'{month_dict[current]},{year}')
            current = current - 1
    if period == 'week':
        current = current - 1
        for i in range(6):
            if current == 0:
                current = 52
                year = year - 1
            result.insert(i,df[(df.week == current) & (df.year == year)].shape[0])
            time_list.insert(i,f'week{current},{year}')
            current = current - 1
    return result,time_list

def val_to_seg(value):
    if (value >= 0) and (value <= 30):
        return '0-30'
    elif (value >= 31) and (value <= 60):
        return '31-60'
    elif (value >= 61) and (value <= 90):
        return '61-90'
    else:
        return '90+'
    
def find_age(df):
    df['Call Date'] = pd.to_datetime(df['Call Date'])
    df_filtered = df[(df.Progress != 'Closed') & (df.Progress != 'Completed')].copy()
    df_filtered['DayDiffBy90']=((datetime.now()-df_filtered['Call Date']).dt.days)
    df_filtered['DayDiffSegment'] = df_filtered['DayDiffBy90'].apply(val_to_seg)
    ans = df_filtered.groupby(['DayDiffSegment'])['Ticket Number'].count().reset_index()
    # Initialize dictionary with all segments set to zero counts
    data_ageing_objects = {
        '0-30': 0,
        '31-60': 0,
        '61-90': 0,
        '90+': 0
    }
    # Update dictionary with actual counts
    for _, row in ans.iterrows():
        data_ageing_objects[row['DayDiffSegment']] = row['Ticket Number']
    result = [{'day_diff_segment': segment, 'ticket_count': count} for segment, count in data_ageing_objects.items()]
    return result

    
def find_actual_count(period,data):
    df = data.copy()
    cur_count = 0
    prev_count = 0
    last_six = []
    df['Call Date'] = pd.to_datetime(df['Call Date'])
    df['year'] = df['Call Date'].dt.year
    if period == 'month':
        df['month'] = df['Call Date'].dt.month
        cur_month = datetime.now().month
        prev_month = cur_month - 1
        cur_year = datetime.now().year
        # st.dataframe(df[(df['month'] == cur_month)]['year'].value_counts())
        cur_count = df[(df['month'] == cur_month) & (df.year == cur_year)].shape[0]
        if cur_month == 1:
            prev_month = 12
            cur_year = cur_year - 1
        prev_count = df[(df['month'] == prev_month) & (df.year == cur_year)].shape[0]
        last_six,time_list = find_last_six(period,df,cur_month,cur_year)
        df.drop(columns=['year','month'],inplace=True)
        
        #Finding the Actual no of resolutions
        df['Completion Date'] = pd.to_datetime(df['Completion Date'])
        df['Completion Date'] = df['Completion Date'].fillna(pd.NA)
        df = df.dropna(subset=['Completion Date'])
        # st.dataframe(df['Completion Date'].tail(10))
        df['com_year'] = df['Completion Date'].dt.year
        df['com_month'] = df['Completion Date'].dt.month
        res_count = df[(df['com_month'] == cur_month)&(df['com_year'] == cur_year)].shape[0]
        prev_res = df[(df['com_month'] == prev_month) & (df.com_year == cur_year)].shape[0]
    if period == 'week':
        df['week'] = df['Call Date'].dt.isocalendar().week
        cur_week = datetime.now().isocalendar()[1]
        prev_week = cur_week - 1
        cur_year = datetime.now().year
        cur_count = df[(df['week'] == cur_week) & (df.year == cur_year)].shape[0]
        if prev_week == 0:
            prev_week = 52
            cur_year = cur_year - 1
        prev_count = df[(df['week'] == prev_week) & (df.year == cur_year)].shape[0]
        last_six,time_list = find_last_six(period,df,cur_week,cur_year)
        df.drop(columns=['year','week'],inplace=True)
        df['Completion Date'] = pd.to_datetime(df['Completion Date'])
        df['Completion Date'] = df['Completion Date'].fillna(pd.NA)
        df = df.dropna(subset=['Completion Date'])
        # st.dataframe(df['Completion Date'].tail(10))
        df['com_year'] = df['Completion Date'].dt.year
        df['com_week'] = df['Completion Date'].dt.isocalendar().week
        res_count = df[(df['com_week'] == cur_week)&(df['com_year'] == cur_year)].shape[0]
        prev_res = df[(df['com_week'] == prev_week) & (df.com_year == cur_year)].shape[0]
    return cur_count,cur_count-prev_count,last_six,time_list,res_count,prev_res

def find_series(df,category,subcategory,ticket_type,period):
    if category == 'All Category':
        category = None
    if subcategory == 'All Subcategories':
        subcategory = None
    if ticket_type == 'All Type':
        ticket_type = None

    if category is not None:
        df = df[df['Category'] == category]
    if subcategory is not None:
        df = df[df['Subcategory'] == subcategory]
    if ticket_type is not None:
        df = df[df['Ticket Type'] == ticket_type]
    
    ref_df = df.copy()
    actual_ticket_count,metric_actual,last_six,time_list,res_count,prev_res = find_actual_count(period,df)
    start = datetime.today()
    end = datetime.today()
    df['Call Date'] = pd.to_datetime(df['Call Date']).dt.date
    data = df.copy()
    age_values = find_age(df)
    data = data.groupby('Call Date')['Ticket Number'].count().reset_index(name='all').fillna(0)
    data.set_index('Call Date',inplace=True)
    if(data.shape[0] > 0):
        start = data.index.min()
        end = data.index.max()
    date_range = pd.date_range(start=start,end=end)
    data = data.reindex(date_range,fill_value=0)
    data = data.rename_axis('Call Date').reset_index()
    data.rename(columns={"Ticket Number": "all"}, inplace=True)
    return data,age_values,actual_ticket_count,metric_actual,last_six,time_list,res_count,prev_res,ref_df

def find_prediction_graph_skeleton(time_frame,selections,category,subcategory,ticket_typ,cat_options,sub_options,tt_options):
    cat_options.pop(0)
    data = {}
    leg = {}
    if time_frame == 'month':
        leg['month'] = []
        for i in range(len(selections)):
            leg['month'].insert(i,selections[i])
    else:
        leg['week'] = []
        for i in range(len(selections)):
            leg['week'].insert(i,selections[i])
    if category == 'All Category':
        data = leg  
        for i in range(len(cat_options)):
            temp = {}
            temp[cat_options[i]] = []
            data.update(temp)     
    elif category != 'All Category' and subcategory == 'All Subcategories':
        sub_options.pop(0)
        data = leg
        for i in range(len(sub_options)):
            temp = {}
            temp[sub_options[i]] = []
            data.update(temp)
    return data


def find_prediction_data(selections,skeleton):
    for i in range(len(selections)):
        for key,value in skeleton.items():
            if key == 'week' or key == 'month':
                continue
            value.append(random.randint(150,300))
    return skeleton
data,excel_data,master_data = find_data()

