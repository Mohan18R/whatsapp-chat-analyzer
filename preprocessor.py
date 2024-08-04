import re
import pandas as pd

# Function to preprocess chat data
def preprocess(data):
    # Updated regex pattern to match the date and time format in the sample file
    pattern = r'\d{2}/\d{2}/\d{2,4},\s\d{1,2}:\d{2}\s[ap]m\s-\s'

    messages = re.split(pattern, data)[1:]
    dates = re.findall(pattern, data)

    df = pd.DataFrame({'user_message': messages, 'message_date': dates})
    
    # Convert message_date to datetime using the correct format
    df['message_date'] = pd.to_datetime(df['message_date'], format='%d/%m/%y, %I:%M %p - ')

    df.rename(columns={'message_date': 'date'}, inplace=True)

    users = []
    messages = []
    for message in df['user_message']:
        entry = re.split(r'([\w\W]+?):\s', message)
        if entry[1:]:  # user name
            users.append(entry[1])
            messages.append(" ".join(entry[2:]))
        else:
            users.append('group_notification')
            messages.append(entry[0])

    df['user'] = users
    df['message'] = messages
    df.drop(columns=['user_message'], inplace=True)

    df['only_date'] = df['date'].dt.date
    df['year'] = df['date'].dt.year
    df['month_num'] = df['date'].dt.month
    df['month'] = df['date'].dt.month_name()
    df['day'] = df['date'].dt.day
    df['day_name'] = df['date'].dt.day_name()
    df['hour'] = df['date'].dt.hour
    df['minute'] = df['date'].dt.minute

    period = []
    for hour in df['hour']:
        if hour == 23:
            period.append(f"{hour}-{str(0).zfill(2)}")
        elif hour == 0:
            period.append(f"{str(0).zfill(2)}-{str(hour + 1).zfill(2)}")
        else:
            period.append(f"{hour}-{hour + 1}")

    df['period'] = period

    return df
